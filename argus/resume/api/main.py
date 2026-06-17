import time
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("ResumeAPI")

from argus.resume.api.model_loader import loader
from argus.resume.api.utils.gpu_info import get_gpu_memory_usage
from argus.resume.api.schemas import (
    HealthResponse,
    SummaryRequest, SummaryResponse,
    ReviewRequest, ReviewResponse,
    ClassifySectionRequest, ClassifySectionResponse,
    JobFitRequest, JobFitResponse
)
from argus.resume.api.services.summary import generate_summary
from argus.resume.api.services.review import review_resume
from argus.resume.api.services.section_classifier import classify_section
from argus.resume.api.services.job_fit import determine_job_fit

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting API server, loading Resume Adapter...")
    try:
        loader.load_model()
    except Exception as e:
        logger.error(f"Failed to load model during startup: {e}")
    yield
    # Shutdown
    logger.info("Shutting down API server...")
    import torch
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

# Swagger docs at /api/docs and OpenAPI spec at /api/openapi.json
app = FastAPI(
    title="Resume Adapter API",
    description="Local inference server for Resume Adapter V2 model",
    version="1.0.0",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    lifespan=lifespan
)

# CORS middleware to support Next.js local integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request logging & Response timing & GPU memory display middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.perf_counter()
    gpu_before = get_gpu_memory_usage()

    response = await call_next(request)

    process_time = (time.perf_counter() - start_time) * 1000.0  # in ms
    gpu_after = get_gpu_memory_usage()

    # Inject performance headers
    response.headers["X-Response-Time-Ms"] = f"{process_time:.2f}"
    response.headers["X-GPU-Memory-Allocated-MB"] = f"{gpu_after['allocated_mb']:.2f}"
    response.headers["X-GPU-Memory-Total-System-MB"] = f"{gpu_after['total_system_gpu_mb']:.2f}"

    logger.info(
        f"Path: {request.url.path} | Method: {request.method} | "
        f"Status: {response.status_code} | Time: {process_time:.2f}ms | "
        f"GPU Alloc: {gpu_after['allocated_mb']}MB (was {gpu_before['allocated_mb']}MB)"
    )
    return response

# GET /health
@app.get("/health", response_model=HealthResponse)
def health_check():
    """
    Server status checks including live GPU utilization.
    """
    gpu = get_gpu_memory_usage()
    return HealthResponse(status="ok", gpu_stats=gpu)

# POST /summary
@app.post("/summary", response_model=SummaryResponse)
def resume_summary(req: SummaryRequest):
    """
    Generates a professional resume summary.
    """
    try:
        summary_text = generate_summary(req.resume_text)
        return SummaryResponse(summary=summary_text)
    except Exception as e:
        logger.error(f"Error in summary generation: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# POST /review
@app.post("/review", response_model=ReviewResponse)
def ats_review(req: ReviewRequest):
    """
    Performs ATS Review, providing score, strengths, weaknesses, and suggestions.
    """
    try:
        review_result = review_resume(req.resume_text)
        return ReviewResponse(
            ats_score=review_result.get("ats_score", 70),
            strengths=review_result.get("strengths", []),
            weaknesses=review_result.get("weaknesses", []),
            suggestions=review_result.get("suggestions", []),
            verdict=review_result.get("verdict", "Potential Fit")
        )
    except Exception as e:
        logger.error(f"Error in ATS Review: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# POST /classify-section
@app.post("/classify-section", response_model=ClassifySectionResponse)
def classify_resume_section(req: ClassifySectionRequest):
    """
    Classifies a resume section label (e.g. Work Experience, Education).
    """
    try:
        label = classify_section(req.section_text)
        return ClassifySectionResponse(label=label)
    except Exception as e:
        logger.error(f"Error in Section Classification: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# POST /job-fit
@app.post("/job-fit", response_model=JobFitResponse)
def resume_job_fit(req: JobFitRequest):
    """
    Analyzes and determines fit between resume and job description.
    """
    try:
        fit = determine_job_fit(req.resume_text, req.job_description)
        return JobFitResponse(fit=fit)
    except Exception as e:
        logger.error(f"Error in Job Fit determination: {e}")
        raise HTTPException(status_code=500, detail=str(e))
