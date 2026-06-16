import json
import os
import sys
import time
import logging
from pathlib import Path
from typing import List, Dict, Any, Tuple

import numpy as np
from transformers import AutoTokenizer

# Config
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger("DatasetBalancerV2")

MODEL_NAME = "meta-llama/Llama-3.2-1B-Instruct"
FALLBACK_MODEL_NAME = "unsloth/Llama-3.2-1B-Instruct"

DATASETS_CONFIG = {
    "resume_sections_instruction.jsonl": {
        "path": "argus/resume/datasets/processed/resume_sections_instruction.jsonl",
        "name": "Resume Sections Instruction",
        "keys": ["instruction", "input", "output"],
        "input_keys": ["instruction", "input"],
        "output_keys": ["output"],
        "sampling_strategy": "Downsample (Random Uniform)",
        "target_rows": 10000
    },
    "resume_job_fit_training_ready.jsonl": {
        "path": "argus/resume/datasets/processed/resume_job_fit_training_ready.jsonl",
        "name": "Resume Job Fit",
        "keys": ["resume_text", "job_description_text", "label"],
        "input_keys": ["resume_text", "job_description_text"],
        "output_keys": ["label"],
        "sampling_strategy": "Downsample (Balanced Labels)",
        "target_rows": 3200
    },
    "resume_summary_synthetic.jsonl": {
        "path": "argus/resume/datasets/processed/resume_summary_synthetic.jsonl",
        "name": "Resume Summary Synthetic",
        "keys": ["resume_text", "summary"],
        "input_keys": ["resume_text"],
        "output_keys": ["summary"],
        "sampling_strategy": "Keep 100% (Full Preservation)",
        "target_rows": None
    },
    "resume_review_synthetic_v1.jsonl": {
        "path": "argus/resume/datasets/processed/resume_review_synthetic_v1.jsonl",
        "name": "Resume Review Synthetic",
        "keys": ["resume_text", "review"],
        "input_keys": ["resume_text"],
        "output_keys": ["review"],
        "sampling_strategy": "Keep 100% (Full Preservation)",
        "target_rows": None
    }
}

REPORT_OUTPUT_PATH = "argus/resume/evaluation/dataset_balance_report_v2.md"

