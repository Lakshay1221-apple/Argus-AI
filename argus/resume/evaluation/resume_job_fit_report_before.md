# Dataset Exploration Report — BEFORE CLEANING

## Dataset Statistics

- **Total Rows:** 6241
- **Column Names:** `resume_text`, `job_description_text`, `label`
- **Duplicate Rows:** 1

### Missing Values Per Column

| Column | Missing Count |
| :--- | :--- |
| `resume_text` | 0 |
| `job_description_text` | 0 |
| `label` | 0 |

### Label Distribution

| Label | Count | Percentage |
| :--- | :--- | :--- |
| `No Fit` | 3143 | 50.36% |
| `Potential Fit` | 1556 | 24.93% |
| `Good Fit` | 1542 | 24.71% |

### Text Length Statistics (Characters)

| Field | Average Length | Shortest | Longest |
| :--- | :--- | :--- | :--- |
| Resume | 5804.40 | 897 | 25364 |
| Job Description | 2731.33 | 72 | 7669 |

## Random Sample Rows (5)

### Sample 1

**Label:** `Good Fit`

**Resume Text Snippet:**
> SummaryDegreed accountant with more than 10 years of diversified accounting experience seeking accounting position at a well-established company in Houston HighlightsTeam-orientedDetail-orientedDeadlines focusedExcellent communication and presentation skillsQuick learnerStrong management skillsGood ...

**Job Description Snippet:**
>   Position Title: Senior Construction Accountant (Req #: 116)  Location: Fresno, CA  Date Posted: 08082023  Pay Range: $82,000 - $118,000  Position Description:  Job Summary Responsible for maintaining financial records and ensures that financial transactions are properly recorded. Verifies the accu...

---

### Sample 2

**Label:** `No Fit`

**Resume Text Snippet:**
> Professional SummaryTo achieve a responsible position that gives me a chance to apply my innovative skills and knowledge. I aim to be a valuable member of the team that works dynamically towards success and growth of organization. Strong Knowledge in Electronics and computer Engineering background w...

**Job Description Snippet:**
> Skills - Cucumber BDD + Selenium UI Automation Experience Excellent knowledge and experience in testing Financial Domain applications.  Hands-on experience in Test Plan, Test Case, and Test Scenario development. Experience in creating data requests based on test cases and data mining.

---

### Sample 3

**Label:** `Good Fit`

**Resume Text Snippet:**
> Professional SummaryForward-thinking Software Engineer with background working effectively in dynamic environments. Fluent in Java and Typescript programming languages used to develop software within Retail and Health care domains. Proud team player focused on achieving project objectives with speed...

**Job Description Snippet:**
> -> Share resume to shan@imrsoft.com Job Title : JDE Business AnalystLocation : REMOTE Mandatory Skills : JDE World Homebuilder  Job Description :  Extensive experience (>10 years) in JDE World Homebuilder, Job Cost, and Procurement module functions functionality and associated business processes. (P...

---

### Sample 4

**Label:** `No Fit`

**Resume Text Snippet:**
> SummarySkilled and technically qualified Java developer with 7+ years of IT industry experience, building web, stand-alone and mobile applications.Adept at designing and developing both front-end and back-end systems with on demand technologies while implementing web services using Java, Spring, Hib...

**Job Description Snippet:**
> Calling all innovators  find your future at Fiserv. Were Fiserv, a global leader in Fintech and payments, and we move money and information in a way that moves the world. We connect financial institutions, corporations, merchants, and consumers to one another millions of times a day  quickly, reliab...

---

### Sample 5

**Label:** `No Fit`

**Resume Text Snippet:**
> ProfileLogical Data Analyst, skilled in eliciting and documenting data projects, requirement analysis, database management and generating insight through analytic and predictive data modelling. Self-directed and proactive professional with 5 years working with technology team using either Agile or H...

**Job Description Snippet:**
> Hello,Greetings from DevCare SolutionsI got an Opening with our direct client in Michigan *Need Only Local to Michigan Candidate 100% placement Position* Job title: Business AnalystLocation: Lansing, MIDuration: 1+YearsInterview mode: Ms. Teams Responsibilities: Minimum of 12 years of general BA exp...

---

