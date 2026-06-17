import json
import re
import logging

logger = logging.getLogger("JSONRepair")

def repair_json(json_str: str) -> dict:
    """
    Attempts to repair and parse a potentially malformed JSON string from the LLM.
    """
    # 1. Clean whitespace and extract markdown JSON code blocks
    cleaned = json_str.strip()
    if "```" in cleaned:
        # Extract content between code fences
        match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", cleaned)
        if match:
            cleaned = match.group(1).strip()

    # 2. Try standard parsing
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    # 3. Find first '{' and last '}' to handle leading/trailing conversational text
    start_idx = cleaned.find('{')
    end_idx = cleaned.rfind('}')
    if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
        cleaned = cleaned[start_idx:end_idx+1]
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            pass

    # 4. Apply heuristic repairs for common syntax issues
    repaired = cleaned
    try:
        # Replace python-like booleans and None
        repaired = re.sub(r'\bTrue\b', 'true', repaired)
        repaired = re.sub(r'\bFalse\b', 'false', repaired)
        repaired = re.sub(r'\bNone\b', 'null', repaired)

        # Replace trailing commas before closing braces/brackets
        repaired = re.sub(r',\s*\}', '}', repaired)
        repaired = re.sub(r',\s*\]', ']', repaired)

        # Try parsing again
        try:
            return json.loads(repaired)
        except json.JSONDecodeError:
            pass

        # 5. Schema-specific regex extraction as a final fallback for ATS Review
        parsed = {}

        # Extract ats_score (integer)
        score_match = re.search(r'"ats_score"\s*:\s*(\d+)', repaired)
        if score_match:
            parsed["ats_score"] = int(score_match.group(1))
        else:
            score_match = re.search(r'ats_score\s*:\s*(\d+)', repaired)
            if score_match:
                parsed["ats_score"] = int(score_match.group(1))
            else:
                parsed["ats_score"] = 70  # Reasonable default

        # Extract verdict
        verdict_match = re.search(r'"verdict"\s*:\s*"([^"]+)"', repaired)
        if verdict_match:
            parsed["verdict"] = verdict_match.group(1)
        else:
            verdict_match = re.search(r'verdict\s*:\s*["\']?([^"\',\s\}]+)["\']?', repaired)
            parsed["verdict"] = verdict_match.group(1) if verdict_match else "Potential Fit"

        # Extract lists (strengths, weaknesses, suggestions)
        for field in ["strengths", "weaknesses", "suggestions"]:
            list_match = re.search(rf'"{field}"\s*:\s*\[([\s\S]*?)\]', repaired)
            if not list_match:
                list_match = re.search(rf'{field}\s*:\s*\[([\s\S]*?)\]', repaired)

            if list_match:
                items_str = list_match.group(1)
                items = re.findall(r'"([^"]*)"', items_str)
                if not items:
                    items = re.findall(r"'([^']*)'", items_str)
                parsed[field] = [it.strip() for it in items if it.strip()]
            else:
                parsed[field] = []

        if parsed.get("ats_score") is not None:
            logger.info("Successfully extracted partial fields using heuristic regex.")
            return parsed

    except Exception as e:
        logger.error(f"Heuristic JSON repair failed: {e}")

    # Return a structured error response if everything fails
    raise ValueError(f"Failed to parse or repair JSON from output: {json_str[:200]}...")
