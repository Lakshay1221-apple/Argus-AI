from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

# Health Response
class GPUStats(BaseModel):
    allocated_mb: float
    reserved_mb: float
    max_allocated_mb: float
    total_system_gpu_mb: float
    used_system_gpu_mb: float

class HealthResponse(BaseModel):
    status: str = "ok"
    gpu_stats: Optional[GPUStats] = None

# Resume Summary
class SummaryRequest(BaseModel):
    resume_text: str = Field(..., description="The full plain text of the candidate's resume.")

class SummaryResponse(BaseModel):
    summary: str = Field(..., description="The generated professional summary.")

# ATS Review
class ReviewRequest(BaseModel):
    resume_text: str = Field(..., description="The full plain text of the resume to review.")

class ReviewResponse(BaseModel):
    ats_score: int = Field(..., description="ATS score out of 100.")
    strengths: List[str] = Field(..., description="Key strengths identified in the resume.")
    weaknesses: List[str] = Field(..., description="Key weaknesses identified in the resume.")
    suggestions: List[str] = Field(..., description="Actionable improvement suggestions.")
    verdict: str = Field(..., description="Overall verdict (e.g. Strong Fit, Potential Fit, Weak Fit).")

# Section Classification
class ClassifySectionRequest(BaseModel):
    section_text: str = Field(..., description="Text content from a specific resume section.")

class ClassifySectionResponse(BaseModel):
    label: str = Field(..., description="Predicted section class label (e.g., Skills, Experience, Education, etc.).")

# Job Fit
class JobFitRequest(BaseModel):
    resume_text: str = Field(..., description="The candidate's resume text.")
    job_description: str = Field(..., description="The job description text to match against.")

class JobFitResponse(BaseModel):
    fit: str = Field(..., description="Candidate fit classification (e.g., Fit, Partial Fit, No Fit).")
