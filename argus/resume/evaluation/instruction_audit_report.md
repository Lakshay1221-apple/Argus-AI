# Instruction Consistency Audit Report

Generated on: 2026-06-16 15:01:17

This report documents the standardization of instructions across all tasks in the fine-tuning dataset.

---

## 📊 Summary Metrics

| Metric | Count |
| :--- | :---: |
| **Total Records Inspected** | 7,202 |
| **Records Standardized** | 2,202 |
| **Unique Instructions Before Audit** | 4 |
| **Unique Instructions After Audit** | 4 |

---

## 🔄 Instruction Mapping & Consolidation

Below is the breakdown of instruction templates before and after the standardization pass:

### Before Standardization

- `Classify the resume section.`: **5,000** records
- `Determine the fit of the candidate's resume for the provided job description. Classify the fit as 'Fit', 'Partial Fit', or 'No Fit'.`: **1,000** records
- `Review the candidate's resume. Provide a qualitative assessment including an ATS score, key strengths, weaknesses, suggestions, and a verdict.`: **784** records
- `Summarize the candidate's professional experience, skills, and qualifications into a concise, high-impact resume summary.`: **418** records

### After Standardization (Allowed Pool)

- `Classify the resume section.`: **5,000** records
- `Determine the fit between the resume and job description.`: **1,000** records
- `Review this resume and provide ATS feedback.`: **784** records
- `Generate a professional resume summary.`: **418** records

---

## ✅ Final Consistency Check

The standardized dataset is saved at [resume_adapter_v1_standardized.jsonl](file:///home/lakshay/Argus%20AI/argus/resume/training/resume_adapter_v1_standardized.jsonl).
All records conform strictly to the four allowed instruction headers.

**Status:** ✅ **PASS**
