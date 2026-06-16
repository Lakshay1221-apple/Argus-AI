# Final Dataset Validation Report V2

Generated on: 2026-06-16 14:41:39
Tokenizer Model: `meta-llama/Llama-3.2-1B-Instruct`

This report validates the integrity, quality, schema format, and token distributions of all fine-tuning and instruction datasets prepared for the Argus AI Resume Adapter, following the synthetic dataset expansion and sanitization pass.

---

## 🧹 Synthetic Cleanup Statistics

| Synthetic Dataset | Original Loaded | Malformed JSON | Corrupted Records | Exact Duplicates | Near Duplicates | Repeated Outputs | Final Cleaned |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Resume Summary** | 418 | 0 | 0 | 0 | 0 | 0 | **418** |
| **Resume Review** | 784 | 0 | 0 | 0 | 0 | 0 | **784** |

---

## 📊 Executive Summary

| Dataset Name | Format | Total Rows | Exact Duplicates | Near Duplicates (Jaccard > 0.85) | Schema Violations (Fail) | Quality Warnings | Validation Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Resume Job Fit (Training Ready)** | JSON Lines | 6,217 | 0 | 906 | 0 | 0 | ✅ **PASS** |
| **Resume Sections Instruction** | JSON Lines | 59,670 | 0 | 0 | 0 | 0 | ✅ **PASS** |
| **Resume Summary Synthetic** | JSON Array | 418 | 0 | 0 | 0 | 0 | ✅ **PASS** |
| **Resume Review Synthetic** | JSON Array | 784 | 0 | 0 | 0 | 0 | ✅ **PASS** |

---

## Token Length Profiles

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
| **Combined (Record)** | 59 | 441 | 150.1 | 74.0 | 378.0 | 398.8 |
| **Input (Resume/Prompt)** | 42 | 297 | 98.1 | 56.0 | 240.1 | 261.0 |
| **Output (Summary/Response)** | 13 | 151 | 52.2 | 19.0 | 140.0 | 144.8 |

### 📊 Resume Review Synthetic

| Field Context | Min Tokens | Max Tokens | Mean Tokens | Median Tokens | 95th Percentile | 99th Percentile |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Combined (Record)** | 74 | 202 | 117.3 | 116.0 | 168.0 | 186.0 |
| **Input (Resume/Prompt)** | 14 | 96 | 34.5 | 27.0 | 77.0 | 86.2 |
| **Output (Summary/Response)** | 58 | 117 | 82.8 | 86.0 | 104.0 | 109.0 |

---

## Quality Auditing Details

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

- **Validation Engine:** `final_dataset_validator.py` (V2)
- **Execution Time:** 40.67 seconds
- **Tokenizer Fallback Used:** Yes
