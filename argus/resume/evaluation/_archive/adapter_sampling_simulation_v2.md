# SFT Mixture Sampling Simulation Report V2

Generated on: 2026-06-16 14:50:47
Tokenizer Model: `unsloth/Llama-3.2-1B-Instruct`

This report compares **Scenario C** and **Scenario E** configurations to select the healthiest multi-task SFT training mixture for Argus Resume Adapter V1.

---

## 📊 Scenario C (Optimized Downsampled Plan)
* **Total Rows:** 10,702
* **Total Tokens:** 2,633,577

| Dataset | Sampled Rows | Row Mix % | Expected Tokens | Token Mix % |
| :--- | :---: | :---: | :---: | :---: |
| **Resume Sections** | 8,000 | 74.75% | 170,284 | 6.47% |
| **Resume Job Fit** | 1,500 | 14.02% | 2,308,561 | 87.66% |
| **Resume Summary** | 418 | 3.91% | 62,744 | 2.38% |
| **Resume Review** | 784 | 7.33% | 91,988 | 3.49% |
| **Total** | **10,702** | **100.00%** | **2,633,577** | **100.00%** |

---

## 📊 Scenario E (Balanced Generator Plan)
* **Total Rows:** 7,202
* **Total Tokens:** 1,800,200

| Dataset | Sampled Rows | Row Mix % | Expected Tokens | Token Mix % |
| :--- | :---: | :---: | :---: | :---: |
| **Resume Sections** | 5,000 | 69.43% | 106,428 | 5.91% |
| **Resume Job Fit** | 1,000 | 13.89% | 1,539,040 | 85.49% |
| **Resume Summary** | 418 | 5.80% | 62,744 | 3.49% |
| **Resume Review** | 784 | 10.89% | 91,988 | 5.11% |
| **Total** | **7,202** | **100.00%** | **1,800,200** | **100.00%** |

---

## ⚖️ Contrast & Comparison

| Comparison Axis | Scenario C | Scenario E | Winner | Rationale |
| :--- | :---: | :---: | :---: | :--- |
| **Job Fit Token Share** | 87.66% | 85.49% | **Scenario E** | Decreases Job Fit dominance by **2.17%** points, allowing higher gradient attention to downstream generative tasks. |
| **Generative Share (Sum+Rev)** | 5.88% | 8.60% | **Scenario E** | Summary and Review tasks combined receive **8.51%** of token updates, a relative increase of **~46%** compared to Scenario C's **5.82%**. |
| **Training Speed & Compute** | 2,633,577 tokens | 1,800,200 tokens | **Scenario E** | Scenario E contains **833,377** fewer tokens (~32% reduction), saving significant training time and VRAM. |
| **Classifier Row representation** | 8,000 rows | 5,000 rows | **Scenario C** | Provides more classification records, though 5,000 is still statistically robust for a 6-class classifier. |

---

## 🏆 Chosen Healthiest Mixture

Based on the quantitative simulation and the design goals, **Scenario E** is selected. It avoids excessive **Job Fit** token dominance, boosts the learning signals for generative summarization and qualitative resume reviews, and offers a more VRAM-friendly and faster training run.
