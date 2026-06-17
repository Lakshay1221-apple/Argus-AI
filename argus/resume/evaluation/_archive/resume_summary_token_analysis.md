# Token Analysis Report — Resume Summary

This analysis was conducted using the actual Llama-3.2-1B-Instruct tokenizer.

## Token Length Distributions

| Field | Average | Median | Minimum | Maximum | P95 | P99 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Resume** | 107.31 | 127 | 35 | 155 | 149 | 154 |
| **Summary** | 50.94 | 50 | 32 | 67 | 61 | 64 |
| **Combined** | 158.25 | 179 | 70 | 215 | 209 | 214 |

## LoRA Training Parameter Recommendations

- **95th Percentile Combined Sequence Length:** `209` tokens
- **99th Percentile Combined Sequence Length:** `214` tokens
- **Recommended Context Window (`max_seq_length`):** `1024` tokens (covers 100% of the dataset without truncation, maximizing efficiency and saving GPU memory).
