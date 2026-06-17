# Final Dataset Validation Report

Generated on: 2026-06-16 13:44:50
Tokenizer Model: `meta-llama/Llama-3.2-1B-Instruct`

This report validates the integrity, quality, schema format, and token distributions of all fine-tuning and instruction datasets prepared for the Argus AI Resume Adapter.

---

## Executive Summary

| Dataset Name | Format | Total Rows | Exact Duplicates | Near Duplicates (Jaccard > 0.85) | Schema Violations (Fail) | Quality Warnings | Validation Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Resume Job Fit (Training Ready)** | JSON Lines | 6,217 | 0 | 913 | 0 | 0 | ✅ **PASS** |
| **Resume Sections Instruction** | JSON Lines | 59,670 | 0 | 0 | 0 | 0 | ✅ **PASS** |
| **Resume Summary Synthetic** | JSON Array | 135 | 0 | 0 | 0 | 0 | ✅ **PASS** |
| **Resume Review Synthetic** | JSON Array | 200 | 0 | 0 | 0 | 0 | ✅ **PASS** |

---

## Token length Profiles

All token counts are estimated using the Llama 3.2 tokenizer.

### 📊 Resume Job Fit (Training Ready)

| Field Context | Min Tokens | Max Tokens | Mean Tokens | Median Tokens | 95th Percentile | 99th Percentile |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Combined (Record)** | 287 | 5,074 | 1555.9 | 1437.0 | 2837.4 | 3623.7 |
| **Input (Resume/Prompt)** | 178 | 4,131 | 1094.0 | 965.0 | 2237.0 | 3156.0 |
| **Output (Summary/Response)** | 1 | 2 | 1.8 | 2.0 | 2.0 | 2.0 |

### 📊 Resume Sections Instruction

| Field Context | Min Tokens | Max Tokens | Mean Tokens | Median Tokens | 95th Percentile | 99th Percentile |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Combined (Record)** | 8 | 401 | 21.3 | 18.0 | 43.0 | 79.3 |
| **Input (Resume/Prompt)** | 1 | 394 | 14.2 | 11.0 | 36.0 | 72.0 |
| **Output (Summary/Response)** | 1 | 2 | 1.1 | 1.0 | 2.0 | 2.0 |

### 📊 Resume Summary Synthetic

| Field Context | Min Tokens | Max Tokens | Mean Tokens | Median Tokens | 95th Percentile | 99th Percentile |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Combined (Record)** | 154 | 441 | 316.5 | 334.0 | 396.3 | 427.2 |
| **Input (Resume/Prompt)** | 80 | 297 | 191.7 | 196.0 | 258.3 | 280.2 |
| **Output (Summary/Response)** | 74 | 151 | 125.1 | 131.0 | 144.0 | 147.0 |

### 📊 Resume Review Synthetic

| Field Context | Min Tokens | Max Tokens | Mean Tokens | Median Tokens | 95th Percentile | 99th Percentile |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Combined (Record)** | 100 | 202 | 148.2 | 154.0 | 183.1 | 194.0 |
| **Input (Resume/Prompt)** | 17 | 96 | 53.9 | 57.0 | 84.0 | 88.0 |
| **Output (Summary/Response)** | 73 | 117 | 94.3 | 96.0 | 107.0 | 113.0 |

---

## Quality Auditing Details

Quality warnings provide detailed insights into minor text layout anomalies and structural features.

### ⚠️ Resume Job Fit (Training Ready) Quality Details
- **Empty / Whitespace fields:** 0
- **Excessive Repetition:** 0
- **Corrupted Unicode / Mojibake:** 0
- **Extremely Short (<3 chars):** 0
- **Extremely Long (>100k chars):** 0

### ⚠️ Resume Sections Instruction Quality Details
- **Empty / Whitespace fields:** 0
- **Excessive Repetition:** 0
- **Corrupted Unicode / Mojibake:** 0
- **Extremely Short (<3 chars):** 0
- **Extremely Long (>100k chars):** 0

### ⚠️ Resume Summary Synthetic Quality Details
- **Empty / Whitespace fields:** 0
- **Excessive Repetition:** 0
- **Corrupted Unicode / Mojibake:** 0
- **Extremely Short (<3 chars):** 0
- **Extremely Long (>100k chars):** 0

### ⚠️ Resume Review Synthetic Quality Details
- **Empty / Whitespace fields:** 0
- **Excessive Repetition:** 0
- **Corrupted Unicode / Mojibake:** 0
- **Extremely Short (<3 chars):** 0
- **Extremely Long (>100k chars):** 0

---

## Technical Details

- **Validation Engine:** `final_dataset_validator.py`
- **Execution Time:** 50.07 seconds
- **Tokenizer Fallback Used:** Yes
