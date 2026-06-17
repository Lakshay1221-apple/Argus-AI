import os
import re
import sys
import json
import time
import logging
from pathlib import Path
from collections import defaultdict
from typing import List, Dict, Any, Tuple, Set, Optional

import numpy as np
from transformers import AutoTokenizer

# Config
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger("DatasetValidatorV2")

MODEL_NAME = "meta-llama/Llama-3.2-1B-Instruct"
FALLBACK_MODEL_NAME = "unsloth/Llama-3.2-1B-Instruct"

DATASETS_CONFIG = {
    "resume_job_fit_training_ready.jsonl": {
        "path": "argus/resume/datasets/processed/resume_job_fit_training_ready.jsonl",
        "primary_schema": ["instruction", "input", "output"],
        "fallback_schema": ["resume_text", "job_description_text", "label"],
        "name": "Resume Job Fit (Training Ready)",
    },
    "resume_sections_instruction.jsonl": {
        "path": "argus/resume/datasets/processed/resume_sections_instruction.jsonl",
        "primary_schema": ["instruction", "input", "output"],
        "name": "Resume Sections Instruction",
    },
    "resume_summary_synthetic.jsonl": {
        "path": "argus/resume/datasets/processed/resume_summary_synthetic.jsonl",
        "primary_schema": ["resume_text", "summary"],
        "name": "Resume Summary Synthetic",
    },
    "resume_review_synthetic_v1.jsonl": {
        "path": "argus/resume/datasets/processed/resume_review_synthetic_v1.jsonl",
        "primary_schema": ["resume_text", "review"],
        "name": "Resume Review Synthetic",
    }
}

REPORT_OUTPUT_PATH = "argus/resume/evaluation/active/final_dataset_validation_report_v2.md"

def parse_flexible_json_resilient(file_path: Path) -> Tuple[List[Dict[str, Any]], int]:
    """
    Parses JSON content. Resilient to concatenated JSON arrays/objects and malformed regions.
    Returns parsed records and malformed record count.
    """
    with open(file_path, "rb") as f:
        raw_bytes = f.read()
    content = raw_bytes.decode("utf-8").strip()

    if not content:
        raise ValueError(f"Empty file: {file_path.name}")

    # Case 1: Standard single JSON array/object
    try:
        data = json.loads(content)
        if isinstance(data, list):
            return [x for x in data if isinstance(x, dict)], 0
        elif isinstance(data, dict):
            return [data], 0
    except json.JSONDecodeError:
        pass

    # Case 2: Line-by-line JSON lines
    records = []
    malformed_count = 0
    lines = content.splitlines()
    is_json_lines = True
    for line in lines:
        line_str = line.strip()
        if not line_str:
            continue
        if line_str in ["[", "]", "],", "], [", "},", "}[", "]["]:
            continue
        try:
            records.append(json.loads(line_str))
        except json.JSONDecodeError:
            # Try stripping trailing comma
            if line_str.endswith(","):
                try:
                    records.append(json.loads(line_str[:-1]))
                    continue
                except json.JSONDecodeError:
                    pass
            is_json_lines = False
            break

    if is_json_lines and records:
        return records, 0

    # Case 3: Concatenated JSON arrays or objects (resilient decoding)
    decoder = json.JSONDecoder()
    pos = 0
    records = []
    malformed_count = 0
    while pos < len(content):
        # Skip whitespace
        while pos < len(content) and content[pos].isspace():
            pos += 1
        if pos >= len(content):
            break
        try:
            obj, next_pos = decoder.raw_decode(content, pos)
            if isinstance(obj, list):
                for item in obj:
                    if isinstance(item, dict):
                        records.append(item)
                    else:
                        malformed_count += 1
            elif isinstance(obj, dict):
                records.append(obj)
            else:
                malformed_count += 1
            pos = next_pos
        except json.JSONDecodeError:
            # Find next likely JSON start character
            next_start = -1
            for p in range(pos + 1, len(content)):
                if content[p] in ('{', '['):
                    next_start = p
                    break
            malformed_count += 1
            if next_start == -1:
                break
            pos = next_start

    return records, malformed_count

