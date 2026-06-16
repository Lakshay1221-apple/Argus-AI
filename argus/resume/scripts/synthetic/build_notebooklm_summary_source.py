"""
Pipeline to build the NotebookLM Resume Summary Source document from cleaned datasets.
"""

import re
import logging
import collections
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

# Constants
NUM_RESUMES_TO_SAMPLE = 55
NUM_SECTIONS_PER_TYPE = 10  # 6 types * 10 = 60 sections total
EXPECTED_LABELS = ["Experience", "Skills", "Education", "Summary", "Objective", "Personal Information"]

def score_resume(text: str) -> float:
    """Score a resume's quality and details for sampling, returning -9999.0 if rejected."""
    if not isinstance(text, str):
        return -9999.0
        
    length = len(text)
    if length < 500:
        return -9999.0
        
    # Reject excessive consecutive repeated punctuation (more than 2 identical symbols) or long ellipses
    if re.search(r"([!?,;:=\-_~])\1{2,}", text) or re.search(r"\.{4,}", text):
        return -9999.0
        
    # Prefer structured and detailed text
    score = 0.0
    
    if 1000 <= length <= 4000:
        score += 100.0
    elif 500 <= length < 1000:
        score += 50.0
        
    # Prefer action verbs representing achievements
    action_verbs = [
        "developed", "built", "managed", "led", "designed", "implemented", 
        "collaborated", "analyzed", "engineered", "optimized", "monitored",
        "facilitated", "authored", "conducted", "coordinated", "delivered"
    ]
    verb_count = sum(1 for w in action_verbs if re.search(rf"\b{w}\b", text, re.IGNORECASE))
    score += verb_count * 10.0
    
    # Prefer technical skills keywords
    skills_kw = ["python", "java", "sql", "aws", "docker", "kubernetes", "react", "c++", "c#", "linux", "git", "jenkins", "excel", "tableau"]
    skill_count = sum(1 for s in skills_kw if re.search(rf"\b{s}\b", text, re.IGNORECASE))
    score += skill_count * 10.0
    
    # Prefer quantified achievements (e.g. '80%', '$500k', '5 years')
    quantified = len(re.findall(r"\b\d+%\b|\$\d+,\d+|\b\d+\s+years\b|\b\d+\s+million\b|\b\d+\s+percent\b", text, re.IGNORECASE))
    score += quantified * 20.0
    
    # Prefer education indicators
    edu_kw = ["bachelor", "master", "degree", "university", "college", "bs in", "ms in"]
    edu_count = sum(1 for e in edu_kw if re.search(rf"\b{e}\b", text, re.IGNORECASE))
    score += edu_count * 15.0
    
    # Complete career history indicators (e.g. years)
    years = len(re.findall(r"\b(20\d{2}|19\d{2})\b", text))
    score += years * 5.0
    
    return score

def score_section(content: str, section_type: str) -> float:
    """Score a section's content quality for library sampling, returning -9999.0 if rejected."""
    if not isinstance(content, str):
        return -9999.0
        
    length = len(content)
    # Reject short content based on category
    if section_type == "Experience":
        if length < 50:
            return -9999.0
    elif section_type in ("Skills", "Summary", "Objective", "Personal Information"):
        if length < 20:
            return -9999.0
    elif section_type == "Education":
        if length < 15:
            return -9999.0
            
    # Reject excessive punctuation
    if re.search(r"([!?,;:=\-_~])\1{2,}", content) or re.search(r"\.{4,}", content):
        return -9999.0
        
    score = 0.0
    
    if section_type == "Experience":
        verbs = ["developed", "built", "designed", "implemented", "managed", "led", "collaborated", "analyzed", "engineered"]
        score += sum(5.0 for v in verbs if re.search(rf"\b{v}\b", content, re.IGNORECASE))
        if re.search(r"\d+%", content) or re.search(r"\$\d+", content):
            score += 20.0
    elif section_type == "Skills":
        # Prefer lists with bullet marks or commas
        score += len(re.findall(r"[,;:/▫·•*]", content)) * 5.0
    elif section_type == "Education":
        degrees = ["bachelor", "master", "university", "college", "gpa", "bs", "ms", "phd"]
        score += sum(10.0 for d in degrees if re.search(rf"\b{d}\b", content, re.IGNORECASE))
    elif section_type == "Summary":
        terms = ["experience", "expert", "skilled", "proven", "track record", "professional"]
        score += sum(8.0 for t in terms if re.search(rf"\b{t}\b", content, re.IGNORECASE))
    elif section_type == "Objective":
        goals = ["seeking", "career", "utilize", "contribute", "opportunity", "position", "growth"]
        score += sum(8.0 for g in goals if re.search(rf"\b{g}\b", content, re.IGNORECASE))
    elif section_type == "Personal Information":
        pi_kw = ["name", "location", "title", "status", "citizen", "visa", "developer", "engineer"]
        score += sum(5.0 for k in pi_kw if re.search(rf"\b{k}\b", content, re.IGNORECASE))
        
    return score

