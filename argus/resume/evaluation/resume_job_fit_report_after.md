# Dataset Exploration Report — AFTER CLEANING

## Pipeline Removals Summary

| Filter Type | Count |
| :--- | :--- |
| Original Rows | 6241 |
| Null Rows Removed | 0 |
| Duplicate Rows Removed | 1 |
| Invalid Label Rows Removed | 0 |
| Length Filter (<100) Removed | 23 |
| **Final Cleaned Rows** | **6217** |
| **Total Rows Removed** | **24** |

## Dataset Statistics

- **Total Rows:** 6217
- **Column Names:** `resume_text`, `job_description_text`, `label`
- **Duplicate Rows:** 0

### Missing Values Per Column

| Column | Missing Count |
| :--- | :--- |
| `resume_text` | 0 |
| `job_description_text` | 0 |
| `label` | 0 |

### Label Distribution

| Label | Count | Percentage |
| :--- | :--- | :--- |
| `No Fit` | 3136 | 50.44% |
| `Fit` | 1542 | 24.8% |
| `Partial Fit` | 1539 | 24.75% |

### Text Length Statistics (Characters)

| Field | Average Length | Shortest | Longest |
| :--- | :--- | :--- | :--- |
| Resume | 5731.34 | 865 | 25328 |
| Job Description | 2721.12 | 211 | 7651 |

## Random Sample Rows (5)

### Sample 1

**Label:** `No Fit`

**Resume Text Snippet:**
> SummaryInvolving in various projects related to Data Modeling, Data Analysis, Design and Development for Data warehousing environments. Practical understanding of the Data modeling (Dimensional & Relational) concepts like Star-Schema Modeling, Snowflake Schema Modeling, Fact and Dimension tables. Co...

**Job Description Snippet:**
> The Senior Manager, Data Architecture & Data Engineering is responsible for translating business strategic goals into future-state data engineering and data science solutions. This includes delivery full life-cycle from execution roadmaps, to implementation, and to production operations. This role d...

---

### Sample 2

**Label:** `No Fit`

**Resume Text Snippet:**
> Career OverviewSeeking a job where I can effectively utilize my academic knowledge and learn new skills to continually enhance the development of my professional skills. QualificationsProficient or familiar with a vast array of programming languages, concepts and operating systems, including:C, Wind...

**Job Description Snippet:**
> Cloud and Things is a leading provider of IT solutions in the public sector. We are dedicated to delivering results and solving complex challenges for our clients. We are looking for individuals who are passionate about making a difference in the world, who are driven by a sense of purpose, and who ...

---

### Sample 3

**Label:** `No Fit`

**Resume Text Snippet:**
> SummarySkilled and technically qualified Java developer with 7+ years of IT industry experience, building web, stand-alone and mobile applications.Adept at designing and developing both front-end and back-end systems with on demand technologies while implementing web services using Java, Spring, Hib...

**Job Description Snippet:**
> A Senior Software Engineer at O'Reilly Auto Parts develops and supports applications for internal and external systems including Inventory, Supply Chain, eCommerce, Retail Applications, Enterprise Search and more. Our teams are focused on the development, design and integration of various software s...

---

### Sample 4

**Label:** `Fit`

**Resume Text Snippet:**
> Professional ProfileExpert in Functional Testing .6-Year Record of Proven ResultsSenior software QA testerwith full system development life cycle experience, including designing, developing and implementing test plans, high level calendar test cases and test processes with attention to detail result...

**Job Description Snippet:**
> Who We Are Apex Fintech Solutions (AFS) powers innovation and the future of digital wealth management by processing millions of transactions daily, to simplify, automate, and facilitate access to financial markets for all. Our robust suite of fintech solutions enables us to support clients such as S...

---

### Sample 5

**Label:** `No Fit`

**Resume Text Snippet:**
> ProfileDedicated Epidemiologist/Data Manager with excellent technical, analytical and communication skills demonstrated by 17 years of experience.Experienced professional with strong leadership and relationship-building skills. SkillsSAS Statistical Software,SAS-AF Software,Project ManagementProgram...

**Job Description Snippet:**
> Are you passionate about the clean tech automotive industry? Looking to make an impact with an global automotive company? Our client is on a mission to provide innovative energy management solutions for electric and conventional vehicles. They are actively growing their team in the US, and they are ...

---