def jaccard_similarity(text1: str, text2: str) -> float:
    words1 = set(re.findall(r"\w+", text1.lower()))
    words2 = set(re.findall(r"\w+", text2.lower()))
    if not words1 or not words2:
        return 0.0
    return len(words1.intersection(words2)) / len(words1.union(words2))

def find_near_duplicates_lsh(
    texts: List[str], threshold: float = 0.85, num_hashes: int = 16, num_bands: int = 4
) -> List[Tuple[int, int]]:
    """
    Locality Sensitive Hashing (LSH) with MinHash to find near-duplicate texts
    efficiently in O(N) time.
    """
    if len(texts) < 2:
        return []

    shingle_sets = []
    for text in texts:
        words = re.findall(r"\w+", text.lower())
        if len(words) < 3:
            shingle_sets.append(set(words) if words else set())
        else:
            shingle_sets.append(set(" ".join(words[i:i+3]) for i in range(len(words)-2)))

    # Signatures using python hash() which is stable within the process session
    signatures = []
    for s_set in shingle_sets:
        sig = []
        if not s_set:
            signatures.append([0] * num_hashes)
            continue
        for i in range(num_hashes):
            min_h = 2**63 - 1
            for shingle in s_set:
                h = hash((i, shingle))
                if h < min_h:
                    min_h = h
            sig.append(min_h)
        signatures.append(sig)

    # Banding LSH
    rows_per_band = num_hashes // num_bands
    candidates = set()
    for b in range(num_bands):
        buckets = defaultdict(list)
        for idx, sig in enumerate(signatures):
            band_sig = tuple(sig[b * rows_per_band : (b + 1) * rows_per_band])
            buckets[band_sig].append(idx)
        for bucket_indices in buckets.values():
            # Apply safety limit on degenerate bucket sizes (prevent O(N^2) explosion)
            if 1 < len(bucket_indices) <= 100:
                for i in range(len(bucket_indices)):
                    for j in range(i + 1, len(bucket_indices)):
                        idx1, idx2 = bucket_indices[i], bucket_indices[j]
                        candidates.add((min(idx1, idx2), max(idx1, idx2)))

    near_dups = []
    for idx1, idx2 in candidates:
        s1, s2 = shingle_sets[idx1], shingle_sets[idx2]
        union_len = len(s1.union(s2))
        if union_len == 0:
            continue
        jaccard = len(s1.intersection(s2)) / union_len
        if jaccard >= threshold:
            near_dups.append((idx1, idx2))

    return near_dups

def check_text_quality(text: str, field_name: str) -> List[str]:
    """
    Performs comprehensive text quality audits on string values.
    Returns a list of warning messages.
    """
    warnings = []
    if not text:
        warnings.append(f"Field '{field_name}' is empty")
        return warnings

    if not text.strip():
        warnings.append(f"Field '{field_name}' contains only whitespace")
        return warnings

    # Extremely short sample detection
    stripped_len = len(text.strip())
    if stripped_len < 3:
        warnings.append(f"Field '{field_name}' is extremely short ({stripped_len} chars)")

    # Extremely long sample detection
    if stripped_len > 100000:
        warnings.append(f"Field '{field_name}' is extremely long ({stripped_len} chars)")

    # Excessive character repetition
    re_rep_char = re.search(r"([a-zA-Z0-9])\1{9,}", text)
    if re_rep_char:
        warnings.append(f"Field '{field_name}' has excessive character repetition of '{re_rep_char.group(1)}'")

    # Excessive word repetition
    re_rep_word = re.search(r"\b(\w+)(?:\s+\1){4,}\b", text, re.IGNORECASE)
    if re_rep_word:
        warnings.append(f"Field '{field_name}' has excessive word repetition of '{re_rep_word.group(1)}'")

    # Corrupted Unicode / Mojibake detection
    if "\uFFFD" in text:
        warnings.append(f"Field '{field_name}' contains Unicode replacement character \\uFFFD")

    # Invalid control characters (excluding common formatting whitespaces)
    ctrl_chars = [c for c in text if ord(c) < 32 and c not in "\n\r\t"]
    if ctrl_chars:
        warnings.append(f"Field '{field_name}' contains {len(ctrl_chars)} control characters (e.g. ASCII {ord(ctrl_chars[0])})")

    # Double-escaped characters (e.g. \\n, \\t, \\" or raw hex \\x89)
    if "\\x" in text or "\\u0" in text:
        warnings.append(f"Field '{field_name}' contains raw escape strings (potential serialization residue)")

    return warnings

