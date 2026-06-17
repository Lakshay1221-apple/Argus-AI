import json
import logging
from argus.resume.api.model_loader import loader
from argus.resume.api.prompts import REVIEW_INSTRUCTION
from argus.resume.api.utils.json_repair import repair_json

logger = logging.getLogger("ReviewService")

def review_resume(resume_text: str) -> dict:
    """
    Analyzes the resume for ATS score, strengths, weaknesses, and suggestions.
    """
    raw_response = loader.generate_response(
        instruction=REVIEW_INSTRUCTION,
        input_text=resume_text,
        max_new_tokens=512
    )

    try:
        # Try direct JSON load
        return json.loads(raw_response.strip())
    except json.JSONDecodeError:
        logger.warning("Direct JSON decode failed. Attempting to repair malformed JSON...")
        try:
            return repair_json(raw_response)
        except Exception as e:
            logger.error(f"Failed to repair JSON: {e}")
            # Fallback structure if parsing is totally broken
            return {
                "ats_score": 60,
                "strengths": ["Review completed, check raw logs for details."],
                "weaknesses": ["Model generated unstructured output."],
                "suggestions": ["Verify resume formatting and key sections are standard."],
                "verdict": "Potential Fit"
            }
