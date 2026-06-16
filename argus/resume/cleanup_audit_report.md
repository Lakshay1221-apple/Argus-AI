# Resume Adapter Repository Cleanup Audit Report

This report outlines the full audit of the `argus/resume/` directory. The goal is to identify a minimal, clean, and reproducible layout for Resume Adapter V1 training and long-term future maintenance.

No files have been modified, moved, or deleted as part of this audit.

---

## 📊 Classification Matrix

Every file in the repository has been assigned to exactly one of the four categories:

### 🟢 KEEP (Preserve in Active Layout)
These files are critical for Adapter V1 training, dataset validation, quality gates, and reproducing datasets from scratch.

*   **Raw Datasets (Source of Truth):**
    *   [resume_seven_class.jsonl](file:///home/lakshay/Argus%20AI/argus/resume/datasets/raw/resume_seven_class.jsonl)
    *   [resume-summary.jsonl](file:///home/lakshay/Argus%20AI/argus/resume/datasets/raw/resume-summary.jsonl)
    *   [resume-job-description-fit.jsonl](file:///home/lakshay/Argus%20AI/argus/resume/datasets/raw/resume-job-description-fit.jsonl)
*   **Canonical Cleaned Datasets (Mixture Ingredients):**
    *   [resume_sections_instruction.jsonl](file:///home/lakshay/Argus%20AI/argus/resume/datasets/processed/resume_sections_instruction.jsonl)
    *   [resume_job_fit_training_ready_v2.jsonl](file:///home/lakshay/Argus%20AI/argus/resume/datasets/processed/resume_job_fit_training_ready_v2.jsonl) (Sanitized V2 deduplicated Job Fit)
    *   [resume_summary_synthetic.jsonl](file:///home/lakshay/Argus%20AI/argus/resume/datasets/processed/resume_summary_synthetic.jsonl)
    *   [resume_review_synthetic_v2.jsonl](file:///home/lakshay/Argus%20AI/argus/resume/datasets/processed/resume_review_synthetic_v2.jsonl) (Strict schema standardized reviews)
*   **Final SFT Training Target:**
    *   [resume_adapter_v1_standardized.jsonl](file:///home/lakshay/Argus%20AI/argus/resume/training/resume_adapter_v1_standardized.jsonl) (Standardized instruction-tuning target file)
*   **NotebookLM Knowledge Document:**
    *   [notebooklm_resume_summary_source.md](file:///home/lakshay/Argus%20AI/argus/resume/datasets/notebooklm/notebooklm_resume_summary_source.md)
*   **Active Maintenance & Builder Scripts:**
    *   [build_resume_adapter_v1.py](file:///home/lakshay/Argus%20AI/argus/resume/scripts/training/build_resume_adapter_v1.py) (Step 1-4 pipeline builder)
    *   [final_dataset_validator.py](file:///home/lakshay/Argus%20AI/argus/resume/scripts/training/final_dataset_validator.py) (Strict token/format validator)
    *   [run_final_quality_audit.py](file:///home/lakshay/Argus%20AI/argus/resume/scripts/training/run_final_quality_audit.py) (Task 1-4 quality gate normalizer)
    *   [dataset_balance_report.py](file:///home/lakshay/Argus%20AI/argus/resume/scripts/training/dataset_balance_report.py) (Balance analyzer)
    *   [adapter_sampling_simulator.py](file:///home/lakshay/Argus%20AI/argus/resume/scripts/training/adapter_sampling_simulator.py) (Downsampling simulator)
    *   [build_notebooklm_summary_source.py](file:///home/lakshay/Argus%20AI/argus/resume/scripts/synthetic/build_notebooklm_summary_source.py) (Extracts data to Markdown source)
    *   [sanitize_datasets.py](file:///home/lakshay/Argus%20AI/argus/resume/scripts/Clean_Dataset/sanitize_datasets.py) (Unicode reconstruction)
    *   [clean_resume_summary.py](file:///home/lakshay/Argus%20AI/argus/resume/scripts/Clean_Dataset/clean_resume_summary.py) (Raw summary cleaner)
    *   [clean_resume_job.py](file:///home/lakshay/Argus%20AI/argus/resume/scripts/Clean_Dataset/clean_resume_job.py) (Raw Job Fit cleaner)
    *   [clean_resume_sections.py](file:///home/lakshay/Argus%20AI/argus/resume/scripts/Clean_Dataset/clean_resume_sections.py) (Raw sections cleaner)
    *   [optimize_resume_job_for_training.py](file:///home/lakshay/Argus%20AI/argus/resume/scripts/Clean_Dataset/optimize_resume_job_for_training.py) (JD/Resume boilerplate stripper)
    *   [token_analysis.py](file:///home/lakshay/Argus%20AI/argus/resume/scripts/token_analysis.py) (Initial token baseline script)
*   **Final Verification Reports (Freeze Gate):**
    *   [final_training_readiness_report.md](file:///home/lakshay/Argus%20AI/argus/resume/evaluation/final_training_readiness_report.md) (Final Freeze sign-off)
    *   [adapter_dataset_report.md](file:///home/lakshay/Argus%20AI/argus/resume/evaluation/adapter_dataset_report.md) (SFT dataset validation report)

---

### 🟡 ARCHIVE (Move to `argus/resume/archive/`)
These are intermediate/older versions of datasets and exploratory reports. They are not needed for active runs, but have historical value.

*   **Older Dataset Versions:**
    *   [resume_adapter_v1.jsonl](file:///home/lakshay/Argus%20AI/argus/resume/training/resume_adapter_v1.jsonl) (Superceded by standardized dataset)
    *   [resume_sections_clean.jsonl](file:///home/lakshay/Argus%20AI/argus/resume/datasets/processed/resume_sections_clean.jsonl) (Superceded by instruction dataset)
    *   [resume_job_fit_clean.jsonl](file:///home/lakshay/Argus%20AI/argus/resume/datasets/processed/resume_job_fit_clean.jsonl) (Superceded by training ready dataset)
    *   [resume_review_synthetic_v1.jsonl](file:///home/lakshay/Argus%20AI/argus/resume/datasets/processed/resume_review_synthetic_v1.jsonl) (Superceded by schema-standardized V2)
*   **Intermediate Phase 1 & 2 Reports:**
    *   [resume_job_fit_report_before.md](file:///home/lakshay/Argus%20AI/argus/resume/evaluation/resume_job_fit_report_before.md)
    *   [resume_job_fit_report_after.md](file:///home/lakshay/Argus%20AI/argus/resume/evaluation/resume_job_fit_report_after.md)
    *   [resume_sections_report_before.md](file:///home/lakshay/Argus%20AI/argus/resume/evaluation/resume_sections_report_before.md)
    *   [resume_sections_report_after.md](file:///home/lakshay/Argus%20AI/argus/resume/evaluation/resume_sections_report_after.md)
    *   [resume_summary_report_before.md](file:///home/lakshay/Argus%20AI/argus/resume/evaluation/resume_summary_report_before.md)
    *   [resume_summary_report_after.md](file:///home/lakshay/Argus%20AI/argus/resume/evaluation/resume_summary_report_after.md)
    *   [resume_job_fit_data_card.md](file:///home/lakshay/Argus%20AI/argus/resume/evaluation/resume_job_fit_data_card.md)
    *   [resume_sections_data_card.md](file:///home/lakshay/Argus%20AI/argus/resume/evaluation/resume_sections_data_card.md)
    *   [resume_summary_data_card.md](file:///home/lakshay/Argus%20AI/argus/resume/evaluation/resume_summary_data_card.md)
    *   [resume_job_fit_samples.md](file:///home/lakshay/Argus%20AI/argus/resume/evaluation/resume_job_fit_samples.md)
    *   [resume_sections_samples.md](file:///home/lakshay/Argus%20AI/argus/resume/evaluation/resume_sections_samples.md)
    *   [resume_summary_samples.md](file:///home/lakshay/Argus%20AI/argus/resume/evaluation/resume_summary_samples.md)
    *   [resume_job_training_optimization_report.md](file:///home/lakshay/Argus%20AI/argus/resume/evaluation/resume_job_training_optimization_report.md)
    *   [resume_summary_generation_log.md](file:///home/lakshay/Argus%20AI/argus/resume/evaluation/resume_summary_generation_log.md)

---

### 🔴 DELETE (Safely Remove)
These files are either empty stubs, compile leftovers, or duplicate script files that should be deleted.

*   **Empty Python Stubs (0-byte files):**
    *   `argus/resume/training/train_resume.py`
    *   `argus/resume/scripts/format_resume_dataset.py`
    *   `argus/resume/scripts/validate_resume_dataset.py`
    *   `argus/resume/scripts/Clean_Dataset/clean_resume_section.py`
*   **Duplicate / Redundant Validator Script:**
    *   `argus/resume/scripts/Clean_Dataset/final_dataset_validator.py` (Superceded by the active, enhanced validator script `argus/resume/scripts/training/final_dataset_validator.py`)
*   **Outdated Report Versions (Superceded):**
    *   `argus/resume/evaluation/dataset_balance_report.md` (Superceded by V2)
    *   `argus/resume/evaluation/final_dataset_validation_report.md` (Superceded by V2)
    *   `argus/resume/evaluation/resume_summary_token_analysis.md` (Superceded by comprehensive token profiles in validation/balance reports)
*   **Python Build Cache Leftovers:**
    *   `argus/resume/scripts/Clean_Dataset/__pycache__/` and its `.pyc` compiled files.

---

### 🔵 REGENERABLE (Keep but marked as Dynamic)
These reports are useful, but can be regenerated automatically using scripts listed in the active Keep list. They do not need to be archived and can be left in the active reports directory.

*   `final_dataset_validation_report_v2.md` (Regenerated via `final_dataset_validator.py`)
*   `dataset_balance_report_v2.md` (Regenerated via `dataset_balance_report.py`)
*   `adapter_sampling_simulation.md` (Regenerated via `adapter_sampling_simulator.py`)
*   `adapter_sampling_simulation_v2.md` (Regenerated via `build_resume_adapter_v1.py` simulation mode)
*   `review_format_audit.md` (Regenerated via `run_final_quality_audit.py`)
*   `instruction_audit_report.md` (Regenerated via `run_final_quality_audit.py`)
*   `summary_quality_audit.md` (Regenerated via `run_final_quality_audit.py`)
*   `job_fit_dedup_report.md` (Regenerated via `build_resume_adapter_v1.py`)
*   `notebooklm_source_report.md` (Regenerated via `build_notebooklm_summary_source.py`)
*   `token_analysis_report.md` (Regenerated via `token_analysis.py`)

---

## 📂 Recommended Post-Cleanup Structure

This is the ideal target directory layout after executing the recommended moves and deletions:

```text
argus/resume/
├── archive/                            # Historical files
│   ├── datasets/
│   │   ├── resume_sections_clean.jsonl
│   │   ├── resume_job_fit_clean.jsonl
│   │   └── resume_review_synthetic_v1.jsonl
│   ├── training/
│   │   └── resume_adapter_v1.jsonl
│   └── evaluation/
│       ├── resume_job_fit_report_before.md
│       ├── resume_job_fit_report_after.md
│       ├── resume_sections_report_before.md
│       ├── resume_sections_report_after.md
│       ├── resume_summary_report_before.md
│       ├── resume_summary_report_after.md
│       ├── resume_job_fit_data_card.md
│       ├── resume_sections_data_card.md
│       ├── resume_summary_data_card.md
│       ├── resume_job_fit_samples.md
│       ├── resume_sections_samples.md
│       ├── resume_summary_samples.md
│       ├── resume_job_training_optimization_report.md
│       └── resume_summary_generation_log.md
├── configs/
├── datasets/
│   ├── raw/                            # Unmodified source datasets
│   │   ├── resume_seven_class.jsonl
│   │   ├── resume-summary.jsonl
│   │   └── resume-job-description-fit.jsonl
│   ├── processed/                      # Cleaned ingredients
│   │   ├── resume_sections_instruction.jsonl
│   │   ├── resume_job_fit_training_ready_v2.jsonl
│   │   ├── resume_summary_synthetic.jsonl
│   │   └── resume_review_synthetic_v2.jsonl
│   └── notebooklm/
│       └── notebooklm_resume_summary_source.md
├── evaluation/                         # Current active reports (Live/Regenerable)
│   ├── final_training_readiness_report.md
│   ├── adapter_dataset_report.md
│   ├── final_dataset_validation_report_v2.md
│   ├── dataset_balance_report_v2.md
│   ├── adapter_sampling_simulation_v2.md
│   ├── review_format_audit.md
│   ├── instruction_audit_report.md
│   ├── summary_quality_audit.md
│   └── job_fit_dedup_report.md
├── scripts/                            # Maintainable code
│   ├── training/                       # Fine-tuning active scripts
│   │   ├── build_resume_adapter_v1.py
│   │   ├── final_dataset_validator.py
│   │   ├── run_final_quality_audit.py
│   │   ├── dataset_balance_report.py
│   │   └── adapter_sampling_simulator.py
│   ├── synthetic/
│   │   └── build_notebooklm_summary_source.py
│   ├── Clean_Dataset/                  # Individual cleaners
│   │   ├── sanitize_datasets.py
│   │   ├── clean_resume_summary.py
│   │   ├── clean_resume_job.py
│   │   ├── clean_resume_sections.py
│   │   └── optimize_resume_job_for_training.py
│   └── token_analysis.py
└── training/                           # Frozen fine-tuning targets
    └── resume_adapter_v1_standardized.jsonl
```
