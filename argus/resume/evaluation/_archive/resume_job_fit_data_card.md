# Dataset Data Card — Resume Job Description Fit

## Dataset Overview
- **Dataset Name:** Resume and Job Description Fit Dataset
- **Source Path:** `argus/resume/datasets/raw/resume-job-description-fit.jsonl`
- **Destination Path:** `argus/resume/datasets/processed/resume_job_fit_clean.jsonl`
- **Columns:** `resume_text`, `job_description_text`, `label`

## Row Count Summary
- **Original Rows:** 6241
- **Final Cleaned Rows:** 6217
- **Total Rows Removed:** 24 (0.38% reduction)

## Label Distribution (Before vs After)

| Raw Label | Raw Count | Raw % | Cleaned Label | Cleaned Count | Cleaned % |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Good Fit` | 1542 | 24.71% | `Fit` | 1542 | 24.8% |
| `Potential Fit` | 1556 | 24.93% | `Partial Fit` | 1539 | 24.75% |
| `No Fit` | 3143 | 50.36% | `No Fit` | 3136 | 50.44% |

## Cleaning Operations
The following operations were applied sequentially to clean the raw dataset:
1. **Null Removal:** Dropped rows where `resume_text`, `job_description_text`, or `label` was null/empty.
2. **Exact Duplicate Removal:** Dropped identical duplicate rows.
3. **PII Removal:** Removed email addresses and phone numbers using regular expressions.
4. **URL Removal:** Removed LinkedIn, GitHub, portfolio, and other web links.
5. **Physical Address Removal:** Removed street addresses, city-state combinations, ZIP codes, and placeholders like `City, STATE` where possible.
6. **Whitespace Normalization:** Replaced tabs with spaces, normalized consecutive newlines/spaces, and trimmed leading/trailing spaces.
7. **Label Validation:** Mapped legacy labels (`Good Fit` ➔ `Fit`, `Potential Fit` ➔ `Partial Fit`, `No Fit` ➔ `No Fit`) and removed invalid labels.
8. **Length Filtering:** Dropped rows where the cleaned `resume_text` or `job_description_text` was less than 100 characters.

## Known Limitations
- **Punctuation Artifacts:** Address stripping regexes replace target patterns with a single space. This can leave trailing commas or double separators (e.g. `Company, , WI` becomes `Company ,`). Whitespace normalization reduces extra spaces but some punctuation fragments may remain.
- **Implicit Locations:** General country names or cities not followed by a 2-letter state code or ZIP code (e.g., just `New York` or `London`) are preserved to prevent accidental deletion of educational institutions or company names.
- **URL Truncation:** Highly non-standard URLs that do not begin with `http`, `www`, `github.com`, or `linkedin.com` might escape detection.
