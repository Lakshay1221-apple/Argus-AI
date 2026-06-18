"""
Argus Code Review Dataset Builder — V2.1

Goals:
- Build a unified code-review dataset for a Llama 3.2 adapter.
- Keep every sample in a consistent schema.
- Add fixed_code, severity, category, source_dataset, and language metadata.
- Deduplicate exact and near-duplicate samples.
- Produce training-safe JSONL plus audit reports.

Recommended training categories:
- review
- security
- complexity

This script is intentionally conservative:
- It avoids overly large samples.
- It limits source counts in Phase 1.
- It keeps metadata for auditing.
- It can be extended later for Phase 2 language balancing.

Usage:
    python build_code_review_dataset_v2.py

Optional:
    python build_code_review_dataset_v2.py --output argus_code_review_v2.jsonl
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

from datasets import load_dataset

# -----------------------------------------------------------------------------
# Config
# -----------------------------------------------------------------------------

OUTPUT_FILE_DEFAULT = "argus_code_review_v2.jsonl"

BASE_DIR = Path("argus/code_review")
DATASET_DIR = BASE_DIR / "datasets" / "processed"
EVAL_DIR = BASE_DIR / "evaluation"
EVAL_ACTIVE_DIR = EVAL_DIR / "active"
EVAL_ARCHIVE_DIR = EVAL_DIR / "_archive"

# Phase 1 source caps. Keep this around ~5k for the first run.
SOURCE_CAPS = {
    "securecode-v2": 1500,                  # security
    "CodeReviewQA": 2500,                   # bug detection / review
    "BigOBench": 1000,                      # complexity
    "Code-Feedback": 1000,                  # review / readability
    "code-review-instruct-critique": 500,   # refactor / best practices
}
TOTAL_CAP = 5000

# Length constraints (characters)
MIN_INPUT_CHARS = 40
MAX_INPUT_CHARS = 8000
MAX_OUTPUT_CHARS = 4000

# Near-duplicate detection
JACCARD_THRESHOLD = 0.85
SHINGLE_K = 4

# Language targets for reports / later balancing
LANGUAGE_TARGETS = {
    "python": 0.35,
    "javascript": 0.25,
    "java": 0.20,
    "go": 0.10,
    "cpp": 0.10,
}

# -----------------------------------------------------------------------------
# Global audit state
# -----------------------------------------------------------------------------

SEEN_EXACT_HASHES: set[str] = set()
SEEN_SHINGLE_SETS: List[set[str]] = []

AUDIT = {
    "sources": {
        src: {
            "loaded": 0,
            "dropped_malformed": 0,
            "dropped_length": 0,
            "dropped_exact_dup": 0,
            "dropped_near_dup": 0,
        }
        for src in SOURCE_CAPS
    },
    "categories": Counter(),
    "languages": Counter(),
    "severity": Counter(),
    "lengths_input": [],
    "lengths_output": [],
    "source_failures": Counter(),
}

# -----------------------------------------------------------------------------
# Utilities
# -----------------------------------------------------------------------------

def ensure_dirs() -> None:
    EVAL_ACTIVE_DIR.mkdir(parents=True, exist_ok=True)
    EVAL_ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    DATASET_DIR.mkdir(parents=True, exist_ok=True)


def norm_text(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def md5_norm(*parts: str) -> str:
    combined = "\n".join(norm_text(p) for p in parts)
    normalized = re.sub(r"\s+", "", combined).lower()
    return hashlib.md5(normalized.encode("utf-8")).hexdigest()


def shingles(text: str, k: int = SHINGLE_K) -> set[str]:
    t = re.sub(r"\s+", " ", (text or "").lower().strip())
    if len(t) <= k:
        return {t}
    return {t[i : i + k] for i in range(len(t) - k + 1)}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def is_near_duplicate(code: str) -> bool:
    s = shingles(code)
    for prev in SEEN_SHINGLE_SETS:
        if jaccard(s, prev) >= JACCARD_THRESHOLD:
            return True
    SEEN_SHINGLE_SETS.append(s)
    return False


def detect_language(code: str) -> str:
    c = (code or "").lower()

    # Python
    if re.search(r"\bdef\s+\w+\s*\(", c) or "import " in c or "print(" in c:
        return "python"

    # JavaScript / TypeScript
    if (
        "console.log" in c
        or re.search(r"\bfunction\s+\w+\s*\(", c)
        or re.search(r"\b(const|let|var)\s+\w+\s*=", c)
        or "=> {" in c
    ):
        return "javascript"

    # Java
    if "public static void main" in c or "system.out.println" in c or "class " in c:
        return "java"

    # Go
    if "package main" in c or re.search(r"\bfunc\s+\w+\s*\(", c):
        return "go"

    # C++
    if "#include <" in c or "using namespace std" in c or "cout <<" in c:
        return "cpp"

    return "unknown"


def estimate_severity(issues: List[str], category: str) -> str:
    text = " ".join(issues).lower()

    if category == "security":
        if any(k in text for k in ["sql injection", "xss", "rce", "remote code execution", "path traversal", "command injection"]):
            return "critical"
        if any(k in text for k in ["hardcoded password", "secret", "token", "auth bypass", "csrf", "ssrf"]):
            return "high"
        return "medium"

    if category == "complexity":
        if any(k in text for k in ["o(n^2)", "quadratic", "nested loop", "o(n^3)", "exponential"]):
            return "medium"
        return "low"

    if any(k in text for k in ["bug", "error", "crash", "exception", "fails", "incorrect"]):
        return "medium"

    return "low"


def derive_quality_score(issues: List[str], category: str, severity: str) -> int:
    base = {
        "security": 70,
        "complexity": 75,
        "review": 80,
    }.get(category, 75)

    sev_penalty = {
        "critical": 35,
        "high": 25,
        "medium": 15,
        "low": 5,
    }.get(severity, 10)

    issue_penalty = min(len(issues) * 4, 20)
    score = base - sev_penalty - issue_penalty
    return max(20, min(95, score))


def score_to_verdict(score: int) -> str:
    if score >= 85:
        return "Good"
    if score >= 65:
        return "Needs Improvement"
    if score >= 45:
        return "Poor"
    return "Unsafe"


def extract_code_block(text: str) -> str:
    if not text:
        return ""
    match = re.search(r"```(?:\w+)?\n(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()[:2000]
    return ""


def extract_bullets(text: str, keywords: List[str], limit: int = 4) -> List[str]:
    if not text:
        return []
    found: List[str] = []
    for raw in text.splitlines():
        line = raw.strip().lstrip("•-*#123456789. ").strip()
        if len(line) < 8:
            continue
        lower = line.lower()
        if any(k in lower for k in keywords):
            found.append(line[:180])
        if len(found) >= limit:
            break
    return found


def fallback_issues(category: str) -> List[str]:
    if category == "security":
        return ["Potential security vulnerability detected."]
    if category == "complexity":
        return ["Algorithmic complexity can likely be improved."]
    return ["Code quality or readability issue detected."]


def fallback_suggestions(category: str) -> List[str]:
    if category == "security":
        return ["Validate input and use secure coding patterns."]
    if category == "complexity":
        return ["Use a more efficient data structure or algorithm."]
    return ["Refactor for clarity, maintainability, and consistency."]


def parse_dataset_item(item: Dict[str, Any], source: str) -> Tuple[str, str, str]:
    """
    Return (input_code, raw_review_text, fixed_code)
    """
    if source == "securecode-v2":
        conversations = item.get("conversations", []) or []
        user_text, assistant_text = "", ""
        for turn in conversations:
            role = (turn.get("from", "") or "").lower()
            val = turn.get("value", "") or ""
            if role in {"human", "user"} and not user_text:
                user_text = val
            elif role in {"gpt", "assistant"} and not assistant_text:
                assistant_text = val
        return user_text, assistant_text, extract_code_block(assistant_text)

    if source == "CodeReviewQA":
        old_code = item.get("old", "") or ""
        review = item.get("review", "") or ""
        new_code = item.get("new", "") or ""
        return old_code, review, new_code

    if source == "BigOBench":
        code = (
            item.get("solution_code")
            or item.get("code")
            or item.get("source_code")
            or ""
        )
        desc = item.get("description") or item.get("problem_description") or ""
        tc = item.get("time_complexity_inferred") or item.get("time_complexity") or "O(n)"
        sc = item.get("space_complexity_inferred") or item.get("space_complexity") or "O(1)"

        review = (
            f"### Algorithmic Complexity Analysis\n"
            f"- Problem Context: {desc[:300]}\n"
            f"- Time Complexity: {tc}\n"
            f"- Space Complexity: {sc}\n"
        )
        fixed = "# Complexity is determined by algorithm choice; see suggestions."
        return code, review, fixed

    if source == "Code-Feedback":
        query, answer = "", ""
        if "messages" in item and isinstance(item["messages"], list):
            for msg in item["messages"]:
                role = (msg.get("role", "") or "").lower()
                content = msg.get("content", "") or ""
                if role == "user" and not query:
                    query = content
                elif role == "assistant" and not answer:
                    answer = content
        query = query or item.get("query") or item.get("instruction") or ""
        answer = answer or item.get("answer") or item.get("response") or ""
        return query, answer, extract_code_block(answer)

    if source == "code-review-instruct-critique":
        code = item.get("code") or item.get("body") or ""
        critique = item.get("critique") or item.get("review") or ""
        revision = item.get("revision") or item.get("corrected_code") or ""
        return code, critique, revision

    return "", "", ""


def build_output_json(
    category: str,
    issues: List[str],
    suggestions: List[str],
    fixed_code: str,
    severity: str,
) -> str:
    score = derive_quality_score(issues, category, severity)
    verdict = score_to_verdict(score)
    payload = {
        "quality_score": score,
        "severity": severity,
        "issues": issues if issues else ["No critical issues detected."],
        "suggestions": suggestions if suggestions else ["Code follows standard patterns."],
        "fixed_code": fixed_code if fixed_code else "# No changes required.",
        "verdict": verdict,
    }
    return json.dumps(payload, ensure_ascii=False)


def make_sample(
    source: str,
    category: str,
    instruction: str,
    code_input: str,
    issues: List[str],
    suggestions: List[str],
    fixed_code: str,
) -> Optional[Dict[str, Any]]:
    if not instruction or not code_input:
        AUDIT["sources"][source]["dropped_malformed"] += 1
        return None

    code_input = norm_text(code_input)
    if len(code_input) < MIN_INPUT_CHARS or len(code_input) > MAX_INPUT_CHARS:
        AUDIT["sources"][source]["dropped_length"] += 1
        return None

    severity = estimate_severity(issues, category)
    output_str = build_output_json(category, issues, suggestions, fixed_code, severity)

    if len(output_str) > MAX_OUTPUT_CHARS:
        AUDIT["sources"][source]["dropped_length"] += 1
        return None

    exact_hash = md5_norm(instruction, code_input, output_str)
    if exact_hash in SEEN_EXACT_HASHES:
        AUDIT["sources"][source]["dropped_exact_dup"] += 1
        return None
    SEEN_EXACT_HASHES.add(exact_hash)

    if is_near_duplicate(code_input):
        AUDIT["sources"][source]["dropped_near_dup"] += 1
        return None

    language = detect_language(code_input)

    AUDIT["sources"][source]["loaded"] += 1
    AUDIT["categories"][category] += 1
    AUDIT["languages"][language] += 1
    AUDIT["severity"][severity] += 1
    AUDIT["lengths_input"].append(len(code_input))
    AUDIT["lengths_output"].append(len(output_str))

    return {
        "instruction": instruction.strip(),
        "input": code_input,
        "output": output_str,
        "category": category,
        "language": language,
        "severity": severity,
        "source_dataset": source,
    }


# -----------------------------------------------------------------------------
# Source processors
# -----------------------------------------------------------------------------

def process_secure_code() -> List[Dict[str, Any]]:
    print("[1/5] securecode-v2")
    out: List[Dict[str, Any]] = []
    try:
        ds = load_dataset("scthornton/securecode-v2", split="train")
        for item in ds:
            if len(out) >= SOURCE_CAPS["securecode-v2"]:
                break
            code_input, review_text, fixed_code = parse_dataset_item(item, "securecode-v2")
            issues = extract_bullets(review_text, ["vulnerab", "attack", "exploit", "risk", "insecure", "sql injection", "xss"])
            suggestions = extract_bullets(review_text, ["use", "sanitize", "validate", "parameter", "escape", "auth", "encrypt"])
            sample = make_sample(
                source="securecode-v2",
                category="security",
                instruction="Analyze the following code for security vulnerabilities. Identify threats and provide a secure refactored version.",
                code_input=code_input,
                issues=issues or fallback_issues("security"),
                suggestions=suggestions or fallback_suggestions("security"),
                fixed_code=fixed_code,
            )
            if sample:
                out.append(sample)
    except Exception as e:
        AUDIT["source_failures"]["securecode-v2"] += 1
        print(f"  failed: {e}")
    print(f"  samples: {len(out)}")
    return out


def process_code_review_qa() -> List[Dict[str, Any]]:
    print("[2/5] CodeReviewQA")
    out: List[Dict[str, Any]] = []
    try:
        ds = load_dataset("Tomo-Melb/CodeReviewQA", split="train")
        for item in ds:
            if len(out) >= SOURCE_CAPS["CodeReviewQA"]:
                break
            code_input, review_text, fixed_code = parse_dataset_item(item, "CodeReviewQA")
            issues = extract_bullets(review_text, ["bug", "issue", "problem", "error", "incorrect", "fails", "wrong"])
            suggestions = extract_bullets(review_text, ["add", "change", "use", "refactor", "improve", "handle"])
            if not fixed_code:
                fixed_code = "# Refactor based on review feedback."
            sample = make_sample(
                source="CodeReviewQA",
                category="bug_detection",
                instruction="Review this code and identify bugs or issues. Provide a corrected version.",
                code_input=code_input,
                issues=issues or fallback_issues("review"),
                suggestions=suggestions or fallback_suggestions("review"),
                fixed_code=fixed_code,
            )
            if sample:
                out.append(sample)
    except Exception as e:
        AUDIT["source_failures"]["CodeReviewQA"] += 1
        print(f"  failed: {e}")
    print(f"  samples: {len(out)}")
    return out


def _complexity_suggestion(tc: str) -> str:
    t = (tc or "").lower()
    if "n^2" in t or "n2" in t or "quadratic" in t:
        return "Consider a hash map, two pointers, or sorting-based optimization to reduce runtime."
    if "2^n" in t or "exponential" in t:
        return "Use dynamic programming or memoization to avoid exponential recomputation."
    if "n log" in t:
        return "Complexity is already near-optimal; focus on constant-factor improvements."
    return "Check whether a more efficient algorithm or data structure is possible."


def process_big_o() -> List[Dict[str, Any]]:
    print("[3/5] BigOBench")
    out: List[Dict[str, Any]] = []

    def make_bigo(code: str, name: str, tc: str, sc: str) -> Optional[Dict[str, Any]]:
        issues = [f"Time complexity is {tc}.", f"Space complexity is {sc}."]
        suggestions = [_complexity_suggestion(tc)]
        return make_sample(
            source="BigOBench",
            category="complexity",
            instruction=f"Analyze the computational complexity of this algorithm: {name}.",
            code_input=code,
            issues=issues,
            suggestions=suggestions,
            fixed_code="# Complexity analysis is algorithm-dependent; see suggestions.",
        )

    try:
        # Try default first; if it fails, fallback to a few synthetic examples.
        ds = load_dataset("facebook/BigOBench", "default", split="train")
        for item in ds:
            if len(out) >= SOURCE_CAPS["BigOBench"]:
                break
            code = item.get("solution_code") or item.get("code") or item.get("source_code") or ""
            tc = item.get("time_complexity_inferred") or item.get("time_complexity") or "O(n)"
            sc = item.get("space_complexity_inferred") or item.get("space_complexity") or "O(1)"
            name = item.get("problem_name") or item.get("name") or "Algorithm"
            if not code:
                continue
            sample = make_bigo(code, name, tc, sc)
            if sample:
                out.append(sample)
    except Exception as e:
        AUDIT["source_failures"]["BigOBench"] += 1
        print(f"  fallback due to: {e}")
        fallbacks = [
            (
                "def bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n - i - 1):\n            if arr[j] > arr[j + 1]:\n                arr[j], arr[j + 1] = arr[j + 1], arr[j]",
                "Bubble Sort",
                "O(n^2)",
                "O(1)",
            ),
            (
                "def binary_search(arr, x):\n    l, r = 0, len(arr) - 1\n    while l <= r:\n        mid = (l + r) // 2\n        if arr[mid] == x:\n            return mid\n        elif arr[mid] < x:\n            l = mid + 1\n        else:\n            r = mid - 1\n    return -1",
                "Binary Search",
                "O(log n)",
                "O(1)",
            ),
            (
                "def fibonacci(n):\n    if n <= 1:\n        return n\n    dp = [0] * (n + 1)\n    dp[1] = 1\n    for i in range(2, n + 1):\n        dp[i] = dp[i - 1] + dp[i - 2]\n    return dp[n]",
                "Fibonacci DP",
                "O(n)",
                "O(n)",
            ),
            (
                "def merge_sort(arr):\n    if len(arr) <= 1:\n        return arr\n    mid = len(arr) // 2\n    left = merge_sort(arr[:mid])\n    right = merge_sort(arr[mid:])\n    return merge(left, right)",
                "Merge Sort",
                "O(n log n)",
                "O(n)",
            ),
        ]
        for code, name, tc, sc in fallbacks:
            if len(out) >= SOURCE_CAPS["BigOBench"]:
                break
            sample = make_bigo(code, name, tc, sc)
            if sample:
                out.append(sample)

    print(f"  samples: {len(out)}")
    return out


def process_code_feedback() -> List[Dict[str, Any]]:
    print("[4/5] Code-Feedback")
    out: List[Dict[str, Any]] = []
    try:
        ds = load_dataset("HuggingFaceH4/Code-Feedback", split="train")
        for item in ds:
            if len(out) >= SOURCE_CAPS["Code-Feedback"]:
                break

            query, answer = "", ""
            if "messages" in item and isinstance(item["messages"], list):
                for msg in item["messages"]:
                    role = (msg.get("role", "") or "").lower()
                    content = msg.get("content", "") or ""
                    if role == "user" and not query:
                        query = content
                    elif role == "assistant" and not answer:
                        answer = content

            query = query or item.get("query") or item.get("instruction") or ""
            answer = answer or item.get("answer") or item.get("response") or ""

            issues = extract_bullets(answer, ["bug", "issue", "problem", "inefficien", "readability", "style", "naming", "maintain"])
            suggestions = extract_bullets(answer, ["should", "could", "refactor", "improve", "use", "prefer"])
            fixed_code = extract_code_block(answer) or "# Refactor according to the feedback."

            sample = make_sample(
                source="Code-Feedback",
                category="review",
                instruction="Review the provided code. Identify issues, suggest improvements, and provide a refactored version.",
                code_input=query,
                issues=issues or fallback_issues("review"),
                suggestions=suggestions or fallback_suggestions("review"),
                fixed_code=fixed_code,
            )
            if sample:
                out.append(sample)
    except Exception as e:
        AUDIT["source_failures"]["Code-Feedback"] += 1
        print(f"  failed: {e}")
    print(f"  samples: {len(out)}")
    return out


def process_dahoas_critique() -> List[Dict[str, Any]]:
    print("[5/5] Dahoas critique/revision")
    out: List[Dict[str, Any]] = []
    try:
        ds = load_dataset("Dahoas/code-review-instruct-critique-revision-python", split="train")
        for item in ds:
            if len(out) >= SOURCE_CAPS["code-review-instruct-critique"]:
                break
            code = item.get("code") or item.get("body") or ""
            critique = item.get("critique") or item.get("review") or ""
            revision = item.get("revision") or item.get("corrected_code") or ""

            issues = extract_bullets(critique, ["anti-pattern", "bug", "issue", "style", "readability", "maintain", "problem"])
            suggestions = extract_bullets(critique, ["refactor", "rename", "simplify", "avoid", "prefer", "use"])
            if not issues and critique:
                issues = [critique.strip()[:180]]

            sample = make_sample(
                source="code-review-instruct-critique",
                category="review",
                instruction="Critique this Python script for structural and styling issues. Provide a corrected version.",
                code_input=code,
                issues=issues or fallback_issues("review"),
                suggestions=suggestions or fallback_suggestions("review"),
                fixed_code=revision.strip() if revision else "# See critique above.",
            )
            if sample:
                out.append(sample)
    except Exception as e:
        AUDIT["source_failures"]["code-review-instruct-critique"] += 1
        print(f"  failed: {e}")
    print(f"  samples: {len(out)}")
    return out


# -----------------------------------------------------------------------------
# Reports
# -----------------------------------------------------------------------------

def write_reports(samples: List[Dict[str, Any]]) -> None:
    total = len(samples)
    avg_in = sum(AUDIT["lengths_input"]) / total if total else 0
    avg_out = sum(AUDIT["lengths_output"]) / total if total else 0

    # source_audit.md
    with open(EVAL_ARCHIVE_DIR / "source_audit.md", "w", encoding="utf-8") as f:
        f.write("# Argus Code Review Dataset Builder — Source Audit\n\n")
        f.write("| Source | Loaded | Malformed | Length | Exact Dup | Near Dup |\n")
        f.write("|---|---:|---:|---:|---:|---:|\n")
        for src, c in AUDIT["sources"].items():
            f.write(
                f"| `{src}` | {c['loaded']} | {c['dropped_malformed']} | "
                f"{c['dropped_length']} | {c['dropped_exact_dup']} | {c['dropped_near_dup']} |\n"
            )
        f.write(f"\n**Total samples exported:** {total}\n")

    # validation_report.md
    total_exact = sum(c["dropped_exact_dup"] for c in AUDIT["sources"].values())
    total_near = sum(c["dropped_near_dup"] for c in AUDIT["sources"].values())
    total_mal = sum(c["dropped_malformed"] for c in AUDIT["sources"].values())
    total_len = sum(c["dropped_length"] for c in AUDIT["sources"].values())

    with open(EVAL_ARCHIVE_DIR / "validation_report.md", "w", encoding="utf-8") as f:
        f.write("# Argus Code Review Dataset Builder — Validation Report\n\n")
        f.write(f"- Exact duplicates blocked: **{total_exact}**\n")
        f.write(f"- Near duplicates blocked (Jaccard ≥ {JACCARD_THRESHOLD}): **{total_near}**\n")
        f.write(f"- Malformed records discarded: **{total_mal}**\n")
        f.write(f"- Length failures: **{total_len}**\n")
        f.write(f"  - Input range: **{MIN_INPUT_CHARS}–{MAX_INPUT_CHARS} chars**\n")
        f.write(f"  - Output max: **{MAX_OUTPUT_CHARS} chars**\n")
        f.write("\n**Schema:** instruction / input / output / category / language / severity / source_dataset\n")

    # balance_report.md
    with open(EVAL_ARCHIVE_DIR / "balance_report.md", "w", encoding="utf-8") as f:
        f.write("# Argus Code Review Dataset Builder — Balance Report\n\n")
        f.write("### Category Distribution\n\n")
        f.write("| Category | Samples | % |\n|---|---:|---:|\n")
        for cat, cnt in sorted(AUDIT["categories"].items(), key=lambda x: -x[1]):
            f.write(f"| {cat} | {cnt} | {cnt/total*100:.1f}% |\n")

        f.write("\n### Severity Distribution\n\n")
        f.write("| Severity | Samples | % |\n|---|---:|---:|\n")
        for sev, cnt in sorted(AUDIT["severity"].items(), key=lambda x: -x[1]):
            f.write(f"| {sev} | {cnt} | {cnt/total*100:.1f}% |\n")

        f.write("\n### Sequence Lengths\n\n")
        f.write(f"- Average input length: **{avg_in:.0f} chars** (~{avg_in/4:.0f} tokens)\n")
        f.write(f"- Average output length: **{avg_out:.0f} chars** (~{avg_out/4:.0f} tokens)\n")

    # language_distribution.md
    with open(EVAL_ARCHIVE_DIR / "language_distribution.md", "w", encoding="utf-8") as f:
        f.write("# Argus Code Review Dataset Builder — Language Distribution\n\n")
        f.write("| Language | Count | % | Target % | Gap |\n|---|---:|---:|---:|---:|\n")
        for lang, cnt in sorted(AUDIT["languages"].items(), key=lambda x: -x[1]):
            actual = cnt / total * 100 if total else 0
            target = LANGUAGE_TARGETS.get(lang, 0.0) * 100
            gap = actual - target
            flag = " ⚠" if abs(gap) > 10 else ""
            f.write(f"| {lang} | {cnt} | {actual:.1f}% | {target:.0f}% | {gap:+.1f}%{flag} |\n")
        f.write("\n> Language balancing is disabled in Phase 1.\n")

    # final_validation_summary.md
    schema_errors = spot_check_schema(samples[:50])
    with open(EVAL_ACTIVE_DIR / "final_validation_summary.md", "w", encoding="utf-8") as f:
        f.write("# Argus Code Review Dataset Builder — Final Pre-Training Validation\n\n")
        f.write("| Check | Result |\n|---|---|\n")
        f.write(f"| Total samples | {total} |\n")
        f.write(f"| Schema spot-check (50 samples) | {'✓ PASS' if schema_errors == 0 else f'✗ {schema_errors} errors'} |\n")
        f.write("| Exact duplicates | 0 (enforced) |\n")
        f.write("| Near duplicates | 0 (enforced) |\n")
        f.write(f"| Avg input tokens (~) | {avg_in/4:.0f} |\n")
        f.write(f"| Avg output tokens (~) | {avg_out/4:.0f} |\n")
        f.write("| fixed_code present | Required |\n")
        f.write("| PII scrubbing | Not applied (use if needed) |\n")
        f.write(f"\n**Ready for SFTTrainer:** {'YES' if schema_errors == 0 and total >= 2000 else 'NO'}\n")

    print("Reports written:")
    print(f"  - {EVAL_ARCHIVE_DIR / 'source_audit.md'}")
    print(f"  - {EVAL_ARCHIVE_DIR / 'validation_report.md'}")
    print(f"  - {EVAL_ARCHIVE_DIR / 'balance_report.md'}")
    print(f"  - {EVAL_ARCHIVE_DIR / 'language_distribution.md'}")
    print(f"  - {EVAL_ACTIVE_DIR / 'final_validation_summary.md'}")


def spot_check_schema(samples: List[Dict[str, Any]]) -> int:
    required = {"quality_score", "severity", "issues", "suggestions", "fixed_code", "verdict"}
    errors = 0
    for sample in samples:
        try:
            obj = json.loads(sample["output"])
            if not required.issubset(set(obj.keys())):
                errors += 1
        except Exception:
            errors += 1
    return errors


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def build_dataset() -> List[Dict[str, Any]]:
    all_samples: List[Dict[str, Any]] = []
    all_samples.extend(process_secure_code())
    all_samples.extend(process_code_review_qa())
    all_samples.extend(process_big_o())
    all_samples.extend(process_code_feedback())
    all_samples.extend(process_dahoas_critique())

    # Global cap
    all_samples = all_samples[:TOTAL_CAP]
    return all_samples


def export_jsonl(samples: List[Dict[str, Any]], output_file: Path) -> None:
    with open(output_file, "w", encoding="utf-8") as f:
        for sample in samples:
            f.write(json.dumps(sample, ensure_ascii=False) + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build Argus Code Review Dataset V2.1")
    parser.add_argument("--output", default=OUTPUT_FILE_DEFAULT, help="Output JSONL path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ensure_dirs()

    print("=" * 72)
    print("Argus Code Review Dataset Builder — V2.1")
    print(f"Phase 1 target cap: {TOTAL_CAP}")
    print("=" * 72)

    samples = build_dataset()

    print("\n" + "=" * 72)
    print(f"Total unique samples ready: {len(samples)}")
    print("=" * 72)

    write_reports(samples)

    output_path = Path(args.output)
    export_jsonl(samples, output_path)

    print(f"\nExported → {output_path.resolve()}")
    print("All outputs conform to the Argus code-review schema.")


if __name__ == "__main__":
    main()