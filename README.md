# 🏛️ Argus AI

### *The All-Seeing Career Copilot*

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/0c80dc67-e014-4029-bcf9-d750f78a01dc" />


Argus AI is a multi-adapter Large Language Model (LLM) system designed to help aspiring software engineers and machine learning practitioners improve their professional readiness through AI-powered career guidance.

Built using **Hugging Face Transformers**, **PEFT**, **QLoRA**, and **LoRA**, Argus AI provides three specialized capabilities:

* 📄 Resume Review Assistant
* 💻 Code Review Assistant
* 🎤 Technical Interview Assistant

Instead of training multiple full-sized models, Argus AI leverages a shared base model with specialized LoRA adapters, enabling efficient task-specific behavior while minimizing memory and compute requirements.

---

# 🚀 Project Vision

Preparing for software engineering and machine learning careers often requires juggling multiple tools:

* Resume analyzers
* Code review platforms
* Interview preparation resources

Argus AI unifies these capabilities into a single intelligent system capable of evaluating resumes, reviewing code, and conducting technical interviews.

The long-term goal is to create an AI mentor that guides developers throughout their career journey.

---

# ✨ Features

## 📄 Resume Review Assistant

Analyze resumes and provide actionable feedback.

### Capabilities

* Resume scoring
* Strength identification
* Weakness detection
* ATS optimization suggestions
* Missing skill analysis
* Improvement recommendations

### Example Output

```text
Resume Score: 82/100

Strengths:
- Strong Python foundation
- Multiple machine learning projects

Weaknesses:
- No quantified achievements
- Limited internship experience

Suggestions:
- Add project metrics
- Include GitHub portfolio links
```

---

## 💻 Code Review Assistant

Acts as a senior software engineer reviewing submitted code.

### Capabilities

* Bug detection
* Complexity analysis
* Performance optimization
* Best practice recommendations
* Refactoring suggestions

### Example Output

```text
Complexity: O(n²)

Issues:
- Nested loops reduce scalability
- Missing edge-case handling

Suggestions:
- Use a hash map
- Add input validation
```

---

## 🎤 Technical Interview Assistant

Conducts realistic mock interviews for technical roles.

### Supported Roles

* Software Engineer
* Machine Learning Engineer
* Frontend Developer
* Backend Developer
* Data Scientist

### Capabilities

* Interview question generation
* Answer evaluation
* Follow-up questioning
* Personalized feedback

### Example Output

```text
Question:
Explain gradient descent.

Evaluation:
7.5/10

Feedback:
Good understanding of optimization.
Missing discussion of learning rate effects.

Follow-Up:
How does stochastic gradient descent differ?
```

---

# 🧠 Architecture

Argus AI follows a Multi-Adapter PEFT Architecture.

```text
                    ┌──────────────────┐
                    │   Base Model     │
                    │ Llama 3.2 1B     │
                    └────────┬─────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼

 ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
 │ Resume      │     │ Code Review │     │ Interview   │
 │ Adapter     │     │ Adapter     │     │ Adapter     │
 └─────────────┘     └─────────────┘     └─────────────┘
```

Each adapter is trained independently and activated depending on the selected task.

This approach provides:

* Lower memory usage
* Faster experimentation
* Reduced training cost
* Better task specialization
* Minimal task interference

---

# 🏗️ Technology Stack

## LLM & Fine-Tuning

* Hugging Face Transformers
* PEFT
* LoRA
* QLoRA
* TRL
* SFTTrainer

## Data Processing

* Datasets
* Tokenizers
* Pandas

## Infrastructure

* PyTorch
* BitsAndBytes
* Accelerate

## Future Integrations

* ChromaDB
* RAG Pipelines
* FastAPI
* Next.js
* PostgreSQL

---

# 📚 Training Pipeline

```text
Raw Dataset
     │
     ▼
Data Cleaning
     │
     ▼
Formatting
     │
     ▼
Tokenization
     │
     ▼
QLoRA Fine-Tuning
     │
     ▼
LoRA Adapter
     │
     ▼
Evaluation
     │
     ▼
Deployment
```

---

# 🗂️ Project Structure

```text
Argus-AI/

├── adapters/
│   ├── resume_adapter/
│   ├── code_adapter/
│   └── interview_adapter/
│
├── backend/
│
├── configs/
│   ├── model_config.yaml
│   ├── lora_config.yaml
│   └── training_config.yaml
│
├── datasets/
│   ├── resume/
│   │   ├── raw/
│   │   └── processed/
│   │
│   ├── interview/
│   │   ├── raw/
│   │   └── processed/
│   │
│   └── code_review/
│       ├── raw/
│       └── processed/
│
├── docs/
│
├── evaluation/
│
├── frontend/
│
├── logs/
│
├── notebooks/
│
├── outputs/
│
├── scripts/
│   ├── clean_resume.py
│   ├── clean_interview.py
│   ├── clean_code.py
│   └── dataset_validation.py
│
├── tests/
│
├── training/
│   ├── train_resume.py
│   ├── train_code.py
│   └── train_interview.py
│
├── README.md
├── pyproject.toml
└── uv.lock

---
```

# 🎯 Learning Objectives

This project is designed to provide practical experience with:

* Transformer Architectures
* Instruction Fine-Tuning
* PEFT
* LoRA
* QLoRA
* Dataset Engineering
* Model Evaluation
* Multi-Adapter Systems
* LLM Deployment
* Retrieval-Augmented Generation (Future)

---

# 📈 Roadmap

## Phase 1

* Resume Review Adapter

## Phase 2

* Code Review Adapter

## Phase 3

* Interview Assistant Adapter

## Phase 4

* Multi-Adapter Inference System

## Phase 5

* Frontend Dashboard

## Phase 6

* RAG Integration with ChromaDB

## Phase 7

* Personalized Career Coaching

---

# 🏆 Success Metrics

### Resume Module

* Accurate feedback generation
* Useful improvement suggestions

### Code **Module**

* Bug detection accuracy
* Optimization recommendation quality

### Interview Module

* Realistic questioning
* Helpful evaluations

### System

* Low memory footprint
* Fast adapter switching
* Sub-5-second response times

---

# 🔮 Future Vision

Argus AI will evolve beyond a career assistant into a complete AI-powered engineering mentor capable of:

* Reviewing resumes
* Analyzing GitHub repositories
* Generating personalized learning roadmaps
* Conducting company-specific mock interviews
* Leveraging Retrieval-Augmented Generation (RAG) for domain-specific expertise

---

# 📜 Inspiration

Named after **Argus Panoptes**, the all-seeing guardian from Greek mythology.

Just as Argus watched over everything with a hundred eyes, Argus AI helps developers identify blind spots in their resumes, code, and interview preparation.

---

## "Observe. Evaluate. Improve."

### Argus AI — The All-Seeing Career Copilot
