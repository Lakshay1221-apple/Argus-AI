import json
import re
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("Sanitizer")

def clean_unicode_replacement_char(text: str) -> str:
    if not isinstance(text, str):
        return text
    
    # Specific known names/words
    text = text.replace("Andr\uFFFDs Bello", "Andrés Bello")
    text = text.replace("Andr\uFFFDs", "Andrés")
    text = text.replace("Travellers\uFFFD", "Travellers'")
    
    # Apostrophes / contractions
    text = re.sub(r"(\w)\uFFFDs\b", r"\1's", text)
    text = re.sub(r"(\w)\uFFFDt\b", r"\1't", text)
    text = re.sub(r"(\w)\uFFFDd\b", r"\1'd", text)
    text = re.sub(r"(\w)\uFFFDll\b", r"\1'll", text)
    text = re.sub(r"(\w)\uFFFDeve\b", r"\1've", text)
    text = re.sub(r"(\w)\uFFFDre\b", r"\1're", text)
    
    # Hyphens or quotes in dates/ranges
    text = re.sub(r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\uFFFD(\d{2})\b", r"\1-\2", text)
    
    # General word boundary replacements (like words or Fathers)
    text = text.replace("Father\uFFFDs", "Father's")
    text = text.replace("P.S.G.V.P.M\uFFFDs", "P.S.G.V.P.M's")
    
    # Words
    text = re.sub(r"(\w)\uFFFD(\w)", r"\1'\2", text)
    
    # E.g. Current -> 'Current
    text = re.sub(r"\uFFFD(\w)", r"'\1", text)
    # E.g. Pharmacology -> Pharmacology'
    text = re.sub(r"(\w)\uFFFD", r"\1'", text)
    
    # E.g.  MS-CIT -> * MS-CIT (at start of line)
    text = re.sub(r"^\uFFFD\s*", "* ", text, flags=re.MULTILINE)
    
    # Remove any remaining consecutive \uFFFD characters
    text = re.sub(r"\uFFFD+", "", text)
    
    return text

def sanitize_record(obj: Any) -> Any:
    if isinstance(obj, str):
        return clean_unicode_replacement_char(obj)
    elif isinstance(obj, dict):
        return {k: sanitize_record(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [sanitize_record(v) for v in obj]
    return obj

def main():
    datasets = [
        "argus/resume/datasets/processed/resume_job_fit_training_ready.jsonl",
        "argus/resume/datasets/processed/resume_sections_clean.jsonl",
        "argus/resume/datasets/processed/resume_sections_instruction.jsonl",
        "argus/resume/datasets/processed/resume_summary_synthetic.jsonl",
        "argus/resume/datasets/processed/resume_review_synthetic_v1.jsonl",
    ]
    
    for path_str in datasets:
        p = Path(path_str)
        if not p.exists():
            logger.warning(f"File not found: {path_str}")
            continue
            
        logger.info(f"Sanitizing {p.name}...")
        
        # Read content
        with open(p, "rb") as f:
            raw_bytes = f.read()
        content = raw_bytes.decode("utf-8").strip()
        
        # Determine format (array or lines)
        # Check if it starts with "[" (JSON Array)
        is_array = content.startswith("[")
        
        # Flexible Parsing to load all records
        records = []
        if is_array:
            try:
                records = json.loads(content)
            except json.JSONDecodeError:
                pass
                
        if not records:
            # Try parsing as JSON lines
            lines = content.splitlines()
            is_json_lines = True
            for line in lines:
                if not line.strip():
                    continue
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    is_json_lines = False
                    break
                    
            if not is_json_lines or not records:
                # Concatenated arrays/objects
                decoder = json.JSONDecoder()
                pos = 0
                records = []
                while pos < len(content):
                    while pos < len(content) and content[pos].isspace():
                        pos += 1
                    if pos >= len(content):
                        break
                    try:
                        obj, next_pos = decoder.raw_decode(content, pos)
                        if isinstance(obj, list):
                            records.extend(obj)
                        else:
                            records.append(obj)
                        pos = next_pos
                    except json.JSONDecodeError as e:
                        logger.error(f"Error parsing concatenated JSON at {pos}: {e}")
                        break
                        
        logger.info(f"Loaded {len(records)} records. Sanitizing...")
        
        sanitized_records = [sanitize_record(r) for r in records]
        
        # Write back in same format
        if is_array:
            with open(p, "w", encoding="utf-8") as f:
                json.dump(sanitized_records, f, indent=2, ensure_ascii=False)
        else:
            with open(p, "w", encoding="utf-8") as f:
                for r in sanitized_records:
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
                    
        logger.info(f"Finished sanitizing {p.name}")

if __name__ == "__main__":
    from typing import Any
    main()
