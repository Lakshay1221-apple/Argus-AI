# Review Dataset Format Audit Report

Generated on: 2026-06-16 15:01:16

This report documents the format normalization and schema compliance audit applied to the synthetic resume review dataset.

---

## 📊 Summary Metrics

| Metric | Count | Percentage |
| :--- | :---: | :---: |
| **Total Records Inspected** | 784 | 100.00% |
| **Records Requiring Normalization** | 0 | 0.00% |
| **Clean Records (No Modifications)** | 784 | 100.00% |
| **Total Schema Violations Found** | 0 | - |

---

## 🔍 Violations Breakdown

The following schema violations and inconsistencies were identified and automatically corrected:

| Violation Category | Occurrences | Corrective Action |
| :--- | :---: | :--- |
| **Missing Fields** | 0 | Re-initialized fields with structured defaults (empty lists / default scores). |
| **Renamed / Alternate Fields** | 0 | Remapped legacy keys (e.g. `fit_verdict` ➔ `verdict`, `strength` ➔ `strengths`). |
| **Invalid Verdict Labels** | 0 | Standardized synonyms and out-of-spec verdicts to allowed pool (`Weak Fit`, `Potential Fit`, `Strong Fit`). |
| **Score Type Mismatches** | 0 | Cast floats and string representation of ATS scores to integers. |
| **List Type Mismatches** | 0 | Wrapped raw strings in lists for strengths, weaknesses, and suggestions. |
| **Other Schema Drift** | 0 | Standardized other JSON structures. |

---

## ✅ Final Schema Verification

All **784** records in the output file [resume_review_synthetic_v2.jsonl](file:///home/lakshay/Argus%20AI/argus/resume/datasets/processed/resume_review_synthetic_v2.jsonl) have been verified to strictly adhere to the target schema:
```json
{
  "ats_score": integer,
  "strengths": [string],
  "weaknesses": [string],
  "suggestions": [string],
  "verdict": string
}
```

**Status:** ✅ **PASS**
