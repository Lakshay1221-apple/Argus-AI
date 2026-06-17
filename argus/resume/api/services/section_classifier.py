from argus.resume.api.model_loader import loader
from argus.resume.api.prompts import CLASSIFY_SECTION_INSTRUCTION

def classify_section(section_text: str) -> str:
    """
    Classifies a resume section (e.g. Work Experience, Education, Skills).
    """
    response = loader.generate_response(
        instruction=CLASSIFY_SECTION_INSTRUCTION,
        input_text=section_text,
        max_new_tokens=20
    )
    return response.strip()
