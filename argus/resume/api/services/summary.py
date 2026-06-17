from argus.resume.api.model_loader import loader
from argus.resume.api.prompts import SUMMARY_INSTRUCTION

def generate_summary(resume_text: str) -> str:
    """
    Generates a professional resume summary using the adapter.
    """
    return loader.generate_response(
        instruction=SUMMARY_INSTRUCTION,
        input_text=resume_text,
        max_new_tokens=250
    )
