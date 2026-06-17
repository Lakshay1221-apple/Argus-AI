from argus.resume.api.model_loader import loader
from argus.resume.api.prompts import JOB_FIT_INSTRUCTION, format_job_fit_input

def determine_job_fit(resume_text: str, job_description: str) -> str:
    """
    Determines the fit between a candidate resume and job description.
    """
    formatted_input = format_job_fit_input(resume_text, job_description)
    response = loader.generate_response(
        instruction=JOB_FIT_INSTRUCTION,
        input_text=formatted_input,
        max_new_tokens=20
    )
    return response.strip()