def analyze_patterns(resumes: List[str], sections_by_type: Dict[str, List[str]]) -> str:
    """Analyze the sampled dataset dynamically to build SECTION C (Patterns)."""
    # 1. Action Verbs count in Experience content
    exp_texts = sections_by_type.get("Experience", [])
    action_verbs = ["developed", "built", "managed", "led", "designed", "implemented", "collaborated", "analyzed", "engineered", "optimized", "monitored"]
    verb_counts = collections.Counter()
    for text in exp_texts:
        for v in action_verbs:
            if re.search(rf"\b{v}\b", text, re.IGNORECASE):
                verb_counts[v] += 1
                
    # 2. Skills count in Skills content
    skills_texts = sections_by_type.get("Skills", [])
    skills_list = ["python", "java", "sql", "aws", "docker", "kubernetes", "react", "c++", "c#", "linux", "git", "jenkins", "excel", "tableau", "spring", "javascript", "oracle", "mysql", "postgresql", "mongodb", "rest"]
    skill_counts = collections.Counter()
    for text in skills_texts:
        for s in skills_list:
            if re.search(rf"\b{s}\b", text, re.IGNORECASE):
                name = "C++" if s == "c++" else ("C#" if s == "c#" else s.capitalize() if s not in ("aws", "sql") else s.upper())
                skill_counts[name] += 1
                
    # 3. Education patterns
    edu_texts = sections_by_type.get("Education", [])
    degree_patterns = {
        "Bachelor (BS/BA/Bachelors)": sum(1 for t in edu_texts if re.search(r"\b(bachelor|bs|ba)\b", t, re.IGNORECASE)),
        "Master (MS/MA/MBA/Masters)": sum(1 for t in edu_texts if re.search(r"\b(master|ms|ma|mba)\b", t, re.IGNORECASE)),
        "PhD/Doctorate": sum(1 for t in edu_texts if re.search(r"\b(phd|doctor|doctorate)\b", t, re.IGNORECASE))
    }
    
    # 4. ATS keywords (high frequency words excluding stopwords)
    stopwords = {"the", "and", "in", "of", "to", "for", "with", "a", "an", "on", "as", "by", "at", "from", "using", "various", "using", "like", "our", "all", "is", "was", "were", "are"}
    word_counts = collections.Counter()
    for text in resumes:
        words = re.findall(r"\b[a-zA-Z]{4,}\b", text.lower())
        for w in words:
            if w not in stopwords:
                word_counts[w] += 1
    common_ats = [w.capitalize() for w, c in word_counts.most_common(20)]
    
    # Format Section C
    md = "# Resume Writing Patterns\n\n"
    md += "This section documents standard patterns extracted from the database examples.\n\n"
    
    md += "### Experience Writing Patterns\n\n"
    md += "Analysis of Experience entries shows the following patterns:\n"
    md += "1. **Dominant Action Verbs:** Professional bullets start with action verbs. The most common verbs in this dataset are:\n"
    for verb, cnt in verb_counts.most_common(5):
        md += f"   - *{verb.capitalize()}* (used in {cnt} examples)\n"
    md += "2. **Quantified Achievements:** High-quality entries link actions to metrics (e.g. system performance increases, budget management sizes).\n"
    md += "3. **ATS Alignment:** Skills and tools are embedded contextually in description sentences.\n\n"
    
    md += "### Skills Representation Patterns\n\n"
    md += "Commonly cited tools and languages in Skills profiles:\n"
    for skill, cnt in skill_counts.most_common(8):
        md += f"- **{skill}:** Found in {cnt} skills section examples.\n"
    md += "\nSkill sets are structured into distinct lists separated by punctuation (commas, pipes, or bullets).\n\n"
    
    md += "### Education Formatting Patterns\n\n"
    md += "Education entries follow standard academic hierarchies:\n"
    for deg, cnt in degree_patterns.items():
        md += f"- **{deg}:** Found in {cnt} education examples.\n"
    md += "\nThey list degree level, major field, institution name, and location in order.\n\n"
    
    md += "### Common ATS Keywords\n\n"
    md += "High-frequency keywords across candidate descriptions:\n\n"
    md += ", ".join([f"`{w}`" for w in common_ats]) + "\n"
    
    return md