def parse_flexible_json(file_path: Path) -> List[Dict[str, Any]]:
    """
    Parses a file that could be standard JSON Lines, a standard JSON array, 
    or concatenated JSON arrays/objects.
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
            return data
        return [data]
    except json.JSONDecodeError:
        pass

    # Case 2: Line-by-line JSON lines
    records = []
    lines = content.splitlines()
    is_json_lines = True
    for line in lines:
        line_str = line.strip()
        if not line_str:
            continue
        try:
            records.append(json.loads(line_str))
        except json.JSONDecodeError:
            is_json_lines = False
            break

    if is_json_lines and records:
        return records

    # Case 3: Concatenated JSON arrays or objects
    decoder = json.JSONDecoder()
    pos = 0
    records = []
    while pos < len(content):
        while pos < len(content) and content[pos].isspace():
            pos += 1
        if pos >= len(content):
            break
        try:
            obj, next_pos = decoder.raw_decode(content, pos)
            if isinstance(obj, list):
                records.extend(obj)
            else:
                records.append(obj)
            pos = next_pos
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON in {file_path.name} at position {pos}: {e}")

    return records

def get_field_string(val: Any) -> str:
    if val is None:
        return ""
    if isinstance(val, (dict, list)):
        return json.dumps(val, ensure_ascii=False)
    return str(val)

def calc_stats_dict(counts: List[int]) -> Dict[str, Any]:
    if not counts:
        return {"min": 0, "max": 0, "mean": 0.0, "median": 0.0, "p95": 0.0, "p99": 0.0}
    arr = np.array(counts)
    return {
        "min": int(arr.min()),
        "max": int(arr.max()),
        "mean": float(arr.mean()),
        "median": float(np.median(arr)),
        "p95": float(np.percentile(arr, 95)),
        "p99": float(np.percentile(arr, 99)),
    }

def main():
    logger.info("Initializing Dataset Balance Analyzer V2...")
    
    # Load tokenizer
    logger.info(f"Loading Llama 3.2 Tokenizer ({MODEL_NAME})...")
    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=True)
    except Exception as e:
        logger.warning(f"Failed to load gated model '{MODEL_NAME}': {e}. Loading fallback '{FALLBACK_MODEL_NAME}'...")
        tokenizer = AutoTokenizer.from_pretrained(FALLBACK_MODEL_NAME, use_fast=True)

    dataset_stats = {}
    total_rows_all = 0
    total_tokens_all = 0

    for file_name, config in DATASETS_CONFIG.items():
        file_path = Path(config["path"])
        logger.info(f"Analyzing {config['name']} ({file_name})...")

        if not file_path.exists():
            logger.error(f"File not found: {file_path}")
            continue

        records = parse_flexible_json(file_path)
        row_count = len(records)
        total_rows_all += row_count

        combined_texts = []
        input_texts = []
        output_texts = []

        for rec in records:
            # Combined representation
            combined_parts = []
            for k in config["keys"]:
                if k in rec:
                    combined_parts.append(get_field_string(rec[k]))
            combined_texts.append(" ".join(combined_parts))

            # Input representation
            input_parts = []
            for k in config["input_keys"]:
                if k in rec:
                    input_parts.append(get_field_string(rec[k]))
            input_texts.append(" ".join(input_parts))

            # Output representation
            output_parts = []
            for k in config["output_keys"]:
                if k in rec:
                    output_parts.append(get_field_string(rec[k]))
            output_texts.append(" ".join(output_parts))

        # Tokenize in batch
        logger.info(f"Tokenizing {row_count} records for {config['name']}...")
        t_start = time.time()
        
        combined_enc = tokenizer(combined_texts, add_special_tokens=False)
        combined_counts = [len(ids) for ids in combined_enc["input_ids"]]
        
        input_enc = tokenizer(input_texts, add_special_tokens=False)
        input_counts = [len(ids) for ids in input_enc["input_ids"]]

        output_enc = tokenizer(output_texts, add_special_tokens=False)
        output_counts = [len(ids) for ids in output_enc["input_ids"]]

        tok_duration = time.time() - t_start
        logger.info(f"Tokenization completed in {tok_duration:.2f}s.")

        sum_combined = sum(combined_counts)
        sum_input = sum(input_counts)
        sum_output = sum(output_counts)
        total_tokens_all += sum_combined

        stats_combined = calc_stats_dict(combined_counts)
        stats_input = calc_stats_dict(input_counts)
        stats_output = calc_stats_dict(output_counts)

        dataset_stats[file_name] = {
            "name": config["name"],
            "row_count": row_count,
            "total_tokens_combined": sum_combined,
            "total_tokens_input": sum_input,
            "total_tokens_output": sum_output,
            "stats_combined": stats_combined,
            "stats_input": stats_input,
            "stats_output": stats_output,
            "sampling_strategy": config["sampling_strategy"],
            "target_rows": config["target_rows"]
        }

    # Generate Report Content
    logger.info("Generating dataset balance report V2...")
    report_md = f"""# Dataset Balance & Training Risk Report V2

Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}
Tokenizer Model: `{tokenizer.name_or_path}`

This report analyzes the distribution of row counts, token volume contributions, sequence lengths, and associated training risks across the four prepared datasets for the Argus AI Resume Adapter fine-tuning.

---

## 📊 Dataset Counts

The following table summarizes the raw sample sizes (row counts) for each of the target training datasets:

| Dataset Name | Filename | Row Count | Percentage Contribution |
| :--- | :--- | :--- | :--- |
"""

    for file_name, stats in dataset_stats.items():
        row_pct = (stats["row_count"] / total_rows_all) * 100 if total_rows_all > 0 else 0.0
        report_md += f"| **{stats['name']}** | `{file_name}` | {stats['row_count']:,} | {row_pct:.2f}% |\n"

    report_md += f"| **Total Combined** | - | **{total_rows_all:,}** | **100.00%** |\n"

    report_md += """
---

## 🪙 Token Contribution

Analyzing datasets purely by row count can be misleading. Below is the breakdown of actual token contributions, showing that sequence lengths dictate the real volume of information presented to the model during training.

