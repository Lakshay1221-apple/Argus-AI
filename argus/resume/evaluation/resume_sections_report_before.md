# Dataset Exploration Report (Before Cleaning) — Resume Sections

## Core Metrics

- **Total Rows:** 78670
- **Column Names:** `text`, `raw_prefix`, `content`
- **Missing Values (Nulls):** 0
- **Empty Rows (Whitespace only):** 1
- **Duplicate Rows (Exact text duplicate):** 15852
- **Invalid Prefix Count:** 1

## Raw Prefix Distribution

| Raw Prefix | Count | Percentage |
| :--- | :--- | :--- |
| `Exp` | 41158 | 52.32% |
| `PI` | 13293 | 16.90% |
| `Edu` | 9495 | 12.07% |
| `Sum` | 6542 | 8.32% |
| `Skill` | 4974 | 6.32% |
| `Obj` | 2230 | 2.83% |
| `QC` | 977 | 1.24% |
| `INVALID` | 1 | 0.00% |

## Raw Content Length Statistics

### Character Lengths
- **Average Length:** 58.16
- **Median Length:** 37
- **Minimum Length:** 0
- **Maximum Length:** 2079
- **95th Percentile Length:** 171
- **99th Percentile Length:** 324

### Token Lengths (Llama-3.2-1B-Instruct)
- **Average Tokens:** 12.48
- **Median Tokens:** 9
- **Minimum Tokens:** 0
- **Maximum Tokens:** 394
- **95th Percentile Tokens:** 34
- **99th Percentile Tokens:** 67

## Random Sample Rows (20)

### Sample 1
- **Raw Prefix:** `Exp`
- **Raw Input Line:** `Exp	 Maintaining the CA Agile central for the project as per SDLC standards and performing activities like test cases mapping to requirements and execution of SIT test cases, defect tracking and reporting.`

### Sample 2
- **Raw Prefix:** `Exp`
- **Raw Input Line:** `Exp	Senior Business Analyst (July 2016 – April 2017)`

### Sample 3
- **Raw Prefix:** `Exp`
- **Raw Input Line:** `Exp	Facilitated Sprint review meeting to demonstrate potentially shippable product to stakeholders.`

### Sample 4
- **Raw Prefix:** `Exp`
- **Raw Input Line:** `Exp	Craiovan Consulting SRL Timisoara, Romania 6/2009 – 5/2011`

### Sample 5
- **Raw Prefix:** `Sum`
- **Raw Input Line:** `Sum	Researched on Best Industry Practices and explained the Business Users of the benefits and costs associated in implementing the same.`

### Sample 6
- **Raw Prefix:** `Obj`
- **Raw Input Line:** `Obj	speedy growth of the company & the individual and upgrade my qualification in order to place`

### Sample 7
- **Raw Prefix:** `Exp`
- **Raw Input Line:** `Exp	JOB PROFILE `

### Sample 8
- **Raw Prefix:** `PI`
- **Raw Input Line:** `PI	Father name  Vijay A  Suryavanshi`

### Sample 9
- **Raw Prefix:** `Exp`
- **Raw Input Line:** `Exp	Work Experience:`

### Sample 10
- **Raw Prefix:** `PI`
- **Raw Input Line:** `PI	Father’s Name`

### Sample 11
- **Raw Prefix:** `Exp`
- **Raw Input Line:** `Exp	. Created Reports in PDF, HTML, RTF formats according to the client specifications.`

### Sample 12
- **Raw Prefix:** `Edu`
- **Raw Input Line:** `Edu	CSE`

### Sample 13
- **Raw Prefix:** `Exp`
- **Raw Input Line:** `Exp	Responsibilites and Contributions:`

### Sample 14
- **Raw Prefix:** `Exp`
- **Raw Input Line:** `Exp	Exposure in Current Job:`

### Sample 15
- **Raw Prefix:** `Exp`
- **Raw Input Line:** `Exp	 IT division of Ardee Technologies Pvt ltd   Rourkela `

### Sample 16
- **Raw Prefix:** `Exp`
- **Raw Input Line:** `Exp	· To Review the Post Sanction Agreement Files for Two Wheeler, Car (loan agreement basis)`

### Sample 17
- **Raw Prefix:** `Exp`
- **Raw Input Line:** `Exp	Build Romeo-MyPlant Counter Synchronous service in webMethods, which receives required parameters from RomeoERP and using these parameters webMethods needs to build custom MyPlant URL and send request to MyPlant via xml over HTTP. WebMethods will insert the response from MyPlant into Romeo ERP s...`

### Sample 18
- **Raw Prefix:** `Edu`
- **Raw Input Line:** `Edu	10th Std`

### Sample 19
- **Raw Prefix:** `Edu`
- **Raw Input Line:** `Edu	Percentage`

### Sample 20
- **Raw Prefix:** `Exp`
- **Raw Input Line:** `Exp	Exported the processed data to the relational databases using Sqoop, to further visualize and generate reports for the BI team.`

