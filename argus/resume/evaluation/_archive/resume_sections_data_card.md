# Dataset Data Card — Resume Section Classification

## Dataset Overview

- **Dataset Name:** Resume Section Classification Dataset
- **Source Path:** `argus/resume/datasets/raw/resume_seven_class.jsonl`
- **Processed Output Path (Standard):** `argus/resume/datasets/processed/resume_sections_clean.jsonl`
- **Processed Output Path (Instruction):** `argus/resume/datasets/processed/resume_sections_instruction.jsonl`
- **Task:** Section Classification (mapping resume paragraphs to their standard section headers)

## Row Count Summary

- **Original Rows:** 78670
- **Final Cleaned Rows:** 59670
- **Total Rows Removed:** 19000 (24.15% reduction)

## Label Mapping

Prefixes are extracted from raw lines and mapped as follows:
- `PI` ➔ `Personal Information`
- `Sum` ➔ `Summary`
- `Skill` ➔ `Skills`
- `Exp` ➔ `Experience`
- `Edu` ➔ `Education`
- `Obj` ➔ `Objective`
- *Any other prefix* ➔ `INVALID` (and removed from the dataset)

## Cleaning Operations

1. **PII and URL Scrubbing:** Inline regex removal of emails, phone numbers, and URLs. Specific street address details and zip codes are removed.
2. **Key Category Preservation:** General locations (Cities, States), Names, and Job Titles are explicitly preserved.
3. **Punctuation Normalization:** Normalized duplicated identical symbols, while preserving standard programming terms (like `C++`, `C#`).
4. **Whitespace and Unicode Standardisation:** Performed NFKC Unicode normalization, standardizing smart quotes/dashes/bullets to ASCII equivalents, and stripped excessive spacing/newlines.
5. **Quality Filtering:** Dropped entries containing empty content, rows with length under 3 characters, duplicate records, rows with invalid/unknown prefixes, and non-informative placeholder inputs (e.g. `N/A`, `-`, etc.).

## Intended Use Cases

- Fine-tuning adapters for resume parser systems (like Argus AI Resume Understanding).
- Text classification models distinguishing different components of user profiles or resumes.
- Instruction tuning models for structured extraction of resume contents.

## Not Recommended Use Cases

- Direct evaluation of full resumes (this dataset contains segmented paragraph-level fragments rather than whole resumes).
- Tasks requiring exact contact retrieval, since all specific PII (emails, phones, street addresses) has been scrubbed.

## Known Limitations

- Paragraph fragments are disconnected, losing global resume layout context.
- Short headers (e.g. 'Responsibilities') are kept in Experience, which can lead to high similarity between segments if context is missing.

## Training Readiness Assessment

### Scorecard

- **Data Quality:** `9/10`
  - *Reasoning:* PII is safely scrubbed and trivial records/punctuation-only artifacts are removed. Text formats are normalized across all entries.
- **Label Quality:** `10/10`
  - *Reasoning:* Checked that 100% of final records map to exactly 6 distinct valid section labels, with no malformed, empty, or misspelled headers surviving.
- **Training Readiness:** `9.5/10`
  - *Reasoning:* Provides both a standard section classification file and a fully instruction-formatted dataset with inputs, instructions, outputs, and task metadata. Direct compatibility with SFT/LoRA fine-tuning libraries.

### Final Verdict
This dataset is **highly recommended** for LoRA fine-tuning or section classification tasks in the resume parsing pipeline.
