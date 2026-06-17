# Argus Resume Adapter Local Testing Stack

This directory contains the local testing stack for evaluating the **Resume Adapter V2** (fine-tuned from `unsloth/Llama-3.2-1B-Instruct-bnb-4bit`).

The testing stack consists of:
1. **FastAPI Backend** (Model Inference Service with GPU/VRAM monitoring and custom JSON repair).
2. **Next.js Frontend Dashboard** (Interactive task runner and batch evaluation benchmark dashboard).

---

## 📂 Project Structure

```text
argus/resume/
├── README.md               # This documentation
├── adapter/
│   └── resume_adapter_v2/  # Model adapter files
├── models/
│   └── resume_adapter_v2_final -> ../adapter/resume_adapter_v2
├── api/                    # FastAPI backend codebase
│   ├── main.py             # Server router and middleware
│   ├── model_loader.py     # Model loading (Unsloth/Transformers)
│   ├── prompts.py          # Prompt management layer
│   ├── schemas.py          # Pydantic schemas
│   ├── services/           # Business logic modules
│   │   ├── summary.py
│   │   ├── review.py
│   │   ├── section_classifier.py
│   │   └── job_fit.py
│   └── utils/              # Heuristic JSON repairs & GPU info
│       ├── json_repair.py
│       └── gpu_info.py
└── frontend/               # Next.js typescript React client
```

---

## 🛠️ Installation & Setup

Ensure you are using the project's virtual environment or have matching versions of PyTorch and CUDA configured.

### 1. Install Backend Dependencies
Run the following from the root workspace directory to install FastAPI and Uvicorn:
```bash
uv pip install fastapi uvicorn
```
*(Note: standard model libraries like `torch`, `transformers`, `peft`, `bitsandbytes` are assumed to be pre-installed in the workspace).*

### 2. Setup Frontend dependencies
Initialize package installs in the frontend folder:
```bash
cd argus/resume/frontend
npm install
```

---

## 🚀 Running the Services

### 1. Run the FastAPI Backend
Start the backend using Uvicorn from the root workspace:
```bash
.venv/bin/python -m uvicorn argus.resume.api.main:app --port 8000 --reload
```
Once started:
* The OpenAPI spec will be available at: `http://localhost:8000/api/openapi.json`
* The Swagger docs will be interactive at: `http://localhost:8000/api/docs`

### 2. Run the Next.js Frontend
Start the local Next.js server:
```bash
cd argus/resume/frontend
npm run dev
```
Open `http://localhost:3000` in your browser to view the testing dashboard.

---

## 🧪 Testing the API

### Automated Testing
We have provided a comprehensive mock unit testing suite to verify endpoints and validation logic without requiring GPU resources:
```bash
.venv/bin/python -m unittest tests/test_api.py
```

---

## 📖 API Endpoints & Request Examples

### 1. Health Check
* **Route:** `GET /health`
* **Response Example:**
  ```json
  {
    "status": "ok",
    "gpu_stats": {
      "allocated_mb": 1280.45,
      "reserved_mb": 1820.00,
      "max_allocated_mb": 2048.20,
      "total_system_gpu_mb": 4096.00,
      "used_system_gpu_mb": 1500.00
    }
  }
  ```

### 2. Resume Summary
* **Route:** `POST /summary`
* **Request:**
  ```json
  {
    "resume_text": "Experienced Python developer with 5 years writing FastAPI web servers."
  }
  ```
* **Response:**
  ```json
  {
    "summary": "Professional Python software engineer specializing in backend RESTful APIs using FastAPI."
  }
  ```

### 3. ATS Resume Review
* **Route:** `POST /review`
* **Request:**
  ```json
  {
    "resume_text": "John Doe... worked at Acme Corp... managed inventory..."
  }
  ```
* **Response:**
  ```json
  {
    "ats_score": 85,
    "strengths": ["Clear section formatting", "Clean presentation of roles"],
    "weaknesses": ["Lack of quantifiable key performance metrics"],
    "suggestions": ["Include percentages and dollar metrics in Acme Corp role achievements."],
    "verdict": "Potential Fit"
  }
  ```

### 4. Resume Section Classification
* **Route:** `POST /classify-section`
* **Request:**
  ```json
  {
    "section_text": "Python, JavaScript, React, Go, Docker, Kubernetes"
  }
  ```
* **Response:**
  ```json
  {
    "label": "Skills"
  }
  ```

### 5. Job Fit
* **Route:** `POST /job-fit`
* **Request:**
  ```json
  {
    "resume_text": "Fullstack web developer with 3 years React and Node experience.",
    "job_description": "We are seeking a React Developer who knows TypeScript and CSS styling."
  }
  ```
* **Response:**
  ```json
  {
    "fit": "Fit"
  }
  ```
