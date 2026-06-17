# Prompt templates and instructions standardized for the Resume Adapter V2.

PROMPT_TEMPLATE = (
    "<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\n"
    "{instruction}\n\n"
    "Input:\n"
    "{input}\n\n"
    "<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
    "Output:\n"
)

# Task Instructions
SUMMARY_INSTRUCTION = "Generate a professional resume summary."
REVIEW_INSTRUCTION = "Review this resume and provide ATS feedback."
CLASSIFY_SECTION_INSTRUCTION = "Classify the resume section."
JOB_FIT_INSTRUCTION = "Determine the fit between the resume and job description."

def format_prompt(instruction: str, input_text: str) -> str:
    """
    Formats the prompt exactly matching the fine-tuning instruction format.
    """
    return PROMPT_TEMPLATE.format(instruction=instruction, input=input_text)

def format_job_fit_input(resume_text: str, job_description: str) -> str:
    """
    Formats the input specifically for the job fit evaluation task.
    """
    return f"Resume:\n{resume_text}\n\nJob Description:\n{job_description}"
