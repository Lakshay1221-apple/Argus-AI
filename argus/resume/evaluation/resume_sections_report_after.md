# Dataset Optimization Report (After Cleaning) — Resume Sections

## Pipeline Removals Summary

| Filter Type | Count |
| :--- | :--- |
| **Original Rows** | **78670** |
| Invalid Prefix Removed | 978 |
| Null/Empty Content Removed | 350 |
| Content Short (<3 chars) Removed | 409 |
| Placeholder/Punctuation Only Removed | 9 |
| Duplicate Rows Removed | 17254 |
| **Final Cleaned Rows** | **59670** |
| **Total Rows Removed** | **19000** (24.15% reduction) |

## Unique Standardized Labels

Only the following 6 valid labels are present in the final dataset:
- `Education`
- `Experience`
- `Objective`
- `Personal Information`
- `Skills`
- `Summary`

## Section Balance Comparison (Before vs After)

| Section Label | Raw Count | Raw % | Cleaned Count | Cleaned % |
| :--- | :--- | :--- | :--- | :--- |
| **Personal Information** | 13293 | 16.90% | 8489 | 14.23% |
| **Summary** | 6542 | 8.32% | 5805 | 9.73% |
| **Skills** | 4974 | 6.32% | 3974 | 6.66% |
| **Experience** | 41158 | 52.32% | 34258 | 57.41% |
| **Education** | 9495 | 12.07% | 5707 | 9.56% |
| **Objective** | 2230 | 2.83% | 1437 | 2.41% |
| *Invalid Prefix* | 1 | 0.00% | 0 | 0.00% |

## Cleaned Content Length Statistics

### Overall Length Distribution

| Metric | Character Length | Token Length (Llama-3.2-1B) |
| :--- | :--- | :--- |
| Average | 67.57 | 14.21 |
| Median | 49 | 11 |
| Minimum | 3 | 1 |
| Maximum | 2079 | 394 |
| 95th Percentile | 186 | 36 |
| 99th Percentile | 356 | 72 |

### Length & Bounds Per Section

| Section Label | Count | Avg Char Len | Median Char Len | Max Char Len | Min Char Len | Avg Tokens | Median Tokens | Max Tokens | Min Tokens |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `Personal Information` | 8489 | 26.26 | 21 | 391 | 3 | 8.07 | 7 | 85 | 1 |
| `Summary` | 5805 | 94.23 | 78 | 1416 | 3 | 18.41 | 15 | 258 | 1 |
| `Skills` | 3974 | 38.71 | 29 | 1273 | 3 | 9.71 | 7 | 356 | 1 |
| `Experience` | 34258 | 80.98 | 64 | 2079 | 3 | 16.21 | 13 | 394 | 1 |
| `Education` | 5707 | 30.86 | 22 | 319 | 3 | 8.76 | 6 | 70 | 1 |
| `Objective` | 1437 | 109.70 | 93 | 568 | 5 | 19.64 | 17 | 95 | 1 |

### Longest and Shortest Examples Per Section

#### `Personal Information` Section

- **Longest Example (Char Len 391, Token Len 85):**
  > Family Background My father Mr Kanai Lal Biswas was a building contractor and now is a retired person My mother Smt Sabita Biswas is a house wife I happen to be the only son with one sister who is pursuing MA Distance Course from Rabindra Bharati University and she is a married woman My wife is a pe...
- **Shortest Example (Char Len 3, Token Len 2):**
  > MOB

#### `Summary` Section

- **Longest Example (Char Len 1416, Token Len 240):**
  > Consultant with 8+ years of proven track record of success in delivering outstanding results in a client facing role in the field of Law Enforcement, Health Care, Mortgage, Loan origination including Equipment Financing Govt., Manufacturing and Insurance products with IT Support in various financial...
- **Shortest Example (Char Len 3, Token Len 1):**
  > IDE

#### `Skills` Section

- **Longest Example (Char Len 1273, Token Len 356):**
  > Technical Skills: Windows 95/98/NT/2000/XP/Vista/7, MS Visio, MS Access, MS Word, MS Excel, MS Project, Rational Rose Enterprise, IBM Rational Software Architect, Microsoft Project, Rational Requisite Pro, MS SQL Server 7.0/2000, PL/SQL, CSS (Cascading Style Sheet), OLTP & OLAP, Synon/2E, COBOL, IBM...
- **Shortest Example (Char Len 3, Token Len 2):**
  > · C

#### `Experience` Section

- **Longest Example (Char Len 2079, Token Len 394):**
  > * Involved in the application development using Java platform. Model View Control (MVC) structure implementation. * Responsible for providing the client-side JavaScript validations and usage of HTML, JavaScript, XML, JSP, CSS as per the requirements to enhance the Portal UI. * Used Spring Core for D...
- **Shortest Example (Char Len 3, Token Len 2):**
  > D&B

#### `Education` Section

- **Longest Example (Char Len 319, Token Len 65):**
  > Master of Science, Computer Science | Andhra University, Visakhapatnam Bachelor of Science, Computer Science | Andhra University, Visakhapatnam Negotiate to Win | 7 Habits of Highly Effective People Certified, Project Manager | Wipro Technologies Certified, German Language course | Goethe Institute,...
- **Shortest Example (Char Len 3, Token Len 2):**
  > SMU

#### `Objective` Section

- **Longest Example (Char Len 568, Token Len 95):**
  > Willing to work as a key player in challenging and creative environment I intend to use my abilities to help my organization in reaching greater heights and to work hard and make the best utilization of my communication skills and knowledge to conquer new grounds and put in new inputs in the field o...
- **Shortest Example (Char Len 5, Token Len 1):**
  > goals

