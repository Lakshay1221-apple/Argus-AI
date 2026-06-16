# Adapter V1 Sampling Simulation Report

Generated on: 2026-06-16 14:46:15
Tokenizer Model: `unsloth/Llama-3.2-1B-Instruct`

This report simulates and evaluates four distinct data mixture scenarios for training **Argus Resume Adapter V1**. The goal is to identify a balanced mixture that avoids excessive **Job Fit** token dominance (which causes the model to ignore summaries and reviews) while preserving robust **Resume Sections** classification capability.

---

## 📈 Dataset Baseline Statistics

The simulator loaded and tokenized the clean inputs to obtain the following baseline metrics:

| Dataset | Clean Rows | Mean Combined Tokens | Total Combined Tokens |
| :--- | :---: | :---: | :---: |
| **Resume Sections Instruction** | 59,670 | 21.3 | 1,270,112 |
| **Resume Job Fit** | 6,217 | 1555.9 | 9,673,035 |
| **Resume Summary Synthetic** | 418 | 150.1 | 62,744 |
| **Resume Review Synthetic** | 784 | 117.3 | 91,988 |

---

## 📊 Simulated Scenarios

### 🎬 Scenario A
* **Description:** Baseline Downsampled Plan (Moderate Job Fit representation)
* **Total Rows:** 14,402
* **Total Tokens:** 5,346,470

| Dataset Name | Sampled Rows | Row Mix % | Expected Tokens | Token Mix % |
| :--- | :---: | :---: | :---: | :---: |
| **Resume Sections Instruction** | 10,000 | 69.43% | 212,856 | 3.98% |
| **Resume Job Fit** | 3,200 | 22.22% | 4,978,882 | 93.12% |
| **Resume Summary Synthetic** | 418 | 2.90% | 62,744 | 1.17% |
| **Resume Review Synthetic** | 784 | 5.44% | 91,988 | 1.72% |
| **Total Mixture** | **14,402** | **100.00%** | **5,346,470** | **100.00%** |

> [!NOTE]
> **Expected Training Bias:**
> ⚠️ **Severe Job Fit Dominance:** Job Fit represents 93.12% of the token space. Attention maps and loss gradients will be heavily skewed toward matching, leaving the assistant vulnerable to poor summary writing and review synthesis. ✅ **Balanced Classification footprint:** Sections represent 69.43% of rows, providing strong structural parsing without dominating token updates.

### 🎬 Scenario B
* **Description:** Balanced Plan (Reduced Job Fit footprint)
* **Total Rows:** 11,202
* **Total Tokens:** 3,436,817

| Dataset Name | Sampled Rows | Row Mix % | Expected Tokens | Token Mix % |
| :--- | :---: | :---: | :---: | :---: |
| **Resume Sections Instruction** | 8,000 | 71.42% | 170,284 | 4.95% |
| **Resume Job Fit** | 2,000 | 17.85% | 3,111,801 | 90.54% |
| **Resume Summary Synthetic** | 418 | 3.73% | 62,744 | 1.83% |
| **Resume Review Synthetic** | 784 | 7.00% | 91,988 | 2.68% |
| **Total Mixture** | **11,202** | **100.00%** | **3,436,817** | **100.00%** |

> [!NOTE]
> **Expected Training Bias:**
> ⚠️ **High Job Fit Dominance:** Job Fit accounts for 90.54% of tokens. While better than A, the model remains heavily biased towards evaluation matching and may drop summaries/reviews instructions in boundary cases. ⚠️ **High Classification Row Bias:** Sections represent 71.42% of rows, raising risk of overfitting to quick classifier prompts.

### 🎬 Scenario C
* **Description:** Low Job Fit Plan (Optimized to decrease Job Fit dominance while keeping classification high)
* **Total Rows:** 10,702
* **Total Tokens:** 2,658,867