def validate_schema(record: Dict[str, Any], dataset_name: str, config: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    """
    Validates record keys and types according to the dataset expectations.
    """
    primary = config["primary_schema"]
    fallback = config.get("fallback_schema", [])

    # Check primary schema
    has_primary = all(k in record for k in primary)
    has_fallback = all(k in record for k in fallback) if fallback else False

    used_schema = primary if has_primary else (fallback if has_fallback else None)

    if not used_schema:
        schema_desc = f"Primary: {primary}" + (f" or Fallback: {fallback}" if fallback else "")
        return False, f"Missing required fields. Expected {schema_desc}. Got keys: {list(record.keys())}"

    # Verify types and nulls
    for field in used_schema:
        val = record[field]
        if val is None:
            return False, f"Field '{field}' is null"

        # Resume Review nested checks
        if dataset_name == "resume_review_synthetic_v1.jsonl" and field == "review":
            if not isinstance(val, dict):
                return False, f"Field 'review' must be a dictionary. Got {type(val).__name__}"
            # Required subkeys
            required_sub = ["ats_score", "strengths", "weaknesses", "suggestions", "verdict"]
            for sub in required_sub:
                if sub not in val:
                    return False, f"Field 'review' is missing subkey '{sub}'"
                if sub == "ats_score" and not isinstance(val[sub], (int, float)):
                    return False, f"Subkey 'review.ats_score' must be numeric. Got {type(val[sub]).__name__}"
                if sub in ["strengths", "weaknesses", "suggestions"] and not isinstance(val[sub], list):
                    return False, f"Subkey 'review.{sub}' must be a list. Got {type(val[sub]).__name__}"
                if sub == "verdict" and not isinstance(val[sub], str):
                    return False, f"Subkey 'review.verdict' must be a string. Got {type(val[sub]).__name__}"
        else:
            # Regular fields should be string or numeric
            if not isinstance(val, (str, int, float)):
                return False, f"Field '{field}' must be a string or numeric value. Got {type(val).__name__}"

    return True, None

def clean_synthetic_dataset(file_name: str, config: Dict[str, Any]) -> Dict[str, int]:
    """
    Performs cleanup on synthetic datasets:
    - Removes exact duplicates
    - Removes near-duplicates (Jaccard similarity of resume_text > 0.85)
    - Removes repeated outputs (summaries or reviews)
    - Removes malformed JSON / corrupted records
    Updates the file in-place with clean records and returns statistics.
    """
    file_path = Path(config["path"])
    logger.info(f"Cleaning Synthetic Dataset: {config['name']} ({file_name})...")

    # Load resiliently
    raw_records, malformed_count = parse_flexible_json_resilient(file_path)
    total_loaded = len(raw_records) + malformed_count
    
    clean_records = []
    seen_canonical = set()
    accepted_resume_texts = []
    accepted_outputs = []

    stats = {
        "original_loaded": total_loaded,
        "malformed_json": malformed_count,
        "corrupted_records": 0,
        "exact_duplicates": 0,
        "near_duplicates": 0,
        "repeated_outputs": 0,
        "final_cleaned": 0
    }

    primary_keys = config["primary_schema"]
    output_key = "summary" if "summary" in primary_keys else "review"

    for idx, rec in enumerate(raw_records):
        # 1. Schema & Corruption Check
        is_valid, err = validate_schema(rec, file_name, config)
        if not is_valid:
            stats["corrupted_records"] += 1
            continue

        # Check for corrupted text quality (empty fields, unicode replacement characters, etc.)
        is_corrupted = False
        for k in primary_keys:
            val = rec[k]
            val_str = json.dumps(val) if isinstance(val, (dict, list)) else str(val)
            # Check for corrupted unicode or empty fields
            if not val_str.strip() or "\uFFFD" in val_str:
                is_corrupted = True
                break
        if is_corrupted:
            stats["corrupted_records"] += 1
            continue

        # 2. Exact Duplicates
        rec_canonical = json.dumps(rec, sort_keys=True)
        if rec_canonical in seen_canonical:
            stats["exact_duplicates"] += 1
            continue

        # 3. Near-Duplicates (Jaccard similarity of resume_text > 0.85)
        resume_text = rec["resume_text"]
        is_near_dup = False
        for prev_text in accepted_resume_texts:
            if jaccard_similarity(resume_text, prev_text) > 0.85:
                is_near_dup = True
                break
        if is_near_dup:
            stats["near_duplicates"] += 1
            continue

        # 4. Repeated Outputs (summaries or reviews)
        output_val = rec[output_key]
        output_str = json.dumps(output_val, sort_keys=True) if isinstance(output_val, dict) else str(output_val)
        is_repeated_output = False
        for prev_out in accepted_outputs:
            if jaccard_similarity(output_str, prev_out) > 0.85:
                is_repeated_output = True
                break
        if is_repeated_output:
            stats["repeated_outputs"] += 1
            continue

        # Accept record
        clean_records.append(rec)
        seen_canonical.add(rec_canonical)
        accepted_resume_texts.append(resume_text)
        accepted_outputs.append(output_str)

    stats["final_cleaned"] = len(clean_records)
    
    # Write back cleaned records as a standard JSON array (since these synthetic files are JSON arrays)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(clean_records, f, indent=2, ensure_ascii=False)
        
    logger.info(f"Cleaned {file_name}: {stats}")
    return stats

def main():
    logger.info("Starting Final Dataset Validator V2...")
    t_start = time.time()

    # 1. Clean Synthetic Datasets first
    summary_stats = clean_synthetic_dataset("resume_summary_synthetic.jsonl", DATASETS_CONFIG["resume_summary_synthetic.jsonl"])
    review_stats = clean_synthetic_dataset("resume_review_synthetic_v1.jsonl", DATASETS_CONFIG["resume_review_synthetic_v1.jsonl"])

    # Load tokenizer
    logger.info(f"Loading Llama 3.2 Tokenizer ({MODEL_NAME})...")
    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=True)
    except Exception as e:
        logger.warning(f"Failed to load gated model '{MODEL_NAME}': {e}. Loading fallback '{FALLBACK_MODEL_NAME}'...")
        tokenizer = AutoTokenizer.from_pretrained(FALLBACK_MODEL_NAME, use_fast=True)

    validation_results = {}
    critical_failure_found = False

    for file_name, config in DATASETS_CONFIG.items():
        file_path = Path(config["path"])
        logger.info(f"--------------------------------------------------")
        logger.info(f"Validating Dataset: {config['name']} ({file_name})")

        if not file_path.exists():
            logger.error(f"CRITICAL ERROR: File does not exist at {file_path}")
            validation_results[file_name] = {
                "name": config["name"],
                "path": str(file_path),
                "error": "File not found",
                "status": "FAIL",
            }
            critical_failure_found = True
            continue

        file_size_bytes = file_path.stat().st_size
        if file_size_bytes == 0:
            logger.error(f"CRITICAL ERROR: File is empty (0 bytes) at {file_path}")
            validation_results[file_name] = {
                "name": config["name"],
                "path": str(file_path),
                "error": "File is empty",
                "status": "FAIL",
            }
            critical_failure_found = True
            continue

        # Load clean records
        records, malformed_count = parse_flexible_json_resilient(file_path)
        logger.info(f"Loaded {len(records)} records for validation.")

        # Initialize counters
        exact_duplicates = 0
        near_duplicates = 0
        invalid_rows = 0
        quality_warnings_count = 0
        warning_categories = defaultdict(int)
        seen_canonical = set()
        invalid_messages = []
        texts_to_check_near_dups = []
        token_combined_texts = []
        token_input_texts = []
        token_output_texts = []

        # Row-by-Row Checks
        for idx, rec in enumerate(records):
            # 1. Schema Check
            is_valid, err_msg = validate_schema(rec, file_name, config)
            if not is_valid:
                invalid_rows += 1
                if len(invalid_messages) < 5:
                    invalid_messages.append(f"Row {idx}: {err_msg}")
                continue

            # Identify schema used
            primary_keys = config["primary_schema"]
            has_primary = all(k in rec for k in primary_keys)
            keys_used = primary_keys if has_primary else config.get("fallback_schema", [])

            # Canonical representation for exact duplicate checking
            rec_canonical = json.dumps(rec, sort_keys=True)
            if rec_canonical in seen_canonical:
                exact_duplicates += 1
            else:
                seen_canonical.add(rec_canonical)

            # Determine main text values
            combined_parts = []
            main_input = ""
            main_output = ""

            for field in keys_used:
                val = rec[field]
                val_str = json.dumps(val) if isinstance(val, (dict, list)) else str(val)
                combined_parts.append(val_str)

                # Map to input/output/instruction representation for token/quality stats
                if field in ["input", "resume_text"]:
                    main_input = val_str
                elif field in ["output", "summary", "review", "label"]:
                    main_output = val_str

            combined_str = " ".join(combined_parts)
            texts_to_check_near_dups.append(combined_str)
            token_combined_texts.append(combined_str)
            token_input_texts.append(main_input)
            token_output_texts.append(main_output)

            # 2. Quality Audit
            row_warnings = []
            for field in keys_used:
                val = rec[field]
                # Recursively extract strings and check quality
                def check_recursive(obj: Any, name: str):
                    if isinstance(obj, str):
                        row_warnings.extend(check_text_quality(obj, name))
                    elif isinstance(obj, dict):
                        for k, v in obj.items():
                            check_recursive(v, f"{name}.{k}")
                    elif isinstance(obj, list):
                        for j, v in enumerate(obj):
                            check_recursive(v, f"{name}[{j}]")
                check_recursive(val, field)

            if row_warnings:
                quality_warnings_count += len(row_warnings)
                for w in row_warnings:
                    if "empty" in w.lower() or "whitespace" in w.lower():
                        warning_categories["empty_or_whitespace"] += 1
                    elif "repetition" in w.lower() or "repeated" in w.lower():
                        warning_categories["excessive_repetition"] += 1
                    elif "unicode" in w.lower() or "control" in w.lower() or "escape" in w.lower():
                        warning_categories["corrupted_unicode"] += 1
                    elif "extremely short" in w.lower():
                        warning_categories["extremely_short"] += 1
                    elif "extremely long" in w.lower():
                        warning_categories["extremely_long"] += 1
                    else:
                        warning_categories["other"] += 1

        # Check Near Duplicates (skip resume_sections_instruction.jsonl)
        if file_name != "resume_sections_instruction.jsonl" and len(texts_to_check_near_dups) > 1:
            logger.info("Computing near duplicates...")
            near_dup_pairs = find_near_duplicates_lsh(texts_to_check_near_dups, threshold=0.85)
            near_duplicates = len(near_dup_pairs)
            logger.info(f"Found {near_duplicates} near duplicate pairs.")
        else:
            near_duplicates = 0

        # Token count stats
        logger.info("Computing token statistics...")
        t_tok_start = time.time()
        
        combined_encodings = tokenizer(token_combined_texts, add_special_tokens=False)
        combined_counts = [len(ids) for ids in combined_encodings["input_ids"]]
        
        filtered_inputs = [t for t in token_input_texts if t]
        if filtered_inputs:
            input_encodings = tokenizer(filtered_inputs, add_special_tokens=False)
            input_counts = [len(ids) for ids in input_encodings["input_ids"]]
        else:
            input_counts = []
        
        filtered_outputs = [t for t in token_output_texts if t]
        if filtered_outputs:
            output_encodings = tokenizer(filtered_outputs, add_special_tokens=False)
            output_counts = [len(ids) for ids in output_encodings["input_ids"]]
        else:
            output_counts = []

        logger.info(f"Tokenized in {time.time() - t_tok_start:.2f} seconds.")

        def calc_stats_dict(counts: List[int]) -> Dict[str, Any]:
            if not counts:
                return {"min": 0, "max": 0, "mean": 0, "median": 0, "p95": 0, "p99": 0}
            arr = np.array(counts)
            return {
                "min": int(arr.min()),
                "max": int(arr.max()),
                "mean": float(arr.mean()),
                "median": float(np.median(arr)),
                "p95": float(np.percentile(arr, 95)),
                "p99": float(np.percentile(arr, 99)),
            }

        stats_combined = calc_stats_dict(combined_counts)
        stats_input = calc_stats_dict(input_counts)
        stats_output = calc_stats_dict(output_counts)

        # Fail Conditions
        status = "PASS"
        error_msg = ""
        if invalid_rows > 0:
            status = "FAIL"
            error_msg = f"{invalid_rows} rows failed schema/type validation"
            critical_failure_found = True
            logger.error(f"CRITICAL ERROR: {error_msg}")

        empty_fields_count = warning_categories["empty_or_whitespace"]
        if empty_fields_count > 0:
            status = "FAIL"
            error_msg = f"Dataset contains {empty_fields_count} empty/whitespace values in required fields"
            critical_failure_found = True
            logger.error(f"CRITICAL ERROR: {error_msg}")

        corrupted_unicode_count = warning_categories["corrupted_unicode"]
        if corrupted_unicode_count > 0:
            status = "FAIL"
            error_msg = f"Dataset contains {corrupted_unicode_count} corrupted unicode / control characters / serialization residue"
            critical_failure_found = True
            logger.error(f"CRITICAL ERROR: {error_msg}")

        validation_results[file_name] = {
            "name": config["name"],
            "path": str(file_path),
            "row_count": len(records),
            "exact_duplicates": exact_duplicates,
            "near_duplicates": near_duplicates,
            "invalid_rows": invalid_rows,
            "quality_warnings_count": quality_warnings_count,
            "warning_categories": dict(warning_categories),
            "stats_combined": stats_combined,
            "stats_input": stats_input,
            "stats_output": stats_output,
            "status": status,
            "error_msg": error_msg,
        }

    # Generate Validation Report
    logger.info("Generating Final Validation Report V2...")
    report_md = f"""# Final Dataset Validation Report V2

Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}
Tokenizer Model: `{MODEL_NAME}`

This report validates the integrity, quality, schema format, and token distributions of all fine-tuning and instruction datasets prepared for the Argus AI Resume Adapter, following the synthetic dataset expansion and sanitization pass.

---

## 🧹 Synthetic Cleanup Statistics

| Synthetic Dataset | Original Loaded | Malformed JSON | Corrupted Records | Exact Duplicates | Near Duplicates | Repeated Outputs | Final Cleaned |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Resume Summary** | {summary_stats['original_loaded']:,} | {summary_stats['malformed_json']:,} | {summary_stats['corrupted_records']:,} | {summary_stats['exact_duplicates']:,} | {summary_stats['near_duplicates']:,} | {summary_stats['repeated_outputs']:,} | **{summary_stats['final_cleaned']:,}** |
| **Resume Review** | {review_stats['original_loaded']:,} | {review_stats['malformed_json']:,} | {review_stats['corrupted_records']:,} | {review_stats['exact_duplicates']:,} | {review_stats['near_duplicates']:,} | {review_stats['repeated_outputs']:,} | **{review_stats['final_cleaned']:,}** |

---

## 📊 Executive Summary

| Dataset Name | Format | Total Rows | Exact Duplicates | Near Duplicates (Jaccard > 0.85) | Schema Violations (Fail) | Quality Warnings | Validation Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
"""

    for file_name, res in validation_results.items():
        if "error" in res:
            report_md += f"| **{res['name']}** | Unknown | - | - | - | - | - | ❌ **FAIL** ({res['error']}) |\n"
            continue

        fmt = "JSON Array" if file_name in ["resume_summary_synthetic.jsonl", "resume_review_synthetic_v1.jsonl"] else "JSON Lines"
        status_emoji = "✅ **PASS**" if res["status"] == "PASS" else "❌ **FAIL**"
        report_md += (
            f"| **{res['name']}** | {fmt} | {res['row_count']:,} | {res['exact_duplicates']:,} | "
            f"{res['near_duplicates']:,} | {res['invalid_rows']:,} | {res['quality_warnings_count']:,} | {status_emoji} |\n"
        )

    report_md += "\n---\n\n## Token Length Profiles\n\nAll token counts are estimated using the Llama 3.2 tokenizer.\n"

    for file_name, res in validation_results.items():
        if "error" in res:
            continue
        report_md += f"""
### 📊 {res['name']}

| Field Context | Min Tokens | Max Tokens | Mean Tokens | Median Tokens | 95th Percentile | 99th Percentile |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Combined (Record)** | {res['stats_combined']['min']:,} | {res['stats_combined']['max']:,} | {res['stats_combined']['mean']:.1f} | {res['stats_combined']['median']:.1f} | {res['stats_combined']['p95']:.1f} | {res['stats_combined']['p99']:.1f} |
"""
        if res['stats_input']['max'] > 0:
            report_md += f"| **Input (Resume/Prompt)** | {res['stats_input']['min']:,} | {res['stats_input']['max']:,} | {res['stats_input']['mean']:.1f} | {res['stats_input']['median']:.1f} | {res['stats_input']['p95']:.1f} | {res['stats_input']['p99']:.1f} |\n"
        if res['stats_output']['max'] > 0:
            report_md += f"| **Output (Summary/Response)** | {res['stats_output']['min']:,} | {res['stats_output']['max']:,} | {res['stats_output']['mean']:.1f} | {res['stats_output']['median']:.1f} | {res['stats_output']['p95']:.1f} | {res['stats_output']['p99']:.1f} |\n"

    report_md += "\n---\n\n## Quality Auditing Details\n"

    for file_name, res in validation_results.items():
        if "error" in res:
            continue
        cats = res["warning_categories"]
        report_md += f"""
### ⚠️ {res['name']} Quality Details
- **Empty / Whitespace fields:** {cats.get('empty_or_whitespace', 0):,}
- **Excessive Repetition:** {cats.get('excessive_repetition', 0):,}
- **Corrupted Unicode / Mojibake:** {cats.get('corrupted_unicode', 0):,}
- **Extremely Short (<3 chars):** {cats.get('extremely_short', 0):,}
- **Extremely Long (>100k chars):** {cats.get('extremely_long', 0):,}
"""
        if res["error_msg"]:
            report_md += f"\n> [!CAUTION]\n> **Validation failure reason:** {res['error_msg']}\n"

    report_md += f"""
---

## Technical Details

- **Validation Engine:** `final_dataset_validator.py` (V2)
- **Execution Time:** {time.time() - t_start:.2f} seconds
- **Tokenizer Fallback Used:** {"Yes" if tokenizer.name_or_path == FALLBACK_MODEL_NAME else "No"}
"""

    Path(REPORT_OUTPUT_PATH).parent.mkdir(parents=True, exist_ok=True)
    with open(REPORT_OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(report_md)
    logger.info(f"Saved validation report to {REPORT_OUTPUT_PATH}")

    if critical_failure_found:
        logger.error("Validation FAILED due to critical corruptions / formatting issues.")
        sys.exit(1)
    else:
        logger.info("Validation completed successfully with PASS status for all datasets.")
        sys.exit(0)

if __name__ == "__main__":
    main()
