"""
Dataset Cleaning and Reporting Pipeline for Argus AI Resume Job Description Fit.
"""

import re
import logging
from pathlib import Path
from typing import Dict, Any, List, Tuple
import pandas as pd

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Regex Patterns for PII, URLs and Addresses
EMAIL_REGEX = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
PHONE_REGEX = re.compile(r"(?:\+?\d{1,3}[-.\s]*)?\(?\d{3}\)?[-.\s]*\d{3}[-.\s]*\d{4}")
LINKEDIN_REGEX = re.compile(r"\b(?:https?://)?(?:www\.)?linkedin\.com/\S*", re.IGNORECASE)
GITHUB_REGEX = re.compile(r"\b(?:https?://)?(?:www\.)?github\.com/\S*", re.IGNORECASE)
GENERAL_URL_REGEX = re.compile(r"https?://\S+|www\.\S+", re.IGNORECASE)

PLACEHOLDER_ADDR_REGEX = re.compile(r"\bCity\s*,\s*ST(?:ATE)?\b", re.IGNORECASE)
CITY_STATE_ST_REGEX = re.compile(r"\b[A-Z][a-zA-Z\s.-]{1,20},\s*[A-Z]{2}\b")
STREET_ADDR_REGEX = re.compile(
    r"\b\d+\s+[A-Za-z0-9\s.,#-]{2,40}\s+(?:Street|St|Avenue|Ave|Road|Rd|Drive|Dr|Lane|Ln|Court|Ct|Circle|Cir|Way|Boulevard|Blvd|Parkway|Pkwy)\b",
    re.IGNORECASE
)
ZIP_REGEX = re.compile(r"\b\d{5}(?:-\d{4})?\b")

LABEL_MAPPING = {
    "Good Fit": "Fit",
    "Potential Fit": "Partial Fit",
    "No Fit": "No Fit"
}

VALID_LABELS = {"Fit", "No Fit", "Partial Fit"}

def load_data(file_path: Path) -> pd.DataFrame:
    """Load JSONL dataset into a pandas DataFrame."""
    logger.info(f"Loading raw dataset from {file_path}")
    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found at {file_path}")
    return pd.read_json(file_path, lines=True)

def clean_text(text: str) -> str:
    """Apply cleaning regexes and normalize whitespace in text."""
    if not isinstance(text, str):
        return ""
    
    # Replace PII and URLs with space to prevent word merging
    text = EMAIL_REGEX.sub(" ", text)
    text = PHONE_REGEX.sub(" ", text)
    text = LINKEDIN_REGEX.sub(" ", text)
    text = GITHUB_REGEX.sub(" ", text)
    text = GENERAL_URL_REGEX.sub(" ", text)
    
    # Replace physical addresses
    text = PLACEHOLDER_ADDR_REGEX.sub(" ", text)
    text = STREET_ADDR_REGEX.sub(" ", text)
    text = CITY_STATE_ST_REGEX.sub(" ", text)
    text = ZIP_REGEX.sub(" ", text)
    
    # Whitespace normalization
    text = text.replace("\r\n", "\n")
    text = text.replace("\t", " ")
    
    # Strip trailing whitespace on each line
    text = "\n".join(line.rstrip() for line in text.splitlines())
    
    # Replace 3 or more newlines with a double newline
    text = re.sub(r"\n{3,}", "\n\n", text)
    
    # Replace 2 or more spaces with a single space
    text = re.sub(r" {2,}", " ", text)
    
    return text.strip()

