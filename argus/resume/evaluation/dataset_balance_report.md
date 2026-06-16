Create:

argus/resume/scripts/training/dataset_balance_report.py

Requirements:

Read:

- resume_sections_instruction.jsonl
- resume_job_fit_training_ready.jsonl
- resume_summary_synthetic.jsonl
- resume_review_synthetic_v1.jsonl

Generate:

argus/resume/evaluation/dataset_balance_report.md

Show:

==================================================
DATASET COUNTS
==================================================

Resume Sections
Resume Job Fit
Resume Summary
Resume Review

==================================================
PERCENTAGE CONTRIBUTION
==================================================

Show percentage of total dataset.

==================================================
TOKEN CONTRIBUTION
==================================================

Estimate total tokens contributed by each dataset.

==================================================
TRAINING RISK ANALYSIS
==================================================

Identify:

- dominant datasets
- underrepresented datasets
- training skew risks

==================================================
RECOMMENDED DOWNSAMPLING
==================================================

Recommend balanced ratios for Adapter V1.