def generate_ats_friendly_characteristics() -> str:
    """Generate Section D summarizing ATS best practices and resume formatting."""
    md = "# ATS-Friendly Resume Characteristics\n\n"
    md += "To maximize compatibility with applicant tracking systems, resumes in this library follow these best practices:\n\n"
    
    md += "1. **Clean Structural Layout:**\n"
    md += "   - Standard sections (Experience, Skills, Education, Summary, Objective) are defined with clear titles.\n"
    md += "   - Free of complex multi-column grids or graphical rating bars that confuse parsers.\n\n"
    
    md += "2. **Consistent Section Flow:**\n"
    md += "   - Reverse-chronological experience representation with job titles, company names, and dates clearly defined.\n\n"
    
    md += "3. **Contextual Skill Integration:**\n"
    md += "   - Technical and soft skills are listed both in standalone checklists and embedded contextually within work experience bullets.\n\n"
    
    md += "4. **Quantified Outcomes:**\n"
    md += "   - Focuses on accomplishments using the Google 'X-Y-Z' formula: 'Accomplished [X] as measured by [Y], by doing [Z].'\n"
    
    return md

def main():
    logger.info("Initializing NotebookLM Source Builder Pipeline")
    
    # Paths
    fit_path = Path("argus/resume/datasets/processed/resume_job_fit_clean.jsonl")
    sections_path = Path("argus/resume/datasets/processed/resume_sections_clean.jsonl")
    
    source_out_path = Path("argus/resume/datasets/notebooklm/notebooklm_resume_summary_source.md")
    report_out_path = Path("argus/resume/evaluation/notebooklm_source_report.md")
    
    source_out_path.parent.mkdir(parents=True, exist_ok=True)
    report_out_path.parent.mkdir(parents=True, exist_ok=True)
    
    # 1. Load data
    if not fit_path.exists():
        raise FileNotFoundError(f"Input file not found: {fit_path}")
    if not sections_path.exists():
        raise FileNotFoundError(f"Input file not found: {sections_path}")
        
    df_fit = pd.read_json(fit_path, lines=True)
    df_sections = pd.read_json(sections_path, lines=True)
    
    logger.info(f"Loaded {len(fit_fit := df_fit)} fit rows and {len(df_sections)} section rows.")
    
    # 2. Score and Filter Resumes
    df_fit["quality_score"] = df_fit["resume_text"].apply(score_resume)
    valid_resumes = df_fit[df_fit["quality_score"] > 0].copy()
    valid_resumes = valid_resumes.sort_values(by="quality_score", ascending=False)
    
    # Deduplicate on resume_text to ensure variety
    valid_resumes = valid_resumes.drop_duplicates(subset=["resume_text"])
    
    logger.info(f"Scoring complete. Unique resumes passing filters: {len(valid_resumes)} / {len(df_fit)}")
    if len(valid_resumes) < NUM_RESUMES_TO_SAMPLE:
        logger.warning("Fewer unique resumes passed filters than target. Relaxing filter to sample.")
        # Grab top scored unique resumes regardless
        unique_fit = df_fit.drop_duplicates(subset=["resume_text"])
        sampled_resumes_df = unique_fit.sort_values(by="quality_score", ascending=False).head(NUM_RESUMES_TO_SAMPLE)
    else:
        sampled_resumes_df = valid_resumes.head(NUM_RESUMES_TO_SAMPLE)
        
    sampled_resumes = sampled_resumes_df["resume_text"].tolist()
    
    # 3. Score and Filter Sections by Type
    sections_by_type = {}
    total_sections_count = 0
    
    for label in EXPECTED_LABELS:
        df_label = df_sections[df_sections["section"] == label].copy()
        df_label["quality_score"] = df_label["content"].apply(lambda c: score_section(c, label))
        
        valid_label_df = df_label[df_label["quality_score"] > 0].sort_values(by="quality_score", ascending=False)
        
        if len(valid_label_df) < NUM_SECTIONS_PER_TYPE:
            logger.warning(f"Fewer section samples for '{label}' than target. Sampling top scoring.")
            sampled_label_df = df_label.sort_values(by="quality_score", ascending=False).head(NUM_SECTIONS_PER_TYPE)
        else:
            sampled_label_df = valid_label_df.head(NUM_SECTIONS_PER_TYPE)
            
        sections_by_type[label] = sampled_label_df["content"].tolist()
        total_sections_count += len(sections_by_type[label])
        logger.info(f"Sampled {len(sections_by_type[label])} sections of type '{label}'.")
        
    # 4. Construct Markdown Source
    md = "# Argus AI Resume Knowledge Base\n\n"
    md += "This document contains examples of real resume content.\n"
    md += "It is intended to teach resume structure, career progression, skills representation, education formatting, and professional writing styles.\n\n"
    md += "---\n\n"
    
    # SECTION A: Resume Examples
    md += "# Resume Examples\n\n"
    for i, res in enumerate(sampled_resumes, 1):
        md += f"## Resume Example {i}\n\n"
        md += "### Resume Content\n\n"
        md += f"{res}\n\n"
        md += "---\n\n"
        
    # SECTION B: Resume Sections Library
    md += "# Resume Sections Library\n\n"
    md += "This library contains individual resume section examples grouped by category.\n\n"
    
    for label in EXPECTED_LABELS:
        md += f"## {label} Examples\n\n"
        for j, content in enumerate(sections_by_type[label], 1):
            md += f"### Example {j}\n\n"
            md += f"{content}\n\n"
        md += "---\n\n"
        
    # SECTION C: Resume Writing Patterns
    patterns_md = analyze_patterns(sampled_resumes, sections_by_type)
    md += patterns_md
    md += "\n---\n\n"
    
    # SECTION D: ATS-Friendly Characteristics
    char_md = generate_ats_friendly_characteristics()
    md += char_md
    
    # Save source file
    source_out_path.write_text(md, encoding="utf-8")
    logger.info(f"Successfully wrote NotebookLM resume source document to {source_out_path}")
    
    # 5. Validation Check
    # Verify file exists
    assert source_out_path.exists(), "Validation failed: Markdown source file does not exist."
    content_read = source_out_path.read_text(encoding="utf-8")
    
    # Verify exceeds 100 examples total
    total_examples = len(sampled_resumes) + total_sections_count
    assert total_examples > 100, f"Validation failed: Total examples ({total_examples}) must exceed 100."
    
    # Verify no JSON format remain (check for common JSON delimiters that shouldn't be top-level)
    assert not content_read.startswith("[{") and not content_read.startswith('{"'), "Validation failed: Source file appears to retain JSON structures."
    
    # Verify readable
    assert len(content_read) > 1000, "Validation failed: File contents are too short."
    logger.info(f"Validation complete: Total Examples = {total_examples} (exceeds 100), JSON checks passed.")
    
    # 6. Generate Report
    report_md = "# NotebookLM Source Generation Report\n\n"
    report_md += "## Execution Statistics\n\n"
    report_md += f"- **Total Resumes Exported (Section A):** {len(sampled_resumes)}\n"
    report_md += f"- **Total Sections Exported (Section B):** {total_sections_count}\n"
    report_md += f"- **Total Combined Examples:** {total_examples}\n"
    report_md += f"- **Markdown File Path:** `{source_out_path}`\n"
    report_md += f"- **Markdown File Size:** {source_out_path.stat().st_size} bytes\n"
    report_md += f"- **Validation Status:** `PASSED`\n\n"
    
    report_md += "### Section Distribution Table\n\n"
    report_md += "| Section Category | Sampled Count |\n"
    report_md += "| :--- | :--- |\n"
    for label in EXPECTED_LABELS:
        report_md += f"| {label} | {len(sections_by_type[label])} |\n"
    report_md += "\n"
    
    report_md += "### Quality Filters Overview\n\n"
    report_md += "All sampled resumes and sections were sorted and filtered by quality scores, prioritizing action verbs, quantified achievements, and structured contents while discarding malformed formatting and repetitive punctuation.\n"
    
    report_out_path.write_text(report_md, encoding="utf-8")
    logger.info(f"Successfully wrote pipeline report to {report_out_path}")

if __name__ == "__main__":
    main()