def compute_statistics(df: pd.DataFrame) -> Dict[str, Any]:
    """Compute statistics for the dataset."""
    stats = {}
    stats["total_rows"] = len(df)
    stats["columns"] = list(df.columns)
    
    # Missing values per column
    missing_vals = df.isna().sum().to_dict()
    # Also count empty strings as missing/null
    for col in df.columns:
        if df[col].dtype == object:
            empty_count = (df[col] == "").sum()
            missing_vals[col] = int(missing_vals[col] + empty_count)
    stats["missing_values"] = missing_vals
    
    # Duplicates (all columns)
    stats["duplicates"] = int(df.duplicated().sum())
    
    # Label distribution
    label_counts = df["label"].value_counts(dropna=False).to_dict()
    label_dist = {}
    for label, count in label_counts.items():
        label_str = str(label)
        pct = (count / len(df)) * 100 if len(df) > 0 else 0.0
        label_dist[label_str] = {"count": int(count), "percentage": round(pct, 2)}
    stats["label_distribution"] = label_dist
    
    # Lengths
    resume_lens = df["resume_text"].fillna("").str.len()
    jd_lens = df["job_description_text"].fillna("").str.len()
    
    stats["avg_resume_len"] = float(resume_lens.mean()) if len(df) > 0 else 0.0
    stats["avg_jd_len"] = float(jd_lens.mean()) if len(df) > 0 else 0.0
    stats["min_resume_len"] = int(resume_lens.min()) if len(df) > 0 else 0
    stats["max_resume_len"] = int(resume_lens.max()) if len(df) > 0 else 0
    stats["min_jd_len"] = int(jd_lens.min()) if len(df) > 0 else 0
    stats["max_jd_len"] = int(jd_lens.max()) if len(df) > 0 else 0
    
    return stats

def generate_report_md(stats: Dict[str, Any], df: pd.DataFrame, title: str, is_after: bool = False, extra_metrics: Dict[str, int] = None) -> str:
    """Generate exploration report as Markdown string."""
    md = f"# {title}\n\n"
    
    if is_after and extra_metrics:
        md += "## Pipeline Removals Summary\n\n"
        md += "| Filter Type | Count |\n"
        md += "| :--- | :--- |\n"
        md += f"| Original Rows | {extra_metrics['original_rows']} |\n"
        md += f"| Null Rows Removed | {extra_metrics['null_removed']} |\n"
        md += f"| Duplicate Rows Removed | {extra_metrics['duplicate_removed']} |\n"
        md += f"| Invalid Label Rows Removed | {extra_metrics['invalid_label_removed']} |\n"
        md += f"| Length Filter (<100) Removed | {extra_metrics['length_removed']} |\n"
        md += f"| **Final Cleaned Rows** | **{stats['total_rows']}** |\n"
        md += f"| **Total Rows Removed** | **{extra_metrics['total_removed']}** |\n\n"
        
    md += "## Dataset Statistics\n\n"
    md += f"- **Total Rows:** {stats['total_rows']}\n"
    md += f"- **Column Names:** {', '.join([f'`{c}`' for c in stats['columns']])}\n"
    md += f"- **Duplicate Rows:** {stats['duplicates']}\n\n"
    
    md += "### Missing Values Per Column\n\n"
    md += "| Column | Missing Count |\n"
    md += "| :--- | :--- |\n"
    for col, count in stats["missing_values"].items():
        md += f"| `{col}` | {count} |\n"
    md += "\n"
    
    md += "### Label Distribution\n\n"
    md += "| Label | Count | Percentage |\n"
    md += "| :--- | :--- | :--- |\n"
    for label, info in stats["label_distribution"].items():
        md += f"| `{label}` | {info['count']} | {info['percentage']}% |\n"
    md += "\n"
    
    md += "### Text Length Statistics (Characters)\n\n"
    md += "| Field | Average Length | Shortest | Longest |\n"
    md += "| :--- | :--- | :--- | :--- |\n"
    md += f"| Resume | {stats['avg_resume_len']:.2f} | {stats['min_resume_len']} | {stats['max_resume_len']} |\n"
    md += f"| Job Description | {stats['avg_jd_len']:.2f} | {stats['min_jd_len']} | {stats['max_jd_len']} |\n\n"
    
    md += "## Random Sample Rows (5)\n\n"
    # Select 5 samples using a fixed seed
    if len(df) >= 5:
        samples = df.sample(n=5, random_state=42)
    else:
        samples = df
        
    for i, (_, row) in enumerate(samples.iterrows(), 1):
        md += f"### Sample {i}\n\n"
        md += f"**Label:** `{row['label']}`\n\n"
        
        resume_snippet = row["resume_text"][:300].replace("\n", " ") + ("..." if len(row["resume_text"]) > 300 else "")
        jd_snippet = row["job_description_text"][:300].replace("\n", " ") + ("..." if len(row["job_description_text"]) > 300 else "")
        
        md += f"**Resume Text Snippet:**\n> {resume_snippet}\n\n"
        md += f"**Job Description Snippet:**\n> {jd_snippet}\n\n"
        md += "---\n\n"
        
    return md