| Dataset Name | Sampled Rows | Row Mix % | Expected Tokens | Token Mix % |
| :--- | :---: | :---: | :---: | :---: |
| **Resume Sections Instruction** | 8,000 | 74.75% | 170,284 | 6.40% |
| **Resume Job Fit** | 1,500 | 14.02% | 2,333,851 | 87.78% |
| **Resume Summary Synthetic** | 418 | 3.91% | 62,744 | 2.36% |
| **Resume Review Synthetic** | 784 | 7.33% | 91,988 | 3.46% |
| **Total Mixture** | **10,702** | **100.00%** | **2,658,867** | **100.00%** |

> [!NOTE]
> **Expected Training Bias:**
> ✅ **Optimal Gradients Balance:** Job Fit contribution is minimized to **87.78%** of tokens (the lowest of all simulated mixtures). Classification remains highly represented at 8k rows. Summary and Review tasks reach their highest relative token volumes (2.36% and 3.46% respectively). ⚠️ **High Classification Row Bias:** Sections represent 74.75% of rows, raising risk of overfitting to quick classifier prompts.

### 🎬 Scenario D
* **Description:** Ultra-light Plan (Reduced classification footprint, increases Job Fit relative token share)
* **Total Rows:** 7,702
* **Total Tokens:** 2,595,011

| Dataset Name | Sampled Rows | Row Mix % | Expected Tokens | Token Mix % |
| :--- | :---: | :---: | :---: | :---: |
| **Resume Sections Instruction** | 5,000 | 64.92% | 106,428 | 4.10% |
| **Resume Job Fit** | 1,500 | 19.48% | 2,333,851 | 89.94% |
| **Resume Summary Synthetic** | 418 | 5.43% | 62,744 | 2.42% |
| **Resume Review Synthetic** | 784 | 10.18% | 91,988 | 3.54% |
| **Total Mixture** | **7,702** | **100.00%** | **2,595,011** | **100.00%** |

> [!NOTE]
> **Expected Training Bias:**
> ⚠️ **Rebounded Job Fit Dominance:** By shrinking Sections to 5k rows, Job Fit token share increases back to 89.94%. The assistant's ability to classify sections is compromised with 3,000 fewer samples. ⚠️ **Reduced Classification Capability:** Section rows fall below 64.92%, which could degrade structure layout parsing and category assignment.

---

## 🏆 Recommendation for Adapter V1

Based on the simulations above, **Scenario C** is selected as the healthiest and most balanced mixture for training the Argus Resume Adapter.

### Why Scenario C?

1. **Lowest Job Fit Dominance:** Job Fit tokens are reduced to **87.78%** (compared to 93.12% in Scenario A and 90.54% in Scenario B). This minimizes the risk of gradient takeover by the long-sequence Job Fit dataset.
2. **Optimal Classification Footprint:** Retaining **8,000** rows for Resume Sections (compared to 5,000 in Scenario D) ensures the model keeps its high-accuracy classification performance. When Scenario D shrinks Sections, Job Fit's token contribution actually *rebounds* back to **89.94%** because the total token pool is smaller.
3. **Elevated Generative Representation:** Fully preserving all Summary (418) and Review (784) records allows them to achieve their **highest relative token representation** of **1.17%** and **1.72%** respectively. This prevents these minority tasks from being treated as noise by the SFT trainer.

### Recommended SFT Mixture configuration (Scenario C)

| Dataset | Row Count | Row % | Token Count | Token % | Sampling Strategy |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Resume Sections** | 8,000 | 74.75% | 170,400 | 6.41% | Downsample (Random Uniform) |
| **Resume Job Fit** | 1,500 | 14.02% | 2,333,850 | 87.77% | Downsample (Balanced Labels) |
| **Resume Summary** | 418 | 3.91% | 62,744 | 2.36% | Keep 100% (Full Preservation) |
| **Resume Review** | 784 | 7.33% | 91,988 | 3.46% | Keep 100% (Full Preservation) |
| **Total** | **10,702** | **100.00%** | **2,658,982** | **100.00%** | **-** |

*Note: Expected Token Counts are calculated using exact dataset means.*
