# =====================================================================
# TOKEN ANALYSIS FOR LORA TRAINING
# =====================================================================

import pandas as pd
import numpy as np

from transformers import AutoTokenizer

# =====================================================================
# CONFIG
# =====================================================================

MODEL_NAME = "meta-llama/Llama-3.2-1B-Instruct"
FALLBACK_MODEL_NAME = "unsloth/Llama-3.2-1B-Instruct"

DATASET_PATH = (
    "argus/resume/datasets/processed/"
    "resume_job_fit_training_ready.jsonl"
)

REPORT_PATH = (
    "argus/resume/evaluation/"
    "token_analysis_report.md"
)

# =====================================================================
# LOAD TOKENIZER
# =====================================================================

print("\nLoading tokenizer...")

try:
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME
    )
except Exception as e:
    print(f"Failed to load gated model '{MODEL_NAME}' ({e}). Falling back to open '{FALLBACK_MODEL_NAME}'...")
    tokenizer = AutoTokenizer.from_pretrained(
        FALLBACK_MODEL_NAME
    )

# =====================================================================
# LOAD DATASET
# =====================================================================

print("Loading dataset...")

df = pd.read_json(
    DATASET_PATH,
    lines=True
)

print(f"Rows Loaded: {len(df)}")

# =====================================================================
# TOKEN COUNT FUNCTION
# =====================================================================

def count_tokens(text: str) -> int:

    return len(
        tokenizer.encode(
            text,
            add_special_tokens=False
        )
    )

# =====================================================================
# TOKENIZE
# =====================================================================

print("\nCalculating token lengths...")

df["resume_tokens"] = df["resume_text"].apply(
    count_tokens
)

df["jd_tokens"] = df["job_description_text"].apply(
    count_tokens
)

df["combined_tokens"] = (
    df["resume_tokens"]
    + df["jd_tokens"]
)

# =====================================================================
# STATS FUNCTION
# =====================================================================

def get_stats(series):

    return {
        "avg": round(series.mean(), 2),
        "median": int(series.median()),
        "p95": int(series.quantile(0.95)),
        "p99": int(series.quantile(0.99)),
        "max": int(series.max()),
        "min": int(series.min())
    }

# =====================================================================
# COMPUTE STATS
# =====================================================================

resume_stats = get_stats(
    df["resume_tokens"]
)

jd_stats = get_stats(
    df["jd_tokens"]
)

combined_stats = get_stats(
    df["combined_tokens"]
)

# =====================================================================
# PRINT RESULTS
# =====================================================================

print("\n========== RESUME ==========")
print(resume_stats)

print("\n========== JOB DESCRIPTION ==========")
print(jd_stats)

print("\n========== COMBINED ==========")
print(combined_stats)

# =====================================================================
# RECOMMEND MAX SEQ LENGTH
# =====================================================================

p95 = combined_stats["p95"]

if p95 <= 1024:
    recommended_seq = 1024

elif p95 <= 2048:
    recommended_seq = 2048

elif p95 <= 4096:
    recommended_seq = 4096

else:
    recommended_seq = 8192

# =====================================================================
# REPORT
# =====================================================================

report = f"""
# Token Analysis Report

## Dataset

Rows: {len(df)}

---

# Resume Tokens

| Metric | Value |
|----------|----------|
| Average | {resume_stats['avg']} |
| Median | {resume_stats['median']} |
| P95 | {resume_stats['p95']} |
| P99 | {resume_stats['p99']} |
| Max | {resume_stats['max']} |
| Min | {resume_stats['min']} |

---

# Job Description Tokens

| Metric | Value |
|----------|----------|
| Average | {jd_stats['avg']} |
| Median | {jd_stats['median']} |
| P95 | {jd_stats['p95']} |
| P99 | {jd_stats['p99']} |
| Max | {jd_stats['max']} |
| Min | {jd_stats['min']} |

---

# Combined Tokens

| Metric | Value |
|----------|----------|
| Average | {combined_stats['avg']} |
| Median | {combined_stats['median']} |
| P95 | {combined_stats['p95']} |
| P99 | {combined_stats['p99']} |
| Max | {combined_stats['max']} |
| Min | {combined_stats['min']} |

---

# Recommended Training Configuration

Recommended max_seq_length:

```python
max_seq_length = {recommended_seq}
```
"""

# Write report to file
with open(REPORT_PATH, "w", encoding="utf-8") as f:
    f.write(report)

print(f"\nSaved token analysis report to: {REPORT_PATH}")