def generate_data_card_md(stats_before: Dict[str, Any], stats_after: Dict[str, Any], removals: Dict[str, int]) -> str:
    """Generate dataset data card as Markdown string."""
    md = "# Dataset Data Card — Resume Job Description Fit\n\n"
    md += "## Dataset Overview\n"
    md += "- **Dataset Name:** Resume and Job Description Fit Dataset\n"
    md += "- **Source Path:** `argus/resume/datasets/raw/resume-job-description-fit.jsonl`\n"
    md += "- **Destination Path:** `argus/resume/datasets/processed/resume_job_fit_clean.jsonl`\n"
    md += "- **Columns:** `resume_text`, `job_description_text`, `label`\n\n"
    
    md += "## Row Count Summary\n"
    md += f"- **Original Rows:** {stats_before['total_rows']}\n"
    md += f"- **Final Cleaned Rows:** {stats_after['total_rows']}\n"
    md += f"- **Total Rows Removed:** {removals['total_removed']} ({removals['total_removed']/stats_before['total_rows']*100:.2f}% reduction)\n\n"
    
    md += "## Label Distribution (Before vs After)\n\n"
    md += "| Raw Label | Raw Count | Raw % | Cleaned Label | Cleaned Count | Cleaned % |\n"
    md += "| :--- | :--- | :--- | :--- | :--- | :--- |\n"
    
    # Combine distributions
    raw_dist = stats_before["label_distribution"]
    clean_dist = stats_after["label_distribution"]
    
    # We know the raw labels: Good Fit, Potential Fit, No Fit
    # Mapped to: Fit, Partial Fit, No Fit
    mapping_rows = [
        ("Good Fit", "Fit"),
        ("Potential Fit", "Partial Fit"),
        ("No Fit", "No Fit")
    ]
    for raw, clean in mapping_rows:
        raw_info = raw_dist.get(raw, {"count": 0, "percentage": 0.0})
        clean_info = clean_dist.get(clean, {"count": 0, "percentage": 0.0})
        md += f"| `{raw}` | {raw_info['count']} | {raw_info['percentage']}% | `{clean}` | {clean_info['count']} | {clean_info['percentage']}% |\n"
    md += "\n"
    
    md += "## Cleaning Operations\n"
    md += "The following operations were applied sequentially to clean the raw dataset:\n"
    md += "1. **Null Removal:** Dropped rows where `resume_text`, `job_description_text`, or `label` was null/empty.\n"
    md += "2. **Exact Duplicate Removal:** Dropped identical duplicate rows.\n"
    md += "3. **PII Removal:** Removed email addresses and phone numbers using regular expressions.\n"
    md += "4. **URL Removal:** Removed LinkedIn, GitHub, portfolio, and other web links.\n"
    md += "5. **Physical Address Removal:** Removed street addresses, city-state combinations, ZIP codes, and placeholders like `City, STATE` where possible.\n"
    md += "6. **Whitespace Normalization:** Replaced tabs with spaces, normalized consecutive newlines/spaces, and trimmed leading/trailing spaces.\n"
    md += "7. **Label Validation:** Mapped legacy labels (`Good Fit` ➔ `Fit`, `Potential Fit` ➔ `Partial Fit`, `No Fit` ➔ `No Fit`) and removed invalid labels.\n"
    md += "8. **Length Filtering:** Dropped rows where the cleaned `resume_text` or `job_description_text` was less than 100 characters.\n\n"
    
    md += "## Known Limitations\n"
    md += "- **Punctuation Artifacts:** Address stripping regexes replace target patterns with a single space. This can leave trailing commas or double separators (e.g. `Company, , WI` becomes `Company ,`). Whitespace normalization reduces extra spaces but some punctuation fragments may remain.\n"
    md += "- **Implicit Locations:** General country names or cities not followed by a 2-letter state code or ZIP code (e.g., just `New York` or `London`) are preserved to prevent accidental deletion of educational institutions or company names.\n"
    md += "- **URL Truncation:** Highly non-standard URLs that do not begin with `http`, `www`, `github.com`, or `linkedin.com` might escape detection.\n"
    return md

