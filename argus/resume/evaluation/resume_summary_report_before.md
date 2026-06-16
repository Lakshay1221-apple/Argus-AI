# Dataset Exploration Report (Before Cleaning) — Resume Summary

## Core Metrics

- **Total Rows:** 100
- **Column Names:** `resume`, `ex_summary`
- **Missing Values (Nulls):** Resume = 0, Summary = 0
- **Empty Rows (Whitespace only):** Resume = 0, Summary = 0
- **Duplicate Rows (Exact raw duplicate):** 0

## Resume Text Length Statistics

| Metric | Character Length | Token Length (Llama-3.2-1B) |
| :--- | :--- | :--- |
| Average | 537.17 | 107.31 |
| Median | 630 | 127 |
| Minimum | 189 | 35 |
| Maximum | 772 | 155 |
| P95 | 747 | 149 |
| P99 | 768 | 154 |

## Summary Text Length Statistics

| Metric | Character Length | Token Length (Llama-3.2-1B) |
| :--- | :--- | :--- |
| Average | 285.15 | 50.94 |
| Median | 290 | 50 |
| Minimum | 167 | 32 |
| Maximum | 391 | 67 |
| P95 | 339 | 61 |
| P99 | 372 | 64 |

## Random Samples (10)

### Sample 1

**Raw Resume Snippet:**
> Samuel Harris | Architect Key Skills: Architectural design, project management, and construction administration Proficient in AutoCAD, Revit, and SketchUp Technical Skills: 3D modeling, Photoshop, and...

**Raw Summary:**
> Creative Architect with expertise in architectural design, project management, and construction administration. Proficient in AutoCAD, Revit, and SketchUp, with skills in 3D modeling, Photoshop, and InDesign for visual presentations. Holds a Bachelor's degree in Architecture from DEF University.

---

### Sample 2

**Raw Resume Snippet:**
> Isabella Young | Event Planner Core Skills: Event planning and coordination, budget management, and vendor relations Excellent organizational and communication abilities Relevant Experience: Event Pla...

**Raw Summary:**
> Detail-oriented Event Planner with expertise in event planning and coordination, budget management, and vendor relations. Excellent organizational and communication abilities, with experience in coordinating corporate events, weddings, and conferences. Holds a Bachelor's degree in Hospitality Management from CDE University. 

---

### Sample 3

**Raw Resume Snippet:**
> Leo Carter | Graphic Designer Key Competencies: Graphic design, branding, and print/digital media design Proficient in Adobe Creative Suite and Sketch Technical Skills: Adobe Illustrator, Photoshop, I...

**Raw Summary:**
> Creative Graphic Designer with expertise in graphic design, branding, and print/digital media design. Proficient in Adobe Creative Suite and Sketch, with experience in designing visual assets for various clients. Holds a Bachelor's degree in Graphic Design from GHI University.

---

### Sample 4

**Raw Resume Snippet:**
> Resume: David Morgan | Architect Key Skills: Architectural design, project management, and sustainable design practices Strong presentation and communication abilities Software Proficiencies: AutoCAD,...

**Raw Summary:**
> Creative Architect with expertise in architectural design, project management, and sustainable design practices. Strong presentation and communication abilities, with proficiency in AutoCAD, Revit, SketchUp, and Adobe Creative Suite. Holds a Master's degree and a Bachelor's degree in Architecture from PQR University.

---

### Sample 5

**Raw Resume Snippet:**
> Emily Hernandez | Sales Manager Core Competencies: Sales strategy development, client relationship management, and team leadership Proven track record of meeting and exceeding sales targets Industry E...

**Raw Summary:**
> Results-driven Sales Manager with experience in sales strategy development, client relationship management, and team leadership. Proven track record of meeting and exceeding sales targets in B2B and B2C sales across various industries. Holds a Bachelor's degree in Business Administration with a Major in Marketing from IJK University.

---

### Sample 6

**Raw Resume Snippet:**
> Resume: Elizabeth Lewis | Event Planner Professional Skills: Event planning, coordination, and management Strong organizational and communication abilities Industry Experience: Corporate events, weddi...

**Raw Summary:**
>  Organized Event Planner with expertise in event planning, coordination, and management. Strong communication and organizational abilities, with experience in corporate events, weddings, and conferences. Holds a Bachelor's degree in Hospitality Management from UVW University.

---

### Sample 7

**Raw Resume Snippet:**
> Rebecca Edwards | Full Stack Developer Programming Languages: JavaScript, Python, Ruby Front-end: HTML, CSS, React Back-end: Node.js, Express, Ruby on Rails Databases: SQL, MongoDB Education: BS in Co...

**Raw Summary:**
> Versatile Full Stack Developer proficient in JavaScript, Python, and Ruby with expertise in front-end and back-end technologies. Holds a BS in Computer Science from UVWX University.

---

### Sample 8

**Raw Resume Snippet:**
> Resume: Olivia Anderson | Marketing Manager Key Skills: Marketing strategy, social media management, and email marketing Proficient in Google Ads, Google Analytics, and Mailchimp Technical Skills: Ado...

**Raw Summary:**
>  management, and email marketing. Proficient in Google Ads, Google Analytics, and Mailchimp, with experience in using Adobe Creative Suite, Canva, and Hootsuite for marketing tasks. Holds a Bachelor's degree in Marketing from GHI University.

---

### Sample 9

**Raw Resume Snippet:**
> Resume: John Doe | Software Developer Experience: Java, Python, and C++ (4 years) Agile methodologies, RESTful APIs, and database management Education: Bachelor's degree in Computer Science, XYZ Unive...

**Raw Summary:**
> Experienced Software Developer with a strong background in Java, Python, and C++. Proficient in Agile methodologies, RESTful APIs, and database management. Holds a Bachelor's degree in Computer Science from XYZ University.

---

### Sample 10

**Raw Resume Snippet:**
> Resume: Laura Anderson | Product Manager Experience: Product lifecycle management, market research, and roadmap development (5 years) Agile methodologies and collaboration with cross-functional teams ...

**Raw Summary:**
> Results-driven Product Manager with 5 years of experience in product lifecycle management, market research, and roadmap development. Skilled in Agile methodologies and collaboration with cross-functional teams. Holds a Bachelor's degree in Business Administration from NOP University.

---