| Dataset Name | Filename | Combined Tokens | Input (Prompt) Tokens | Output (Response) Tokens | Token Contribution % | Mean Record Tokens | Min/Max Record Tokens |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
"""

    for file_name, stats in dataset_stats.items():
        tok_pct = (stats["total_tokens_combined"] / total_tokens_all) * 100 if total_tokens_all > 0 else 0.0
        report_md += (
            f"| **{stats['name']}** | `{file_name}` | {stats['total_tokens_combined']:,} | {stats['total_tokens_input']:,} | "
            f"{stats['total_tokens_output']:,} | {tok_pct:.2f}% | {stats['stats_combined']['mean']:.1f} | "
            f"{stats['stats_combined']['min']:,} / {stats['stats_combined']['max']:,} |\n"
        )

    report_md += f"| **Total Combined** | - | **{total_tokens_all:,}** | **-** | **-** | **100.00%** | **-** | **-** |\n"

    # Print detailed token profiles section
    report_md += """
---

## 📈 Detailed Token Profiles

A detailed profile of token sizes for each dataset, splitting combined, input, and output token distributions.

"""
    for file_name, stats in dataset_stats.items():
        report_md += f"""### 📊 {stats['name']}

| Context | Min | Max | Mean | Median | P95 | P99 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Combined** | {stats['stats_combined']['min']:,} | {stats['stats_combined']['max']:,} | {stats['stats_combined']['mean']:.1f} | {stats['stats_combined']['median']:.1f} | {stats['stats_combined']['p95']:.1f} | {stats['stats_combined']['p99']:.1f} |
| **Input** | {stats['stats_input']['min']:,} | {stats['stats_input']['max']:,} | {stats['stats_input']['mean']:.1f} | {stats['stats_input']['median']:.1f} | {stats['stats_input']['p95']:.1f} | {stats['stats_input']['p99']:.1f} |
| **Output** | {stats['stats_output']['min']:,} | {stats['stats_output']['max']:,} | {stats['stats_output']['mean']:.1f} | {stats['stats_output']['median']:.1f} | {stats['stats_output']['p95']:.1f} | {stats['stats_output']['p99']:.1f} |

"""

    # Training Risk Analysis Calculations
    sections_row_pct = (dataset_stats["resume_sections_instruction.jsonl"]["row_count"] / total_rows_all) * 100
    job_fit_tok_pct = (dataset_stats["resume_job_fit_training_ready.jsonl"]["total_tokens_combined"] / total_tokens_all) * 100
    summary_row_pct = (dataset_stats["resume_summary_synthetic.jsonl"]["row_count"] / total_rows_all) * 100
    review_row_pct = (dataset_stats["resume_review_synthetic_v1.jsonl"]["row_count"] / total_rows_all) * 100

    report_md += f"""
---

## ⚠️ Training Risk Analysis

An analysis of row and token distributions reveals significant structural skew in the combined training dataset:

### 1. Dominant Datasets
- **By Row Count:** **Resume Sections Instruction** is heavily dominant, representing **{sections_row_pct:.2f}%** of all rows in the raw mixture. If trained directly, the gradient updates will be overwhelmingly dominated by section classification records, potentially leading to overfitting on prefix matching and layout identification.
- **By Token Volume:** **Resume Job Fit** is overwhelmingly dominant, representing **{job_fit_tok_pct:.2f}%** of the total token count. Because job descriptions and full resumes are highly detailed, each row contains thousands of tokens. Consequently, the attention maps and loss gradients will be heavily skewed toward matching resumes with job descriptions, making the other tasks secondary.

### 2. Underrepresented Datasets
- **Resume Summary Synthetic** (representing **{summary_row_pct:.2f}%** of rows) and **Resume Review Synthetic** (representing **{review_row_pct:.2f}%** of rows) are underrepresented in terms of volume.
- In a joint fine-tuning regime, a contribution of less than 1-2% can cause the model to treat these tasks as noise, leading to **Catastrophic Forgetting** or failure to master summary synthesis and qualitative resume feedback formatting.

### 3. Training Skew Risks
- **Gradient Domain Bias:** During training backpropagation, the loss computed on long Job Fit sequences will dwarf the signal from short classification and summary tasks, creating a model that evaluates job fit well but performs poorly on structured text generation.
- **Task Neglect:** Without balancing, the adapter will fail to learn the instruction formatting for summarizing or reviewing resumes because the batch weights do not provide enough signal frequency.

---

## 🎯 Recommended Downsampling & Re-balancing (Adapter V1)

To build a robust and functional **Adapter V1**, we recommend a balanced data mixture strategy. This involves downsampling the dominant tasks to prevent overfitting/gradient takeover while fully preserving the high-quality synthetic datasets.