def generate_samples_md(df_before: pd.DataFrame, df_after: pd.DataFrame, count: int = 10, seed: int = 42) -> str:
    """Generate Markdown visualizing 10 random samples before and after cleaning."""
    common_indices = df_before.index.intersection(df_after.index)
    if len(common_indices) < count:
        sample_indices = common_indices.tolist()
    else:
        sample_indices = common_indices.to_series().sample(n=count, random_state=seed).tolist()
        
    md = "# Dataset Cleaning Visual Inspection Samples\n\n"
    md += "This document displays 10 random samples showing their text **before** and **after** cleaning. Use this to verify that the regex cleaning operations did not remove valid technical content (such as `C++`, `C#`, `Node.js`).\n\n"
    
    for i, idx in enumerate(sample_indices, 1):
        row_before = df_before.loc[idx]
        row_after = df_after.loc[idx]
        
        md += f"## Sample {i} (Original Row Index: {idx})\n\n"
        md += f"- **Label:** `{row_before['label']}` ➔ `{row_after['label']}`\n"
        md += f"- **Before Lengths:** Resume = {len(row_before['resume_text'])} chars, JD = {len(row_before['job_description_text'])} chars\n"
        md += f"- **After Lengths:** Resume = {len(row_after['resume_text'])} chars, JD = {len(row_after['job_description_text'])} chars\n\n"
        
        md += "### 📄 Resume Text Comparison\n\n"
        md += "<details>\n<summary>Show Original Resume</summary>\n\n"
        md += f"```text\n{row_before['resume_text']}\n```\n"
        md += "</details>\n\n"
        md += "<details>\n<summary>Show Cleaned Resume</summary>\n\n"
        md += f"```text\n{row_after['resume_text']}\n```\n"
        md += "</details>\n\n"
        
        md += "### 💼 Job Description Text Comparison\n\n"
        md += "<details>\n<summary>Show Original Job Description</summary>\n\n"
        md += f"```text\n{row_before['job_description_text']}\n```\n"
        md += "</details>\n\n"
        md += "<details>\n<summary>Show Cleaned Job Description</summary>\n\n"
        md += f"```text\n{row_after['job_description_text']}\n```\n"
        md += "</details>\n\n"
        
        md += "---\n\n"
        
    return md

