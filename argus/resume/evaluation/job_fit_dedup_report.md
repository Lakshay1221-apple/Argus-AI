# Resume Job Fit Deduplication Report

Generated on: 2026-06-16 14:50:40

This report documents the near-duplicate removal process applied to `resume_job_fit_training_ready.jsonl` using LSH conflict resolution.

---

## 📊 Deduplication Metrics

| Metric | Count | Percentage |
| :--- | :---: | :---: |
| **Original Rows** | 6,217 | 100.00% |
| **Removed (Near Duplicates)** | 366 | 5.89% |
| **Final Cleaned Rows** | **5,851** | **94.11%** |

---

## 🎯 Label Distribution Balance

The deduplication algorithm prioritized removing duplicates from more frequent labels, moving the dataset towards a more balanced label state while eliminating redundancy.

| Label | Count Before | % Before | Count After | % After | Delta (Rows) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Fit** | 1,542 | 24.80% | 1,432 | 24.47% | -110 |
| **No Fit** | 3,136 | 50.44% | 2,965 | 50.68% | -171 |
| **Partial Fit** | 1,539 | 24.75% | 1,454 | 24.85% | -85 |