### Target Dataset Mixture for SFT Trainer

"""

    # Dynamically compute re-balanced counts and expected mix percentages
    mix_data = []
    total_rec_rows = 0
    for file_name, stats in dataset_stats.items():
        orig_rows = stats["row_count"]
        target = stats["target_rows"]
        rec_rows = min(orig_rows, target) if target is not None else orig_rows
        total_rec_rows += rec_rows
        mix_data.append({
            "file_name": file_name,
            "name": stats["name"],
            "orig_rows": orig_rows,
            "rec_rows": rec_rows,
            "strategy": stats["sampling_strategy"],
            "mean_tokens": stats["stats_combined"]["mean"]
        })

    # Compute expected tokens in mixture
    total_mix_expected_tokens = 0
    for md in mix_data:
        md["expected_tokens"] = md["rec_rows"] * md["mean_tokens"]
        total_mix_expected_tokens += md["expected_tokens"]

    report_md += """| Dataset Name | Original Rows | Recommended Rows | Sampling Strategy | Recommended Mix % (Rows) | Expected Mix % (Tokens) |
| :--- | :---: | :---: | :--- | :---: | :---: |
"""
    for md in mix_data:
        mix_pct_rows = (md["rec_rows"] / total_rec_rows) * 100 if total_rec_rows > 0 else 0.0
        mix_pct_tokens = (md["expected_tokens"] / total_mix_expected_tokens) * 100 if total_mix_expected_tokens > 0 else 0.0
        report_md += (
            f"| **{md['name']}** | {md['orig_rows']:,} | {md['rec_rows']:,} | {md['strategy']} | "
            f"{mix_pct_rows:.2f}% | {mix_pct_tokens:.2f}% |\n"
        )

    report_md += f"| **Total Mixture** | **{total_rows_all:,}** | **{total_rec_rows:,}** | **-** | **100.00%** | **100.00%** |\n\n"

    report_md += """### Implementation Guidelines for LoRA/SFT
1. **Sampling Weights:** In the Hugging Face `SFTTrainer` or training script, apply custom sample blending or dataset wrapping to draw samples according to the recommended row mix counts.
2. **Packing Strategy:** Use packing (concatenating multiple short sequences like Resume Sections up to `max_seq_length = 4096`) to maximize VRAM utilization and training efficiency.
3. **Task-Specific Loss Scaling:** If possible, scale the loss weight for Resume Summary and Resume Review by `2.0x` or `3.0x` to amplify their training signals and compensate for their smaller size.
"""

    # Ensure parent directory exists
    Path(REPORT_OUTPUT_PATH).parent.mkdir(parents=True, exist_ok=True)
    with open(REPORT_OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(report_md)
    logger.info(f"Saved dataset balance report to {REPORT_OUTPUT_PATH}")

    # Print Console Summary
    print("=" * 60)
    print("DATASET BALANCE SUMMARY V2 (POST-CLEANUP)")
    print("=" * 60)
    for file_name, stats in dataset_stats.items():
        print(f"Dataset: {stats['name']}")
        print(f"  Filename:   {file_name}")
        print(f"  Clean Rows: {stats['row_count']:,}")
        print(f"  Total Toks: {stats['total_tokens_combined']:,} (Combined mean: {stats['stats_combined']['mean']:.1f})")
    print("-" * 60)
    print("RECOMMENDED BALANCED SAMPLING PLAN (ADAPTER V1):")
    print("-" * 60)
    print(f"{'Dataset Name':<30} | {'Original':<10} | {'Recommended':<12} | {'Mix % (Rows)':<12} | {'Mix % (Tokens)':<14}")
    print("-" * 88)
    for md in mix_data:
        mix_pct_rows = (md["rec_rows"] / total_rec_rows) * 100 if total_rec_rows > 0 else 0.0
        mix_pct_tokens = (md["expected_tokens"] / total_mix_expected_tokens) * 100 if total_mix_expected_tokens > 0 else 0.0
        print(f"{md['name']:<30} | {md['orig_rows']:<10,} | {md['rec_rows']:<12,} | {mix_pct_rows:<12.2f}% | {mix_pct_tokens:<14.2f}%")
    print("-" * 88)
    print(f"{'Total Mixture':<30} | {total_rows_all:<10,} | {total_rec_rows:<12,} | 100.00%       | 100.00%")
    print("=" * 60)

if __name__ == "__main__":
    main()