def main():
    logger.info("Starting Resume Job Description Fit dataset cleaning pipeline...")
    
    raw_path = Path("argus/resume/datasets/raw/resume-job-description-fit.jsonl")
    processed_dir = Path("argus/resume/datasets/processed")
    evaluation_dir = Path("argus/resume/evaluation/_archive")
    
    # Create target directories
    processed_dir.mkdir(parents=True, exist_ok=True)
    evaluation_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. Load raw dataset
    df_raw = load_data(raw_path)
    df_before = df_raw.copy()
    
    # 2. Generate and save before-cleaning report
    logger.info("Computing initial statistics...")
    stats_before = compute_statistics(df_raw)
    report_before_md = generate_report_md(stats_before, df_raw, "Dataset Exploration Report — BEFORE CLEANING", is_after=False)
    report_before_path = evaluation_dir / "resume_job_fit_report_before.md"
    report_before_path.write_text(report_before_md, encoding="utf-8")
    logger.info(f"Saved exploration report before cleaning to {report_before_path}")
    
    # 3. Cleaning Pipeline with stats tracking
    n_start = len(df_raw)
    
    # Filter Nulls
    null_mask = df_raw["resume_text"].isna() | df_raw["job_description_text"].isna() | df_raw["label"].isna()
    n_null_removed = int(null_mask.sum())
    df_clean = df_raw[~null_mask].copy()
    logger.info(f"Removed {n_null_removed} null rows.")
    
    # Filter Exact Duplicates
    dup_mask = df_clean.duplicated()
    n_dup_removed = int(dup_mask.sum())
    df_clean = df_clean[~dup_mask].copy()
    logger.info(f"Removed {n_dup_removed} exact duplicate rows.")
    
    # Apply Text Cleaning
    logger.info("Cleaning resumes and job descriptions...")
    df_clean["resume_text"] = df_clean["resume_text"].apply(clean_text)
    df_clean["job_description_text"] = df_clean["job_description_text"].apply(clean_text)
    
    # Map and Validate Labels
    logger.info("Mapping and validating labels...")
    # Map raw labels
    df_clean["label"] = df_clean["label"].map(LABEL_MAPPING)
    # Check for invalid labels
    invalid_label_mask = ~df_clean["label"].isin(VALID_LABELS)
    n_invalid_label_removed = int(invalid_label_mask.sum())
    df_clean = df_clean[~invalid_label_mask].copy()
    logger.info(f"Removed {n_invalid_label_removed} rows with invalid labels.")
    
    # Filter by Length (< 100 characters in either resume or job description)
    length_mask = (df_clean["resume_text"].str.len() < 100) | (df_clean["job_description_text"].str.len() < 100)
    n_length_removed = int(length_mask.sum())
    df_clean = df_clean[~length_mask].copy()
    logger.info(f"Removed {n_length_removed} rows failing length filters.")
    
    n_end = len(df_clean)
    n_total_removed = n_start - n_end
    
    removals = {
        "original_rows": n_start,
        "null_removed": n_null_removed,
        "duplicate_removed": n_dup_removed,
        "invalid_label_removed": n_invalid_label_removed,
        "length_removed": n_length_removed,
        "total_removed": n_total_removed
    }
    
    # 4. Generate and save after-cleaning report
    logger.info("Computing cleaned dataset statistics...")
    stats_after = compute_statistics(df_clean)
    report_after_md = generate_report_md(stats_after, df_clean, "Dataset Exploration Report — AFTER CLEANING", is_after=True, extra_metrics=removals)
    report_after_path = evaluation_dir / "resume_job_fit_report_after.md"
    report_after_path.write_text(report_after_md, encoding="utf-8")
    logger.info(f"Saved exploration report after cleaning to {report_after_path}")
    
    # 5. Generate and save data card
    data_card_md = generate_data_card_md(stats_before, stats_after, removals)
    data_card_path = evaluation_dir / "resume_job_fit_data_card.md"
    data_card_path.write_text(data_card_md, encoding="utf-8")
    logger.info(f"Saved dataset data card to {data_card_path}")
    
    # 6. Generate and save random samples file
    samples_md = generate_samples_md(df_before, df_clean, count=10, seed=42)
    samples_path = evaluation_dir / "resume_job_fit_samples.md"
    samples_path.write_text(samples_md, encoding="utf-8")
    logger.info(f"Saved visual inspection samples to {samples_path}")
    
    # 7. Export Cleaned Dataset
    clean_dataset_path = processed_dir / "resume_job_fit_clean.jsonl"
    df_clean.to_json(clean_dataset_path, orient="records", lines=True)
    logger.info(f"Saved cleaned dataset to {clean_dataset_path}")
    logger.info("Dataset cleaning and reporting pipeline completed successfully!")

if __name__ == "__main__":
    main()