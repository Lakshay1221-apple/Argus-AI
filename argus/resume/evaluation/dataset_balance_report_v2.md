# Dataset Balance & Training Risk Report V2

Generated on: 2026-06-16 14:42:44
Tokenizer Model: `unsloth/Llama-3.2-1B-Instruct`

This report analyzes the distribution of row counts, token volume contributions, sequence lengths, and associated training risks across the four prepared datasets for the Argus AI Resume Adapter fine-tuning.

---

## 📊 Dataset Counts

The following table summarizes the raw sample sizes (row counts) for each of the target training datasets:

| Dataset Name | Filename | Row Count | Percentage Contribution |
| :--- | :--- | :--- | :--- |
| **Resume Sections Instruction** | `resume_sections_instruction.jsonl` | 59,670 | 88.94% |
| **Resume Job Fit** | `resume_job_fit_training_ready.jsonl` | 6,217 | 9.27% |
| **Resume Summary Synthetic** | `resume_summary_synthetic.jsonl` | 418 | 0.62% |
| **Resume Review Synthetic** | `resume_review_synthetic_v1.jsonl` | 784 | 1.17% |
| **Total Combined** | - | **67,089** | **100.00%** |

---

## 🪙 Token Contribution

Analyzing datasets purely by row count can be misleading. Below is the breakdown of actual token contributions, showing that sequence lengths dictate the real volume of information presented to the model during training.

| Dataset Name | Filename | Combined Tokens | Input (Prompt) Tokens | Output (Response) Tokens | Token Contribution % | Mean Record Tokens | Min/Max Record Tokens |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Resume Sections Instruction** | `resume_sections_instruction.jsonl` | 1,270,112 | 1,201,953 | 68,159 | 11.44% | 21.3 | 8 / 401 |
| **Resume Job Fit** | `resume_job_fit_training_ready.jsonl` | 9,673,035 | 9,662,143 | 10,892 | 87.16% | 1555.9 | 287 / 5,074 |
| **Resume Summary Synthetic** | `resume_summary_synthetic.jsonl` | 62,744 | 40,990 | 21,808 | 0.57% | 150.1 | 59 / 441 |
| **Resume Review Synthetic** | `resume_review_synthetic_v1.jsonl` | 91,988 | 27,047 | 64,941 | 0.83% | 117.3 | 74 / 202 |
| **Total Combined** | - | **11,097,879** | **-** | **-** | **100.00%** | **-** | **-** |

---

## 📈 Detailed Token Profiles

A detailed profile of token sizes for each dataset, splitting combined, input, and output token distributions.

### 📊 Resume Sections Instruction

| Context | Min | Max | Mean | Median | P95 | P99 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Combined** | 8 | 401 | 21.3 | 18.0 | 43.0 | 79.3 |
| **Input** | 7 | 400 | 20.1 | 17.0 | 42.0 | 78.3 |
| **Output** | 1 | 2 | 1.1 | 1.0 | 2.0 | 2.0 |

### 📊 Resume Job Fit

| Context | Min | Max | Mean | Median | P95 | P99 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Combined** | 287 | 5,074 | 1555.9 | 1437.0 | 2837.4 | 3623.7 |
| **Input** | 285 | 5,072 | 1554.1 | 1435.0 | 2835.4 | 3621.7 |
| **Output** | 1 | 2 | 1.8 | 2.0 | 2.0 | 2.0 |

### 📊 Resume Summary Synthetic

| Context | Min | Max | Mean | Median | P95 | P99 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Combined** | 59 | 441 | 150.1 | 74.0 | 378.0 | 398.8 |
| **Input** | 42 | 297 | 98.1 | 56.0 | 240.1 | 261.0 |
| **Output** | 13 | 151 | 52.2 | 19.0 | 140.0 | 144.8 |

### 📊 Resume Review Synthetic

| Context | Min | Max | Mean | Median | P95 | P99 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Combined** | 74 | 202 | 117.3 | 116.0 | 168.0 | 186.0 |
| **Input** | 14 | 96 | 34.5 | 27.0 | 77.0 | 86.2 |
| **Output** | 58 | 117 | 82.8 | 86.0 | 104.0 | 109.0 |


---

## ⚠️ Training Risk Analysis

An analysis of row and token distributions reveals significant structural skew in the combined training dataset:

### 1. Dominant Datasets
- **By Row Count:** **Resume Sections Instruction** is heavily dominant, representing **88.94%** of all rows in the raw mixture. If trained directly, the gradient updates will be overwhelmingly dominated by section classification records, potentially leading to overfitting on prefix matching and layout identification.
- **By Token Volume:** **Resume Job Fit** is overwhelmingly dominant, representing **87.16%** of the total token count. Because job descriptions and full resumes are highly detailed, each row contains thousands of tokens. Consequently, the attention maps and loss gradients will be heavily skewed toward matching resumes with job descriptions, making the other tasks secondary.

### 2. Underrepresented Datasets
- **Resume Summary Synthetic** (representing **0.62%** of rows) and **Resume Review Synthetic** (representing **1.17%** of rows) are underrepresented in terms of volume.
- In a joint fine-tuning regime, a contribution of less than 1-2% can cause the model to treat these tasks as noise, leading to **Catastrophic Forgetting** or failure to master summary synthesis and qualitative resume feedback formatting.

### 3. Training Skew Risks
- **Gradient Domain Bias:** During training backpropagation, the loss computed on long Job Fit sequences will dwarf the signal from short classification and summary tasks, creating a model that evaluates job fit well but performs poorly on structured text generation.
- **Task Neglect:** Without balancing, the adapter will fail to learn the instruction formatting for summarizing or reviewing resumes because the batch weights do not provide enough signal frequency.

---

## 🎯 Recommended Downsampling & Re-balancing (Adapter V1)

To build a robust and functional **Adapter V1**, we recommend a balanced data mixture strategy. This involves downsampling the dominant tasks to prevent overfitting/gradient takeover while fully preserving the high-quality synthetic datasets.

### Target Dataset Mixture for SFT Trainer

| Dataset Name | Original Rows | Recommended Rows | Sampling Strategy | Recommended Mix % (Rows) | Expected Mix % (Tokens) |
| :--- | :---: | :---: | :--- | :---: | :---: |
| **Resume Sections Instruction** | 59,670 | 10,000 | Downsample (Random Uniform) | 69.43% | 3.98% |
| **Resume Job Fit** | 6,217 | 3,200 | Downsample (Balanced Labels) | 22.22% | 93.12% |
| **Resume Summary Synthetic** | 418 | 418 | Keep 100% (Full Preservation) | 2.90% | 1.17% |
| **Resume Review Synthetic** | 784 | 784 | Keep 100% (Full Preservation) | 5.44% | 1.72% |
| **Total Mixture** | **67,089** | **14,402** | **-** | **100.00%** | **100.00%** |

### Implementation Guidelines for LoRA/SFT
1. **Sampling Weights:** In the Hugging Face `SFTTrainer` or training script, apply custom sample blending or dataset wrapping to draw samples according to the recommended row mix counts.
2. **Packing Strategy:** Use packing (concatenating multiple short sequences like Resume Sections up to `max_seq_length = 4096`) to maximize VRAM utilization and training efficiency.
3. **Task-Specific Loss Scaling:** If possible, scale the loss weight for Resume Summary and Resume Review by `2.0x` or `3.0x` to amplify their training signals and compensate for their smaller size.
