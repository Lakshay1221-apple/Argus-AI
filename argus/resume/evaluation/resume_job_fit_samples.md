# Dataset Cleaning Visual Inspection Samples

This document displays 10 random samples showing their text **before** and **after** cleaning. Use this to verify that the regex cleaning operations did not remove valid technical content (such as `C++`, `C#`, `Node.js`).

## Sample 1 (Original Row Index: 2622)

- **Label:** `No Fit` ➔ `No Fit`
- **Before Lengths:** Resume = 2854 chars, JD = 4466 chars
- **After Lengths:** Resume = 2817 chars, JD = 4448 chars

### 📄 Resume Text Comparison

<details>
<summary>Show Original Resume</summary>

```text
SummaryInvolving in various projects related to Data Modeling, Data Analysis, Design and Development for Data warehousing environments. Practical understanding of the Data modeling (Dimensional & Relational) concepts like Star-Schema Modeling, Snowflake Schema Modeling, Fact and Dimension tables. Comprehensive knowledge and experience in process improvement, normalization/de-normalization, data extraction, data cleansing, data manipulation. Exceptional troubleshooting skills with ETL Technologies.
HighlightsHadoop, Hive, Avro, Kafka, MapReduce, Looker
Programming Languages: SQL, Java, Scala, PHP, Shell Script, HTML
Database Tools: Aster Database, PostgreSQL, MySQL
Operating Systems: Linux, Unix, Microsoft Windows
Experience08/2012toCurrentData EngineerAvanade|Greenville,NC,Experience with full development cycle of a Data Warehouse, including requirements gathering, design, implementation, and maintenance.Data modeling based on Kimball methodology, developed and architected ETL processes for different projects (RMA, inventory, purchase order etc.) Re-engineer some of the current ETL processes to streamline the data acquisition and integration process using our homegrown ETL tools.Built event-driven data pipeline that comprises multiple steps to gather high volume and velocity data from both push based and pull based sources, which includes design and implement web service to collect data (JSON object over http request), convert data in JSON format into Avro then feed into Kafka, land data in Kafka on Hadoop and Aster.Designed and built Looker API using Scala, which makes other teams access the data in data warehouse more easily and gracefully.Establish and maintain SQL queries and routines.Write ad-hoc queries based upon the schema understanding for diverse needs of our business users.02/2012to03/2012Java InternDominion Enterprises|Fredericksburg,VA,Implemented code for small features & bug-fixes in Java.06/2011to09/2011PHP DeveloperMeetoncruise|City,STATE,Implemented the back-end logic using PHP.Utilized JQuery and AJAX to provide dynamic and interactive user interface.Designed and implemented data model in MySQL database to support the website.
EducationExpected in2012totoMaster of Science|Electrical and Computer EngineeringPolytechnic Institute of New York University,Brooklyn,NYGPA:Electrical and Computer EngineeringExpected in2010totoBachelor of Science|Automation EngineeringNanjing University of Aeronautics and Astronautics,Nanjing,JiangsuGPA:Automation Engineering
Skillsstreamline, ad, AJAX, API, data acquisition, Data modeling, data warehouse, Database, engineer, ETL, features, HTML, http, PHP, inventory, Java, JQuery, JSON, Linux, logic, access, Microsoft Windows, MySQL, Operating Systems, PostgreSQL, processes, Programming, requirements gathering, Shell Script, SQL, Unix, user interface, website
```
</details>

<details>
<summary>Show Cleaned Resume</summary>

```text
SummaryInvolving in various projects related to Data Modeling, Data Analysis, Design and Development for Data warehousing environments. Practical understanding of the Data modeling (Dimensional & Relational) concepts like Star-Schema Modeling, Snowflake Schema Modeling, Fact and Dimension tables. Comprehensive knowledge and experience in process improvement, normalization/de-normalization, data extraction, data cleansing, data manipulation. Exceptional troubleshooting skills with ETL Technologies.
HighlightsHadoop, Hive, Avro, Kafka, MapReduce, Looker
Programming Languages: SQL, Java, Scala, PHP, Shell Script, HTML
Database Tools: Aster Database, PostgreSQL, MySQL
Operating Systems: Linux, Unix, Microsoft Windows
Experience08/2012toCurrentData EngineerAvanade| ,Experience with full development cycle of a Data Warehouse, including requirements gathering, design, implementation, and maintenance.Data modeling based on Kimball methodology, developed and architected ETL processes for different projects (RMA, inventory, purchase order etc.) Re-engineer some of the current ETL processes to streamline the data acquisition and integration process using our homegrown ETL tools.Built event-driven data pipeline that comprises multiple steps to gather high volume and velocity data from both push based and pull based sources, which includes design and implement web service to collect data (JSON object over http request), convert data in JSON format into Avro then feed into Kafka, land data in Kafka on Hadoop and Aster.Designed and built Looker API using Scala, which makes other teams access the data in data warehouse more easily and gracefully.Establish and maintain SQL queries and routines.Write ad-hoc queries based upon the schema understanding for diverse needs of our business users.02/2012to03/2012Java InternDominion Enterprises| ,Implemented code for small features & bug-fixes in Java.06/2011to09/2011PHP DeveloperMeetoncruise| ,Implemented the back-end logic using PHP.Utilized JQuery and AJAX to provide dynamic and interactive user interface.Designed and implemented data model in MySQL database to support the website.
EducationExpected in2012totoMaster of Science|Electrical and Computer EngineeringPolytechnic Institute of New York University,Brooklyn,NYGPA:Electrical and Computer EngineeringExpected in2010totoBachelor of Science|Automation EngineeringNanjing University of Aeronautics and Astronautics,Nanjing,JiangsuGPA:Automation Engineering
Skillsstreamline, ad, AJAX, API, data acquisition, Data modeling, data warehouse, Database, engineer, ETL, features, HTML, http, PHP, inventory, Java, JQuery, JSON, Linux, logic, access, Microsoft Windows, MySQL, Operating Systems, PostgreSQL, processes, Programming, requirements gathering, Shell Script, SQL, Unix, user interface, website
```
</details>

### 💼 Job Description Text Comparison

<details>
<summary>Show Original Job Description</summary>

```text
The Senior Manager, Data Architecture & Data Engineering is responsible for translating business strategic goals into future-state data engineering and data science solutions. This includes delivery full life-cycle from execution roadmaps, to implementation, and to production operations. This role drives the creation and maintenance of enterprise data and analytics capabilities, data reference architectures, and integrated data & analytics technology roadmaps that will guide our strategic investments and enterprise strategy.Translate business strategic goals into actionable future-state data engineering and data science architectures and solutions.Delivery of full life-cycle Data Solutions from execution roadmaps, to implementation, and to operations. This includes a specific focus on ELT and ETL Data Pipeline solutions from inception to production.Lead end to end solution delivery of enterprise data warehouse, data marts, and data lake with governance.Drive the creation and maintenance of enterprise data and analytics capabilities, data solutions, and integrated data & analytics technology roadmaps that will guide our strategic investments and enterprise strategy.Deliver architecture connecting Data Science, Data Engineering, and Data Analytics practices together to deliver impactful data products.Strong partnership with DevOps, DataOps, business partners, engineering teams, and data management.A minimum of ten (10) years of experience in IT with a minimum (6) years in data architecture and data solutions are required.Successful track-record in managing a team of Data Engineers and Data ScientistsSkilled in hybrid cloud data platforms and analytical technologies including Azure andor GCP data infrastructure, Spark, Data Lake, Data Warehouse and Data Marts, BI reporting with PowerBI, Metadata Management, Data Governance, Master Data Management, Data Catalog, and Business Glossary.Ability to document, communicate, implement, and operationalize complex architectures.Experience with ELT and ETL Data Pipeline solutions from inception to production.Proficient in SQL, NoSQL and columnar databases.Experience with SparkPyspark and JSON.Excellent grasp of Computer Science fundamentals - data structures and algorithms.Must have Panda Data Frames knowledge and best practices, execution engines, DAGs (airflow, dagster, luigi, etc), and Kubernetes.Proficient with GitLabFamiliarity with Azure data factory preferred, Google data flow or AWS GlueExperience with Biomedical Informatics, S3Azure blob store, Machine Learning and AI, Unstructured Data, and Data Democratization is preferred.Experience with Agile methodologies, Kanban preferred, and using tools like Jira and Confluence to facilitate the work.Bachelor's degree in computer science or a related discipline required. Master's degree preferred. RECRUITERS NOTES: The role will definitely be hands-on and will require excellent communication skills. The hiring manager mentioned the following technologies: AImachine learning; data warehouses; product support; Cloud experienceAzure; must be open to new technologies. Working with the Product Development Team. Act as the point of contact; will create a group that helps the product teams. Create data warehouses for analytics. MUST have excellent communication skills  verbal and written. This person will envision strategy and must be able to effectively communicate that strategy to others.  The organization has asked me not to advertise the compensation. If you contact me I would be more than willing to share it with you. 
For over 50 years this non-profit organization has made it their mission to protect patients from unsafe and ineffective medical technologies and practices. More than 5,000 healthcare institutions and systems worldwide including four out of every five U.S. hospitals rely on the services of this organization to guide their operational and strategic decisions. In addition, they serve public and private payers, federal and state agencies, policymakers, ministries of health, associations, and accrediting agencies. Benefit from a healthy work-life balance while staying on the leading edge of technology and thriving in an innovative startup-like culture minus the risk. Sleep well knowing you are helping achieve a world where safe, high-quality healthcare is accessible to everyone. Excellent benefits to include work from home, flex-time and 19 days starting vacation.
Its a nice place to work!
```
</details>

<details>
<summary>Show Cleaned Job Description</summary>

```text
The Senior Manager, Data Architecture & Data Engineering is responsible for translating business strategic goals into future-state data engineering and data science solutions. This includes delivery full life-cycle from execution roadmaps, to implementation, and to production operations. This role drives the creation and maintenance of enterprise data and analytics capabilities, data reference architectures, and integrated data & analytics technology roadmaps that will guide our strategic investments and enterprise strategy.Translate business strategic goals into actionable future-state data engineering and data science architectures and solutions.Delivery of full life-cycle Data Solutions from execution roadmaps, to implementation, and to operations. This includes a specific focus on ELT and ETL Data Pipeline solutions from inception to production.Lead end to end solution delivery of enterprise data warehouse, data marts, and data lake with governance.Drive the creation and maintenance of enterprise data and analytics capabilities, data solutions, and integrated data & analytics technology roadmaps that will guide our strategic investments and enterprise strategy.Deliver architecture connecting Data Science, Data Engineering, and Data Analytics practices together to deliver impactful data products.Strong partnership with DevOps, DataOps, business partners, engineering teams, and data management.A minimum of ten (10) years of experience in IT with a minimum (6) years in data architecture and data solutions are required.Successful track-record in managing a team of Data Engineers and Data ScientistsSkilled in hybrid cloud data platforms and analytical technologies including Azure andor GCP data infrastructure, Spark, Data Lake, Data Warehouse and reporting with PowerBI, Metadata Management, Data Governance, Master Data Management, Data Catalog, and Business Glossary.Ability to document, communicate, implement, and operationalize complex architectures.Experience with ELT and ETL Data Pipeline solutions from inception to production.Proficient in SQL, NoSQL and columnar databases.Experience with SparkPyspark and JSON.Excellent grasp of Computer Science fundamentals - data structures and algorithms.Must have Panda Data Frames knowledge and best practices, execution engines, DAGs (airflow, dagster, luigi, etc), and Kubernetes.Proficient with GitLabFamiliarity with Azure data factory preferred, Google data flow or AWS GlueExperience with Biomedical Informatics, S3Azure blob store, Machine Learning and AI, Unstructured Data, and Data Democratization is preferred.Experience with Agile methodologies, Kanban preferred, and using tools like Jira and Confluence to facilitate the work.Bachelor's degree in computer science or a related discipline required. Master's degree preferred. RECRUITERS NOTES: The role will definitely be hands-on and will require excellent communication skills. The hiring manager mentioned the following technologies: AImachine learning; data warehouses; product support; Cloud experienceAzure; must be open to new technologies. Working with the Product Development Team. Act as the point of contact; will create a group that helps the product teams. Create data warehouses for analytics. MUST have excellent communication skills verbal and written. This person will envision strategy and must be able to effectively communicate that strategy to others. The organization has asked me not to advertise the compensation. If you contact me I would be more than willing to share it with you.
For over 50 years this non-profit organization has made it their mission to protect patients from unsafe and ineffective medical technologies and practices. More than 5,000 healthcare institutions and systems worldwide including four out of every five U.S. hospitals rely on the services of this organization to guide their operational and strategic decisions. In addition, they serve public and private payers, federal and state agencies, policymakers, ministries of health, associations, and accrediting agencies. Benefit from a healthy work-life balance while staying on the leading edge of technology and thriving in an innovative startup-like culture minus the risk. Sleep well knowing you are helping achieve a world where safe, high-quality healthcare is accessible to everyone. Excellent benefits to include work from home, flex-time and 19 days starting vacation.
Its a nice place to work!
```
</details>

---

## Sample 2 (Original Row Index: 1877)

- **Label:** `No Fit` ➔ `No Fit`
- **Before Lengths:** Resume = 6073 chars, JD = 3620 chars
- **After Lengths:** Resume = 5926 chars, JD = 3620 chars

### 📄 Resume Text Comparison

<details>
<summary>Show Original Resume</summary>

```text
Career OverviewSeeking a job where I can effectively utilize my academic knowledge and learn new skills to continually enhance the development of my professional skills.
QualificationsProficient or familiar with a vast array of programming languages, concepts and operating systems, including:C, Windows 98/2000/03/XP/VISTA/7/8/10,Adobe Photoshop, Visual StudioNetwork fundamentals,MATLAB, SQL Server 2008R2,2012.SSIS,SSAS,SSRSMultisim, simulink, ImageProcessing.SQL, T-SQL. SQL Server 2012/2008/2005 Enterprise Edition, SSIS, SSRS, PPS, MS PowerPoint, MS Project, MS Access 2003 ,Oracle, Business Objects ,SharePoint , PL/SQL, C#,VB.Net,ASP.NET, XML, Visual Studio 2008 & 2005,MS Visio 2007,Borland StarTeam, Build Forge, Visual SourceSafe
Work Experience02/2017toPresentJr Data analystApex Systems–Gulfport,MS,Underwent internship program conducted by BSNL Telecommunications Vijayawada.Trained in designing PULSE DIGITAL CIRCUITS.Underwent internship program as Data Analyst at A4 Softech.Activities.Won prizes in many essay writings, elocution, quiz, debate competitions and talent search examinations in school and college levels.Active member of Institute of Electronics and Telecommunication Engineers (IETE).Project Work :
Title    
          Description          
Customer Master ETL Integration
The Repository: The Repository contains all of the metadata required for the training examples.It
is hosted, for these evaluation purposes, in a supplied database.Orders Application: An application for tracking customer orders, hosted in a supplied database.Parameters (File): Flat files (ASCII) issued from the production system containing a list of sales representatives and the segmentation of ages into age ranges.Sales Administration: The administration or tracking of sales, hosted in another supplied database .We will populate this data warehouse with our transformations.Exos is the cloud provider that offers various cloud services like virtual servers, storage, networking and hosted applications for corporate messaging, document management and company portals.Developed custom user interface for the document management solution that helps to easily sort, order, filter and manage documents in the cloud from the dashboard.Responsibilities:.Analyzed business requirements and built logical and physical data models that described all the data and relationships between the data.Created Tables, Stored Procedures, Views, Indexes, User-defined Functions and Triggers to use them for updating and cleaning the existing and the new data.Created indexes to improve the performance of the queries.Performed job scheduling to ensure execution of certain jobs and daily updates.Extensively used T-SQL in constructing Stored Procedures, triggers, cursors, tables, user defined functions, views, indexes.Upgraded DTS packages to SQL Server Integration Services (SSIS) and used it to perform bulk insert operations from SQL Server 2012/2008R2/2008 databases to flat files/CSV files and vice versa.Configured the  SSIS Package for run time Parameters and Configured files as well as developed  the Documents for Logging/Error Handling for SSIS Packages.Worked on different sources in SSIS (XML, Flat file, Excel, OLEDB Source) and created XSLT files for loading the XML data to database.Implemented custom error handling in SSIS packages and also worked on different methods of logging.Created batch files to load the data from text file to database tables.Developed packages to copy tables, schemas and views and to extract data from Excel and other legacy systems using SSIS.Developed complex SSIS packages to migrate the data from flat files to SSIS.Created ETL/SSIS packages both design and code to process data to target databases.Created technical documents for the process of executing the packages.Performed MS SQL Server Configuration, Performance Tuning of stored procedures, SSIS Packages, SSRS Reports.Performed unit and system testing, troubleshooting and bug fixing in development, QA environments and some of the production issues.Modified existing reports by creating new Parameters, Formulas etc,.Created SQL Server Profiler traces & used with Database Tuning Advisor (DTA) for optimum performance of T-SQL and MDX queries.Logged & tracked defects in JIRA and followed up to make sure they are resolved and tested in QA environment before the code released to staging and production servers.Worked on source controls VSS (Visual Source Safe), Borland Star team.Involved in crystal report generation and also generated EXCEL based reports for business users.Reported and tracked the status of the bugs per project, resolved defects based on project severity of the defects using Jira for the development & QA team to prioritize.Developed custom reports and deployed them on server using SQL Server Reporting Services (SSRS).Created adhoc reports based on the user requirements and worked on different on-demand reports.Created Drill down reports, parameterized reports, cascading parameterized reports and drill through reports.
Education and TrainingExpected intotoBachelors:Electronics & CommunicationsDHANEKULA-Vijayawada,APGPA:Electronics & Communications 63.28 91.2Expected in06/20/1993toto:Sri Chaitanya college-Vijayawada,APGPA:Availability     
Graduate student, Department of Electrical engineering, Fairleigh Dickinson University.
SkillsVB.Net, ASP.NET, Adobe Photoshop, Borland, Business Objects, C, good Communication skills, crystal report, Data Analyst, DTS, data warehouse, databases, Database, designing, document management, Electrical engineering, Electronics, English, ETL, XML, Image
Processing, Logging, MATLAB, messaging, MS Access, C#, EXCEL, MS PowerPoint, MS Project, SharePoint, 2000, Windows 98, Enterprise, Network, networking, OLEDB, operating systems, Oracle, PL/SQL, programming, QA, quiz, Reporting, Sales, scheduling, servers, Visual SourceSafe, Visual Source Safe, MS SQL Server, SQL, SQL Server, Tables, Telecommunication, Telecommunications, T-SQL, troubleshooting, user interface, Visio, VISTA, Visual Studio, XSLT
```
</details>

<details>
<summary>Show Cleaned Resume</summary>

```text
Career OverviewSeeking a job where I can effectively utilize my academic knowledge and learn new skills to continually enhance the development of my professional skills.
QualificationsProficient or familiar with a vast array of programming languages, concepts and operating systems, including:C, Windows 98/2000/03/XP/VISTA/7/8/10,Adobe Photoshop, Visual StudioNetwork fundamentals,MATLAB, SQL Server 2008R2,2012.SSIS,SSAS,SSRSMultisim, simulink, ImageProcessing.SQL, T-SQL. SQL Server 2012/2008/2005 Enterprise Edition, SSIS, SSRS, Access 2003 ,Oracle, Business Objects , /SQL, C#,VB.Net,ASP.NET, XML, Visual Studio 2008 & 2005,MS Visio 2007,Borland StarTeam, Build Forge, Visual SourceSafe
Work Experience02/2017toPresentJr Data analystApex Systems– ,Underwent internship program conducted by BSNL Telecommunications Vijayawada.Trained in designing PULSE DIGITAL CIRCUITS.Underwent internship program as Data Analyst at A4 Softech.Activities.Won prizes in many essay writings, elocution, quiz, debate competitions and talent search examinations in school and college levels.Active member of Institute of Electronics and Telecommunication Engineers (IETE).Project Work :
Title
 Description
Customer Master ETL Integration
The Repository: The Repository contains all of the metadata required for the training examples.It
is hosted, for these evaluation purposes, in a supplied database.Orders Application: An application for tracking customer orders, hosted in a supplied database.Parameters (File): Flat files (ASCII) issued from the production system containing a list of sales representatives and the segmentation of ages into age ranges.Sales Administration: The administration or tracking of sales, hosted in another supplied database .We will populate this data warehouse with our transformations.Exos is the cloud provider that offers various cloud services like virtual servers, storage, networking and hosted applications for corporate messaging, document management and company portals.Developed custom user interface for the document management solution that helps to easily sort, order, filter and manage documents in the cloud from the dashboard.Responsibilities:.Analyzed business requirements and built logical and physical data models that described all the data and relationships between the data.Created Tables, Stored Procedures, Views, Indexes, User-defined Functions and Triggers to use them for updating and cleaning the existing and the new data.Created indexes to improve the performance of the queries.Performed job scheduling to ensure execution of certain jobs and daily updates.Extensively used T-SQL in constructing Stored Procedures, triggers, cursors, tables, user defined functions, views, indexes.Upgraded DTS packages to SQL Server Integration Services (SSIS) and used it to perform bulk insert operations from SQL Server 2012/2008R2/2008 databases to flat files/CSV files and vice versa.Configured the SSIS Package for run time Parameters and Configured files as well as developed the Documents for Logging/Error Handling for SSIS Packages.Worked on different sources in SSIS (XML, Flat file, Excel, OLEDB Source) and created XSLT files for loading the XML data to database.Implemented custom error handling in SSIS packages and also worked on different methods of logging.Created batch files to load the data from text file to database tables.Developed packages to copy tables, schemas and views and to extract data from Excel and other legacy systems using SSIS.Developed complex SSIS packages to migrate the data from flat files to SSIS.Created ETL/SSIS packages both design and code to process data to target databases.Created technical documents for the process of executing the packages.Performed MS SQL Server Configuration, Performance Tuning of stored procedures, SSIS Packages, SSRS Reports.Performed unit and system testing, troubleshooting and bug fixing in development, QA environments and some of the production issues.Modified existing reports by creating new Parameters, Formulas etc,.Created SQL Server Profiler traces & used with Database Tuning Advisor (DTA) for optimum performance of T-SQL and MDX queries.Logged & tracked defects in JIRA and followed up to make sure they are resolved and tested in QA environment before the code released to staging and production servers.Worked on source controls VSS (Visual Source Safe), Borland Star team.Involved in crystal report generation and also generated EXCEL based reports for business users.Reported and tracked the status of the bugs per project, resolved defects based on project severity of the defects using Jira for the development & QA team to prioritize.Developed custom reports and deployed them on server using SQL Server Reporting Services (SSRS).Created adhoc reports based on the user requirements and worked on different on-demand reports.Created Drill down reports, parameterized reports, cascading parameterized reports and drill through reports.
Education and TrainingExpected intotoBachelors:Electronics & CommunicationsDHANEKULA-Vijayawada,APGPA:Electronics & Communications 63.28 91.2Expected in06/20/1993toto:Sri Chaitanya college-Vijayawada,APGPA:Availability
Graduate student, Department of Electrical engineering, Fairleigh Dickinson University.
SkillsVB.Net, ASP.NET, Adobe Photoshop, Borland, Business Objects, C, good Communication skills, crystal report, Data Analyst, DTS, data warehouse, databases, Database, designing, document management, Electrical engineering, Electronics, English, ETL, XML, Image
Processing, Logging, MATLAB, messaging, MS Access, C#, Project, SharePoint, 2000, Windows 98, Enterprise, Network, networking, OLEDB, operating systems, /SQL, programming, QA, quiz, Reporting, Sales, scheduling, servers, Visual SourceSafe, SQL Server, SQL, SQL Server, Tables, Telecommunication, Telecommunications, T-SQL, troubleshooting, user interface, Visio, VISTA, Visual Studio, XSLT
```
</details>

### 💼 Job Description Text Comparison

<details>
<summary>Show Original Job Description</summary>

```text
Cloud and Things is a leading provider of IT solutions in the public sector. We are dedicated to delivering results and solving complex challenges for our clients. We are looking for individuals who are passionate about making a difference in the world, who are driven by a sense of purpose, and who are committed to excellence. Our team thrives on collaboration, innovation, and delivering high-quality projects that have a significant impact on the public sector's IT landscape.
We are seeking experienced Business Analysts for Level III positions with a strong background in leading complex projects and a focus on system requirements analysis. As a Business Analyst, you will play a crucial role in understanding business needs, gathering requirements, and contributing to the successful implementation of projects. You will collaborate closely with cross-functional teams and assume a leadership role to ensure that project planning, design, and delivery align with business objectives.
DutiesLead and participate in requirements gathering sessions, facilitating discussions to capture client-focused needs.Analyze gathered requirements to identify key insights and prioritize system requirements for continuous integration and deployment.Utilize your expertise to validate and document system requirements that align with best-fit technology solutions.Manage and identify system requirements with a focus on areas such as eligibility, enrollment, case management, payment, claims, and recoupments.Document system requirements for mainframe modernization projects across multiple complex functional domains.Conduct thorough business process analysis and optimization within technology environments, documenting current "As Is" states and proposing innovative "To Be" states.Develop comprehensive requirements documentation, including use cases, screen prototypes, and specifications, adhering to established templates and using tools like Blueprint Storyteller.Facilitate meetings and workgroups to foster collaboration and ensure a comprehensive understanding of requirements.
Basic QualificationsAt least 7 years of experience on complex projects, with a minimum of two (2) years in a leadership role as a Business Analyst.At least 7 years of client-focused business and requirements analysis experience, including leading requirements gathering sessions and preparing technology proposals based on elicited requirements.
Preferred SkillsProfound experience in managing, identifying, documenting, and validating system requirements in areas like eligibility, enrollment, case management, payment, claims, and recoupments.Expertise in identifying, documenting, and validating system requirements within mainframe modernization projects encompassing multiple intricate functional domains.Strong aptitude for business process analysis and optimization in technology environments, with an ability to document "As Is" and "To Be" states.Extensive proficiency in creating comprehensive requirements documentation, including use cases, screen prototypes, and specifications, using tools like Blueprint Storyteller.Demonstrated capability in facilitating meetings and workgroups to enhance collaboration and requirement understanding.
 Cloud and Things complies with all applicable federal, state, and local laws regarding recruitment and hiring. All qualified applicants are considered for employment without regard to race, color, religion, sex, sexual orientation, gender identity, national origin, age, disability, protected veteran status, or any other category protected by applicable federal, state, or local laws.
```
</details>

<details>
<summary>Show Cleaned Job Description</summary>

```text
Cloud and Things is a leading provider of IT solutions in the public sector. We are dedicated to delivering results and solving complex challenges for our clients. We are looking for individuals who are passionate about making a difference in the world, who are driven by a sense of purpose, and who are committed to excellence. Our team thrives on collaboration, innovation, and delivering high-quality projects that have a significant impact on the public sector's IT landscape.
We are seeking experienced Business Analysts for Level III positions with a strong background in leading complex projects and a focus on system requirements analysis. As a Business Analyst, you will play a crucial role in understanding business needs, gathering requirements, and contributing to the successful implementation of projects. You will collaborate closely with cross-functional teams and assume a leadership role to ensure that project planning, design, and delivery align with business objectives.
DutiesLead and participate in requirements gathering sessions, facilitating discussions to capture client-focused needs.Analyze gathered requirements to identify key insights and prioritize system requirements for continuous integration and deployment.Utilize your expertise to validate and document system requirements that align with best-fit technology solutions.Manage and identify system requirements with a focus on areas such as eligibility, enrollment, case management, payment, claims, and recoupments.Document system requirements for mainframe modernization projects across multiple complex functional domains.Conduct thorough business process analysis and optimization within technology environments, documenting current "As Is" states and proposing innovative "To Be" states.Develop comprehensive requirements documentation, including use cases, screen prototypes, and specifications, adhering to established templates and using tools like Blueprint Storyteller.Facilitate meetings and workgroups to foster collaboration and ensure a comprehensive understanding of requirements.
Basic QualificationsAt least 7 years of experience on complex projects, with a minimum of two (2) years in a leadership role as a Business Analyst.At least 7 years of client-focused business and requirements analysis experience, including leading requirements gathering sessions and preparing technology proposals based on elicited requirements.
Preferred SkillsProfound experience in managing, identifying, documenting, and validating system requirements in areas like eligibility, enrollment, case management, payment, claims, and recoupments.Expertise in identifying, documenting, and validating system requirements within mainframe modernization projects encompassing multiple intricate functional domains.Strong aptitude for business process analysis and optimization in technology environments, with an ability to document "As Is" and "To Be" states.Extensive proficiency in creating comprehensive requirements documentation, including use cases, screen prototypes, and specifications, using tools like Blueprint Storyteller.Demonstrated capability in facilitating meetings and workgroups to enhance collaboration and requirement understanding.
 Cloud and Things complies with all applicable federal, state, and local laws regarding recruitment and hiring. All qualified applicants are considered for employment without regard to race, color, religion, sex, sexual orientation, gender identity, national origin, age, disability, protected veteran status, or any other category protected by applicable federal, state, or local laws.
```
</details>

---

## Sample 3 (Original Row Index: 2559)

- **Label:** `No Fit` ➔ `No Fit`
- **Before Lengths:** Resume = 3815 chars, JD = 4000 chars
- **After Lengths:** Resume = 3756 chars, JD = 4000 chars

### 📄 Resume Text Comparison

<details>
<summary>Show Original Resume</summary>

```text
SummarySkilled and technically qualified Java
developer with 7+ years of IT industry experience, building web, stand-alone and mobile applications.Adept at designing and developing both front-end and back-end systems with on demand technologies while implementing web services using Java, Spring, Hibernate, REST, SOAP, AWS, jQuery, AJAX, JSON and XML.Competent at  understanding requirements and converting
it to solutions in an Agile (Scrum) project development environment, while utilizing Application Security principles.
SkillsLanguages:
Java, JavaScript, Android, PythonWeb: Java EE, Servlets,
JSP, JSF, JavaScript, jQuery, AJAX, HTML5, CSS3, Bootstrap, AngularJSWeb Services: REST,
SOAP, JSON, XML, JMS, Google Map API, Twitter API, AWS, Cloud FoundryWeb/App Servers:
Tomcat, Glassfish, PivotalFrameworks: Spring, Hibernate, Swing, JSF, JDBC, JPA, GJTAPI, JMAPI, JSAPI, IVR, DTMFDatabases:
MySQL, NoSQL, MongoDB, HbaseBig Data: MR,
HDFS, Spark, Sqoop, Flume, Pig, HiveDesign Patterns:
Singleton, Prototype, Facade, Factory, MVC and other Java Design PatternsSDLC: Agile (Scrum, DSDM,
XP), SSADM, USDP and othersTools: Maven, Git, Eclipse, IntelliJ, Android Studio, UML ToolsPlatforms:
Windows, Linux, Cloudera, BackTrack, AndroidNetworks & Security: Vulnerability
Assessment, Penetration Testing, CCNA, CCNA Security
Professional ExperienceJava Software Engineer,08/2017-CurrentWells Fargo Bank–Brisbane,CA,Collaborated with team members to create and integrate high availability solutions for mission-critical applications.Assisted customers in resolving defects in the most effective manner.Prepared and presented design and technical proposals for clients.Project:Precision Dispatch System (PDS)Technologies used:Java, Swing, JMS, CORBA, SMI, XML, XSL, Oracle, Log4j, MVC, Git, Github, Eclipse, Rally, Confluence.Software Developer,02/2015-06/2016Smart Software Solutions, Inc–Austin,TX,Successfully developed and supported projects across the entire software lifecycle.Collected requirements from the clients and transformed it into business solutions.Provided innovative solutions and technologies for solving client requirements.Worked with Private and Government clients to provide par solutions to their business needs.Projects:Tourist Tracking System, Voice Mail System, Inventory Management SystemTechnologies used:Java, Spring, Hibernate, JSP, Android, Swing, Java Telephony API, Speech Synthesizer, DTMF, IVR, Google Map API, Geo-location, MySQL.Software Developer,10/2012-01/2015Smart Software Solutions, Inc–Sioux Falls,SD,Cooperated with other project partners to create application's system analysis based on client specifications.Integrated dynamic solution using futuristic technology like Augmented Reality in mobile application to address issues of students.Created and implemented HRMS software with modules for staff monitoring, administration, RFID attendance and report generation.Projects:AR Location Guide, Human Resource Management System (HRMS)Technologies used:Java, Augmented Reality, JEE, JSP, Spring MVC, Hibernate JavaScript, Ajax, jQuery, HTML, CSS, XML, MySQL, WireShark, Nmap, VA/PT, Windows, Linux.Network Support Engineer,04/2006-11/2008Interactive Brokers Llc–Washington,DC,Worked for three years installing,
configuring, maintaining and troubleshooting clients and ISP network
infrastructure.Actively participated in research and
development of new tools and techniques to use in the company.Technologies Used: CISCO,
Juniper, UBNT, Routers, Switches, ASA, ACL, DMZ, Linux, GNS, CACTI, MRTG.
Education and TrainingMaster of Science:Computer Science,Expected in-Maharishi University Of Management-Fairfield,IAGPA:Status-3.77GPA, expected completion 4/2019B.Sc (Hons):Computer Networking and IT Security,Expected in2012-London Metropolitan University-,GPA:Status-3.87GPA
```
</details>

<details>
<summary>Show Cleaned Resume</summary>

```text
SummarySkilled and technically qualified Java
developer with 7+ years of IT industry experience, building web, stand-alone and mobile applications.Adept at designing and developing both front-end and back-end systems with on demand technologies while implementing web services using Java, Spring, Hibernate, REST, SOAP, AWS, jQuery, AJAX, JSON and XML.Competent at  understanding requirements and converting
it to solutions in an Agile (Scrum) project development environment, while utilizing Application Security principles.
SkillsLanguages:
Java, JavaScript, Android, PythonWeb: Java EE, Servlets,
JSP, JSF, JavaScript, jQuery, AJAX, HTML5, CSS3, Bootstrap, AngularJSWeb Services: REST,
SOAP, JSON, XML, JMS, Google Map API, Twitter API, AWS, Cloud FoundryWeb/App Servers:
Tomcat, Glassfish, PivotalFrameworks: Spring, Hibernate, Swing, JSF, JDBC, JPA, GJTAPI, JMAPI, JSAPI, IVR, DTMFDatabases:
MySQL, NoSQL, MongoDB, HbaseBig Data: MR,
HDFS, Spark, Sqoop, Flume, Pig, HiveDesign Patterns:
Singleton, Prototype, Facade, Factory, MVC and other Java Design PatternsSDLC: Agile (Scrum, ), SSADM, USDP and othersTools: Maven, Git, Eclipse, IntelliJ, Android Studio, UML ToolsPlatforms:
Windows, Linux, Cloudera, BackTrack, AndroidNetworks & Security: Vulnerability
Assessment, Penetration Testing, CCNA, CCNA Security
Professional ExperienceJava Software Engineer,08/2017-CurrentWells Fargo Bank– ,Collaborated with team members to create and integrate high availability solutions for mission-critical applications.Assisted customers in resolving defects in the most effective manner.Prepared and presented design and technical proposals for clients.Project:Precision Dispatch System (PDS)Technologies used:Java, Swing, JMS, CORBA, SMI, XML, XSL, Oracle, Log4j, MVC, Git, Github, Eclipse, Rally, Confluence.Software Developer,02/2015-06/2016Smart Software Solutions, Inc– ,Successfully developed and supported projects across the entire software lifecycle.Collected requirements from the clients and transformed it into business solutions.Provided innovative solutions and technologies for solving client requirements.Worked with Private and Government clients to provide par solutions to their business needs.Projects:Tourist Tracking System, Voice Mail System, Inventory Management SystemTechnologies used:Java, Spring, Hibernate, JSP, Android, Swing, Java Telephony API, Speech Synthesizer, DTMF, IVR, Google Map API, Geo-location, MySQL.Software Developer,10/2012-01/2015Smart Software Solutions, Inc– ,Cooperated with other project partners to create application's system analysis based on client specifications.Integrated dynamic solution using futuristic technology like Augmented Reality in mobile application to address issues of students.Created and implemented HRMS software with modules for staff monitoring, administration, RFID attendance and report generation.Projects:AR Location Guide, Human Resource Management System (HRMS)Technologies used:Java, Augmented Reality, JEE, JSP, Spring MVC, Hibernate JavaScript, Ajax, jQuery, HTML, CSS, XML, MySQL, WireShark, /PT, Windows, Linux.Network Support Engineer,04/2006-11/2008Interactive Brokers Llc– ,Worked for three years installing,
configuring, maintaining and troubleshooting clients and ISP network
infrastructure.Actively participated in research and
development of new tools and techniques to use in the company.Technologies Used: CISCO,
Juniper, UBNT, Routers, Switches, ASA, ACL, DMZ, Linux, GNS, CACTI, MRTG.
Education and TrainingMaster of Science:Computer Science,Expected in-Maharishi University Of Management-Fairfield,IAGPA:Status-3.77GPA, expected completion 4/2019B.Sc (Hons):Computer Networking and IT Security,Expected in2012-London Metropolitan University-,GPA:Status-3.87GPA
```
</details>

### 💼 Job Description Text Comparison

<details>
<summary>Show Original Job Description</summary>

```text
A Senior Software Engineer at O'Reilly Auto Parts develops and supports applications for internal and external systems including Inventory, Supply Chain, eCommerce, Retail Applications, Enterprise Search and more. Our teams are focused on the development, design and integration of various software systems, databases, and third-party packages utilizing tools and technologies including Java, JavaScript, Spring, Hibernate, and SQL. This particular position will be a full stack role working on Warehouse Management Applications; however, we will consider anyone with Supply Chain Application Development experience.
The base salary for this position is $116,000-$145,000 annually plus a 10% Annual Bonus. Exact compensation will be determined based on experience, however mid point around $126,000 - $131,000 would be more practical.
What You'll Do:Partner with key stakeholders to develop new features and enhance and support existing applications and programs.Work with business systems analysts and stakeholders to translate business to technical requirements and problem solve.Collaborate with project teams and cross functional teams to troubleshoot open issues and bug-fixes.Collaborate, coach and mentor team members on best practices, code reviews, internal tools, and process improvements.Write and maintain readable, sustainable, and efficient code in highly optimized and scalable architectures.Own applications from conception and design, to implementation and support.Debug and test code as needed.Create and update advanced technical documentation.
Skills and QualificationsRequired:High School diploma or equivalent.10+ years of software development experience.Strong knowledge of software engineering best practices of the full software development life cycle, including coding standards, code reviews, source control, testing, build and release engineering processes with focus on automation and end to end traceability.Experience in Java, Spring Boot, SQL Databases, and HibernateWorking understanding of databases including writing and amending queries in Oracle, SQL, PostgreSQL andor NoSQL.Experience working in DevOps including continuous integration and continuous deployment using open source technologies like GIT, Jenkins, JIRA and Confluence.Experience in effectively communicating with a broad base of end users and multiple management layers, including the ability to interact with vendors as needed.Ability to lead and mentor junior developer and effectively communicate with members of the team.Ability to work flexible schedule including nightsweekends.
Desired:Bachelor's degree in computer science or equivalent experience.Ability to articulate advanced technical concepts and teach others.Experience working with AgileScrum methodology.Experience in Microservice Architecture, Kubernetes, Containerization, MongoDB, SOLRExperience working in a remote, virtual or work-from-home environment.
Location: Remote, USA - This role can be remote, virtual or work-from-home anywhere in the United States.
 About UsO'Reilly Auto Parts IT department provides services to our corporate office, 6000+ stores, 28 distribution centers and 85,000 + team members.We have over 900 IT team members supporting 250+ small, medium and large web and software applications in addition to third party packages.We provide a collaborative environment and encourage knowledge sharingWe respect a healthy work-life balanceOur teams keep open communication through video conferencing, team messaging and daily stand-upsOur leadership values collaboration and encourages team members to bring creative problem-solving ideas from both a technical and functional perspectiveWe have several career paths, whether you want to be an individual contributor, manager, project manager, or stay technical - there's a documented growth plan to help you follow the path you chooseWe want to grow our people - we help to make you better by providing training for both technical and professional development
```
</details>

<details>
<summary>Show Cleaned Job Description</summary>

```text
A Senior Software Engineer at O'Reilly Auto Parts develops and supports applications for internal and external systems including Inventory, Supply Chain, eCommerce, Retail Applications, Enterprise Search and more. Our teams are focused on the development, design and integration of various software systems, databases, and third-party packages utilizing tools and technologies including Java, JavaScript, Spring, Hibernate, and SQL. This particular position will be a full stack role working on Warehouse Management Applications; however, we will consider anyone with Supply Chain Application Development experience.
The base salary for this position is $116,000-$145,000 annually plus a 10% Annual Bonus. Exact compensation will be determined based on experience, however mid point around $126,000 - $131,000 would be more practical.
What You'll Do:Partner with key stakeholders to develop new features and enhance and support existing applications and programs.Work with business systems analysts and stakeholders to translate business to technical requirements and problem solve.Collaborate with project teams and cross functional teams to troubleshoot open issues and bug-fixes.Collaborate, coach and mentor team members on best practices, code reviews, internal tools, and process improvements.Write and maintain readable, sustainable, and efficient code in highly optimized and scalable architectures.Own applications from conception and design, to implementation and support.Debug and test code as needed.Create and update advanced technical documentation.
Skills and QualificationsRequired:High School diploma or equivalent.10+ years of software development experience.Strong knowledge of software engineering best practices of the full software development life cycle, including coding standards, code reviews, source control, testing, build and release engineering processes with focus on automation and end to end traceability.Experience in Java, Spring Boot, SQL Databases, and HibernateWorking understanding of databases including writing and amending queries in Oracle, SQL, PostgreSQL andor NoSQL.Experience working in DevOps including continuous integration and continuous deployment using open source technologies like GIT, Jenkins, JIRA and Confluence.Experience in effectively communicating with a broad base of end users and multiple management layers, including the ability to interact with vendors as needed.Ability to lead and mentor junior developer and effectively communicate with members of the team.Ability to work flexible schedule including nightsweekends.
Desired:Bachelor's degree in computer science or equivalent experience.Ability to articulate advanced technical concepts and teach others.Experience working with AgileScrum methodology.Experience in Microservice Architecture, Kubernetes, Containerization, MongoDB, SOLRExperience working in a remote, virtual or work-from-home environment.
Location: Remote, USA - This role can be remote, virtual or work-from-home anywhere in the United States.
 About UsO'Reilly Auto Parts IT department provides services to our corporate office, 6000+ stores, 28 distribution centers and 85,000 + team members.We have over 900 IT team members supporting 250+ small, medium and large web and software applications in addition to third party packages.We provide a collaborative environment and encourage knowledge sharingWe respect a healthy work-life balanceOur teams keep open communication through video conferencing, team messaging and daily stand-upsOur leadership values collaboration and encourages team members to bring creative problem-solving ideas from both a technical and functional perspectiveWe have several career paths, whether you want to be an individual contributor, manager, project manager, or stay technical - there's a documented growth plan to help you follow the path you chooseWe want to grow our people - we help to make you better by providing training for both technical and professional development
```
</details>

---

## Sample 4 (Original Row Index: 5394)

- **Label:** `Good Fit` ➔ `Fit`
- **Before Lengths:** Resume = 5336 chars, JD = 4113 chars
- **After Lengths:** Resume = 5286 chars, JD = 4101 chars

### 📄 Resume Text Comparison

<details>
<summary>Show Original Resume</summary>

```text
Professional ProfileExpert in Functional Testing .6-Year Record of Proven ResultsSenior software QA testerwith full system development life cycle experience, including designing, developing and implementing test plans, high level calendar test cases and test processes with attention to detail resulting in high quality Change Request and production change implementationsHands-on technology professionalaccustomed to working in complex, project-based environments. Multifaceted experience in QA software testing, system testing, user-acceptance testing and production certification testing.Backed by strong credentialsincluding a Bachelor's degree, certificate in business management and advanced command of various testing tools, agile methodologies and cross-platform skills in Windows, and Unix.
Summary of SkillsTest Plans, Cases & ProcessesFunctional RequirementsDocumentationScrum/Agile MethodologiesUI & Compatibility TestingTest strategiesDefect / Bug TrackingUAT and System TestingTesting AutomationRegression & negative testingData interface and migration testing
EducationAll India Institute of Management StudiesChennai,Expected inMarch 1999––Diploma:Business Management-GPA:Business ManagementL.A.D College of Commerce and ScienceNagpur,Expected inJune 1997––Bachelor of Commerce:Accounting-GPA:Accounting
ExperienceGeneral Dynamics-Senior Software Quality Assurance TesterPatuxent River,MD,07/2014-CurrentServe as a key member of Quality Assurance team for a leading Amdocs telecom customer (T-Mobile).Worked on various front end Amdocs modules including web, CRM, ordering and billing.Key responsibilities include Testing of APIs, Web, widgets and batch jobs (Unix) across modules as part of the system test/Production testing teamsCreate test designs and execute software test plans, cases and scripts to uncover, identify defects in parallel to UATDocument software defects using bug tracking system(QC/ALM) and report defects involving program functionality, output, online screen and content to software developersData creation and analysis.Validation of XML data in the outcome of testing as per business requirementsLogs validations in batch Hotfix (patch) packages testing to productionIdentified and pointed out design gaps during testing of major CRs. Communicated effectively with developers and became a 'go-to-tester' for challenging test cases.Certified patches to productionDeliver QA reports and statuses as requiredPost release production sanity testing during releases identifying defects in productionConduct formal high level calendar design reviews with Customer IT operations  and business groupsProvide knowledge transfer to offshore/peers.Pae Government Services Inc-QA Tester (Senior SME)Camp Lejeune,NC,08/2013-07/2014Worked across testing various Amdocs applications for a leading Amdocs customer (Metro) like API, Payment module, ordering (ASAP).Key member in the production testing team holding following responsibilities:-Production hotfix patch testing for front end and batch applications.Was instrumental in identifying critical escaping defects to production during new release sanity and became a key tester for major new releases.Galaxy Solutions-QA Tester (Senior SME)Nashville,TN,04/2011-08/2013Part of the Change Request testing teamLearned very quickly to become a key iCare(CRM)testing team member which was the latest Amdocs CRM release and a major upgrade for the client.Designed test calendars  and test cases designTest calendar reviews with internal development teams and client as requiredAssisted with user-acceptance testing and defect tracking for  new software releases.Provided recommendations for resolving defects.Executed regression suite adding new test cases based on lessons learnt from production and also from new Change requestsPart of Automation team creating Amdocs iCare module automation test cases using QTP.AMDOCS-Operations SchedulerCity,STATE,07/2010-04/2011As a new team member in the operations group quickly learned all the operational tools available to run billing operations for one of the largest Amdocs customers.Became one of the dependable team member individually managing batch operations and critical billing runs with millions of subscribersValidate checklist prior to batch End of Day runsPrepare and build MAPs to run End of Day and other batch jobs Run scheduler and check job logs.Provide first level of triage to jobs failing in production.Follow escalation procedures in place to get development involved and resolve production job failures in a timely mannerProvide reports on job failure/success report trendsMaintain issues list each day and follow up with development teams including action items.ACCENTURE-QA TesterCity,STATE,11/2006-06/2007Analyzed and interpreted test data and prepared technical reports.Prepared detailed test cases by understanding the business logic and user requirements for testingDocumented the test cases in Testing tool Prepared and executed test cases manually for different modulesResponsible for development of test plan and test cases and checking the screens for Quality AssuranceValidated the application according to client requirementsIdentified errors, issues and documented the defects.
Technical SkillsHP Quality Center, SoapUI, SQL, XML,
Windows, Linux, Unix, QTP. Understanding of C, C++
```
</details>

<details>
<summary>Show Cleaned Resume</summary>

```text
Professional ProfileExpert in Functional Testing .6-Year Record of Proven ResultsSenior software QA testerwith full system development life cycle experience, including designing, developing and implementing test plans, high level calendar test cases and test processes with attention to detail resulting in high quality Change Request and production change implementationsHands-on technology professionalaccustomed to working in complex, project-based environments. Multifaceted experience in QA software testing, system testing, user-acceptance testing and production certification testing.Backed by strong credentialsincluding a Bachelor's degree, certificate in business management and advanced command of various testing tools, agile methodologies and cross-platform skills in Windows, and Unix.
Summary of SkillsTest Plans, Cases & ProcessesFunctional RequirementsDocumentationScrum/Agile MethodologiesUI & Compatibility TestingTest strategiesDefect / Bug TrackingUAT and System TestingTesting AutomationRegression & negative testingData interface and migration testing
EducationAll India Institute of Management StudiesChennai,Expected inMarch 1999––Diploma:Business Management-GPA:Business ManagementL.A.D College of Commerce and ScienceNagpur,Expected inJune 1997––Bachelor of Commerce:Accounting-GPA:Accounting
ExperienceGeneral Dynamics-Senior Software Quality Assurance ,07/2014-CurrentServe as a key member of Quality Assurance team for a leading Amdocs telecom customer (T-Mobile).Worked on various front end Amdocs modules including web, CRM, ordering and billing.Key responsibilities include Testing of APIs, Web, widgets and batch jobs (Unix) across modules as part of the system test/Production testing teamsCreate test designs and execute software test plans, cases and scripts to uncover, identify defects in parallel to UATDocument software defects using bug tracking system(QC/ALM) and report defects involving program functionality, output, online screen and content to software developersData creation and analysis.Validation of XML data in the outcome of testing as per business requirementsLogs validations in batch Hotfix (patch) packages testing to productionIdentified and pointed out design gaps during testing of major CRs. Communicated effectively with developers and became a 'go-to-tester' for challenging test cases.Certified patches to productionDeliver QA reports and statuses as requiredPost release production sanity testing during releases identifying defects in productionConduct formal high level calendar design reviews with Customer IT operations and business groupsProvide knowledge transfer to offshore/peers.Pae Government Services Inc-QA Tester (Senior SME) ,08/2013-07/2014Worked across testing various Amdocs applications for a leading Amdocs customer (Metro) like API, Payment module, ordering (ASAP).Key member in the production testing team holding following responsibilities:-Production hotfix patch testing for front end and batch applications.Was instrumental in identifying critical escaping defects to production during new release sanity and became a key tester for major new releases.Galaxy Solutions-QA Tester (Senior SME) ,04/2011-08/2013Part of the Change Request testing teamLearned very quickly to become a key iCare(CRM)testing team member which was the latest Amdocs CRM release and a major upgrade for the client.Designed test calendars  and test cases designTest calendar reviews with internal development teams and client as requiredAssisted with user-acceptance testing and defect tracking for new software releases.Provided recommendations for resolving defects.Executed regression suite adding new test cases based on lessons learnt from production and also from new Change requestsPart of Automation team creating Amdocs iCare module automation test cases using QTP.AMDOCS-Operations SchedulerCity,STATE,07/2010-04/2011As a new team member in the operations group quickly learned all the operational tools available to run billing operations for one of the largest Amdocs customers.Became one of the dependable team member individually managing batch operations and critical billing runs with millions of subscribersValidate checklist prior to batch End of Day runsPrepare and build MAPs to run End of Day and other batch jobs Run scheduler and check job logs.Provide first level of triage to jobs failing in production.Follow escalation procedures in place to get development involved and resolve production job failures in a timely mannerProvide reports on job failure/success report trendsMaintain issues list each day and follow up with development teams including action items.ACCENTURE-QA TesterCity,STATE,11/2006-06/2007Analyzed and interpreted test data and prepared technical reports.Prepared detailed test cases by understanding the business logic and user requirements for testingDocumented the test cases in Testing tool Prepared and executed test cases manually for different modulesResponsible for development of test plan and test cases and checking the screens for Quality AssuranceValidated the application according to client requirementsIdentified errors, issues and documented the defects.
Technical SkillsHP Quality Center, SoapUI, SQL, XML,
Windows, Linux, Unix, QTP. Understanding of C, C++
```
</details>

### 💼 Job Description Text Comparison

<details>
<summary>Show Original Job Description</summary>

```text
Who We Are
Apex Fintech Solutions (AFS) powers innovation and the future of digital wealth management by processing millions of transactions daily, to simplify, automate, and facilitate access to financial markets for all. Our robust suite of fintech solutions enables us to support clients such as Stash, Betterment, SoFi, and WeBull, and more than 20 million of our clients' customers.
Collectively, AFS creates an environment in which companies with the biggest ideas in fintech are empowered to change the world. We are based in Dallas, TX and also have offices in Austin, New York, Chicago, Portland, and Belfast.
If you are seeking a fast-paced and entrepreneurial environment where you'll have the opportunity to make an immediate impact, and you have the guts to change everything, this is the place for you.
AFS has received a number of prestigious industry awards, including:
2021, 2020, 2019, and 2018 Best Wealth Management Company - presented by Fintech Breakthrough Awards2021 Most Innovative Companies - presented by Fast Company2021 Best API & Best Trading Technology - presented by Global Fintech Awards
About This Role
As a Principal Cloud Software Engineer at Apex Silver, you are responsible for design and development of software code. You will help lead other developers in the design and development of financial services applications that integrate with cloud-based services. You are a results oriented leader who can lead a team to exceed client expectations. You perform hands-on work required to meet service level requirements. You will lead by example.
Key Responsibilities
Coordinate with your cross functional product development team and members of the software development teamOversee and provide guidance to other development team membersDesign and develop highly performant large scale financial services applicationsImplement robust CICD processesAdhere to Silvers coding standardsKeep up-to-date with industry trends and technology developments
Skills & Requirements
Requires a bachelor's degree (or equivalent experience) and at least 10 years of experienceExtensive knowledge of software development processesExtensive knowledge of bash shell scriptingExtensive knowledge of implementing serverless solutions using AWS lambda, SQS, EventBridgeExtensive knowledge of Cloud Databases: AWS RDSAurora, DynamoDBExtensive knowledge of Infrastructure-as-Code deployment tools like CloudFormation templates, TerraformExtensive knowledge of AWS Cloud Technologies (EC2, RDS, Amazon MQ, S3, API Gateway, etc.)Extensive knowledge of bash shell scriptingExtensive knowledge of CICD processes and tools like like BitBucket and PipelinesKnowledge of Java and SQLSolid experience in coding object oriented softwareKnowledge of javascript and front-end web frameworksPossess strong knowledge of fintech, investment services clearingcustody, best practices, and proceduresExcellent communication, organizational, analytical and team building skillsLead and direct the work of others Demonstrates strong problem solving skills, process driven mindset, resourcefulness, and the ability to meet responsibilities with minimal direct oversight
#engineering #mid-senior #full-time
OUR REWARDS
We offer a robust package of employee perks and benefits, including healthcare benefits (medical, dental and vision, EAP), competitive PTO, 401k match, parental leave, and HSA contribution match. We also provide our employees with a paid subscription to the Calm app and offer generous external learning and tuition reimbursement benefits. At AFS, we offer a hybrid work schedule for most roles that allows employees to have the flexibility of working from home and one of our primary offices.
AFS is committed to creating a diverse environment and is proud to be an equal opportunity employer. All qualified applicants will receive consideration for employment without regard to race, color, religion, gender, gender identity or expression, sexual orientation, national origin, natural or protective hairstyle, genetics, disability, age, or any other basis forbidden under federal, state, or local law.

```
</details>

<details>
<summary>Show Cleaned Job Description</summary>

```text
Who We Are
Apex Fintech Solutions (AFS) powers innovation and the future of digital wealth management by processing millions of transactions daily, to simplify, automate, and facilitate access to financial markets for all. Our robust suite of fintech solutions enables us to support clients such as Stash, Betterment, SoFi, and WeBull, and more than 20 million of our clients' customers.
Collectively, AFS creates an environment in which companies with the biggest ideas in fintech are empowered to change the world. We are based in and also have offices in Austin, New York, Chicago, Portland, and Belfast.
If you are seeking a fast-paced and entrepreneurial environment where you'll have the opportunity to make an immediate impact, and you have the guts to change everything, this is the place for you.
AFS has received a number of prestigious industry awards, including:
2021, 2020, 2019, and 2018 Best Wealth Management Company - presented by Fintech Breakthrough Awards2021 Most Innovative Companies - presented by Fast Company2021 Best API & Best Trading Technology - presented by Global Fintech Awards
About This Role
As a Principal Cloud Software Engineer at Apex Silver, you are responsible for design and development of software code. You will help lead other developers in the design and development of financial services applications that integrate with cloud-based services. You are a results oriented leader who can lead a team to exceed client expectations. You perform hands-on work required to meet service level requirements. You will lead by example.
Key Responsibilities
Coordinate with your cross functional product development team and members of the software development teamOversee and provide guidance to other development team membersDesign and develop highly performant large scale financial services applicationsImplement robust CICD processesAdhere to Silvers coding standardsKeep up-to-date with industry trends and technology developments
Skills & Requirements
Requires a bachelor's degree (or equivalent experience) and at least 10 years of experienceExtensive knowledge of software development processesExtensive knowledge of bash shell scriptingExtensive knowledge of implementing serverless solutions using AWS lambda, SQS, EventBridgeExtensive knowledge of Cloud Databases: AWS RDSAurora, DynamoDBExtensive knowledge of Infrastructure-as-Code deployment tools like CloudFormation templates, TerraformExtensive knowledge of AWS Cloud Technologies (EC2, RDS, Amazon MQ, S3, API Gateway, etc.)Extensive knowledge of bash shell scriptingExtensive knowledge of CICD processes and tools like like BitBucket and PipelinesKnowledge of Java and SQLSolid experience in coding object oriented softwareKnowledge of javascript and front-end web frameworksPossess strong knowledge of fintech, investment services clearingcustody, best practices, and proceduresExcellent communication, organizational, analytical and team building skillsLead and direct the work of others Demonstrates strong problem solving skills, process driven mindset, resourcefulness, and the ability to meet responsibilities with minimal direct oversight
#engineering #mid-senior #full-time
OUR REWARDS
We offer a robust package of employee perks and benefits, including healthcare benefits (medical, dental and vision, EAP), competitive PTO, 401k match, parental leave, and HSA contribution match. We also provide our employees with a paid subscription to the Calm app and offer generous external learning and tuition reimbursement benefits. At AFS, we offer a hybrid work schedule for most roles that allows employees to have the flexibility of working from home and one of our primary offices.
AFS is committed to creating a diverse environment and is proud to be an equal opportunity employer. All qualified applicants will receive consideration for employment without regard to race, color, religion, gender, gender identity or expression, sexual orientation, national origin, natural or protective hairstyle, genetics, disability, age, or any other basis forbidden under federal, state, or local law.
```
</details>

---

## Sample 5 (Original Row Index: 999)

- **Label:** `No Fit` ➔ `No Fit`
- **Before Lengths:** Resume = 6942 chars, JD = 1791 chars
- **After Lengths:** Resume = 6768 chars, JD = 1779 chars

### 📄 Resume Text Comparison

<details>
<summary>Show Original Resume</summary>

```text
ProfileDedicated Epidemiologist/Data Manager with excellent technical, analytical and communication skills demonstrated by 17 years of experience.Experienced professional with strong leadership and relationship-building skills.
SkillsSAS Statistical Software,SAS-AF Software,Project ManagementProgramming skills
Education and TrainingThe George Washington UniversityWashington,DCExpected inDecember 2003––MASTER OF PUBLIC HEALTH (EPIDEMIOLOGY):Epidemiology-GPA:Research Project: Impact of Ethnicity on the Delivery of Cardiac Care in a Large Urban HospitalHAMPTONUNIVERSITYHampton,VAExpected inAugust 1994––Master of Arts:Biology-GPA:NORFOLK STATE UNIVERSITYNorfolk,VAExpected inMay 1992––Bachelor of Science:BIOLOGY-GPA:
Professional ExperienceEdelman-DIRECTOR, DATA MANAGEMENT & ANALYSISNew York,NY,07/2014-CurrentManage and direct all aspects of health outcomes research projects involving medical chart abstraction, including protocol development, IRB submission, site enrollment/management, chart abstraction, and data management/analysisConcurrently maintain more than 10 client relationships among research, pharmaceutical, and continuing education companies and managed care organizations.Provide research direction to clients and internal staff for timely and effective completion of more than 30 outcomes research projects.Support, grow and lead a team of 12 Clinical Managers, Data Managers and Physician Recruiters to deliver outcomes research services.Developed strategies to enhance provider engagement and improve project success, including staff incentives and process improvement plans.Perform quality audits of staff performance and product delivery for services.Conduct data analysis using SAS to provide baseline and final study  reports.Rochester General Health System-RESEARCH MANAGERWilliamson,NY,03/2013-07/2014Responsible for database management, data cleaning and analysis of health outcomes research studies.Use SAS programming and other database tools to check study data for inconsistencies or missing data.Work with Clinical Managers and Outreach staff to ensure accurate data capture, in order to provide clients with clean and reliable data.Aleut Support Services Llc - Main-PROJECT SET-UP MANAGERTexarkana,AR,09/2012-04/2013Manage the process of designing and launching single region, global/regional clinical research studies through protocol review and implementation.Lead the activities of the Sponsor/Clinical Research Organization (CRO), and guide the Project Manager and Set-up Coordinators in designing and organizing project components.Dartmouth College-DATA MANAGER/EPIDEMIOLOGISTHanover,NH,11/2015-09/2012Responsible for the management, cleaning and updating of data for the Cancer Prevention Study-II (CPS-II) and the Cancer Prevention Study-3 (CPS-3), two of the largest longitudinal studies following cohorts of the general population looking for risks factors for various cancers.Developed the database design requirements for the CPS-II Parkinson's and ALS study databases.Independently manage projects involving study participants, including database administration, data editing, uploading and maintenance, as well as resolution of data problems as they arise.Responsible for the implementation and maintenance of Abstract Plus software and databases for use by Cancer Tumor Registrars.Coordinated a team to review survey design and implement changes for new survey questions.Incorporate epidemiologic and biostatistical methods in order to provide analysis and reports for Principal Investigators.Communicate with participants to ensure all concerns regarding the study and its procedures are explained and to maintain retention of participants.Albert Einstein College Of Medicine-DATA MANAGERBronx,NY,06/2015-10/2015Performed database management, analysis and reporting for financial and descriptive purposes.Wrote business plan and operating agreement utilized to outline company affairs.Responsible for documenting monthly billing and account receivables.22Nd Century Technologies-RESEARCH ASSOCIATEBrownsville,TX,05/2003-04/2004Assisted in database management, data auditing and analysis for the Prevention of Events with Angiotensin Converting Enzyme Inhibition (PEACE) Study, a large multi-center trial in cardiovascular health.Programmed and ran edit checks on study data to look for inconsistencies or missing data.Monitored clinical sites in the United States, Canada and Italy to ensure adherence to study protocol and quality of data.Resolved data discrepancies by reviewing patient records and effectively communicating and coordinating with external clients.Prepared ad-hoc reports and analyses as deemed necessary.Bd (Becton, Dickinson And Company)-EPIDEMIOLOGISTGlens Falls,NY,2003-05/2003Served as the lead analyst for collaboration between The George Washington University and Minority Health Communications to prepare a publication of the leading causes of death and mortality rates at the zip code level for each state in the United States.Utilized SAS statistical software to calculate age-adjusted standardized premature mortality rates at the zip code level for major US cities.Collaborated with Geographic Information System (GIS) mappers to place premature mortality rates on maps for review and action by government officials and policymakers.Boundless Networks-CLINICAL DATA ANALYST IIPhoenix,AZ,01/1-01/1Designed and implemented Data Management Plan for a major pharmaceutical firm's key study, resulting in the acquisition of a strategic account for the company.Performed data comparisons, data edit checks and data auditing for clinical trial projects, resulting in 99.9% data accuracy.Maintained clinical trial data accuracy through review and analysis of case report forms.St. Louis Arc-CLINICAL DATA COORDINATORAffton,MO,01/1-01/1Designed, developed and managed clinical trial databases using SAS Programming.Conducted data comparisons, edit checks and auditing for clinical trial projects.Queried data inconsistencies and revised case report forms in compliance with operating procedures, client guidelines and regulatory agency procedures.UNIVERSITY OF MICHIGAN-PROGRAM COORDINATORCity,STATE,01/1-01/1Successfully recruited corporate partners for expansion of internship program, resulting in 50% increase in student participants.Supervised student support staff from seven departments.Oversaw summer and Saturday engineering program for high school students from across the country.UNIVERSITY OF NORTH CAROLINA - CHARLOTTE-ASSISTANT COORDINATORCity,STATE,01/1-01/1MATH AND SCIENCE EDUCATION NETWORK.Coordinated enrichment activities in math and science for students in grades 7-12.Proposed ways to increase student retention by providing more class selections and by increasing student participation through internships.Initiated method to evaluate program success through surveys.
SkillsClient Management, Data management/analysis, Outcomes Research, SAS.
```
</details>

<details>
<summary>Show Cleaned Resume</summary>

```text
ProfileDedicated Epidemiologist/Data Manager with excellent technical, analytical and communication skills demonstrated by 17 years of experience.Experienced professional with strong leadership and relationship-building skills.
SkillsSAS Statistical Software,SAS-AF Software,Project ManagementProgramming skills
Education and TrainingThe George Washington UniversityWashington,DCExpected inDecember 2003––MASTER OF PUBLIC HEALTH (EPIDEMIOLOGY):Epidemiology-GPA:Research Project: Impact of Ethnicity on the Delivery of Cardiac Care in a Large Urban HospitalHAMPTONUNIVERSITYHampton,VAExpected inAugust 1994––Master of Arts:Biology-GPA:NORFOLK STATE UNIVERSITYNorfolk,VAExpected inMay 1992––Bachelor of Science:BIOLOGY-GPA:
Professional ExperienceEdelman-DIRECTOR, DATA MANAGEMENT & ,07/2014-CurrentManage and direct all aspects of health outcomes research projects involving medical chart abstraction, including protocol development, IRB submission, site enrollment/management, chart abstraction, and data management/analysisConcurrently maintain more than 10 client relationships among research, pharmaceutical, and continuing education companies and managed care organizations.Provide research direction to clients and internal staff for timely and effective completion of more than 30 outcomes research projects.Support, grow and lead a team of 12 Clinical Managers, Data Managers and Physician Recruiters to deliver outcomes research services.Developed strategies to enhance provider engagement and improve project success, including staff incentives and process improvement plans.Perform quality audits of staff performance and product delivery for services.Conduct data analysis using SAS to provide baseline and final study reports.Rochester General Health System-RESEARCH ,03/2013-07/2014Responsible for database management, data cleaning and analysis of health outcomes research studies.Use SAS programming and other database tools to check study data for inconsistencies or missing data.Work with Clinical Managers and Outreach staff to ensure accurate data capture, in order to provide clients with clean and reliable data.Aleut Support Services Llc - Main-PROJECT SET- ,09/2012-04/2013Manage the process of designing and launching single region, global/regional clinical research studies through protocol review and implementation.Lead the activities of the Sponsor/Clinical Research Organization (CRO), and guide the Project Manager and Set-up Coordinators in designing and organizing project components.Dartmouth College-DATA MANAGER/ ,11/2015-09/2012Responsible for the management, cleaning and updating of data for the Cancer Prevention Study-II (CPS-II) and the Cancer Prevention Study-3 (CPS-3), two of the largest longitudinal studies following cohorts of the general population looking for risks factors for various cancers.Developed the database design requirements for the CPS-II Parkinson's and ALS study databases.Independently manage projects involving study participants, including database administration, data editing, uploading and maintenance, as well as resolution of data problems as they arise.Responsible for the implementation and maintenance of Abstract Plus software and databases for use by Cancer Tumor Registrars.Coordinated a team to review survey design and implement changes for new survey questions.Incorporate epidemiologic and biostatistical methods in order to provide analysis and reports for Principal Investigators.Communicate with participants to ensure all concerns regarding the study and its procedures are explained and to maintain retention of participants.Albert Einstein College Of Medicine- ,06/2015-10/2015Performed database management, analysis and reporting for financial and descriptive purposes.Wrote business plan and operating agreement utilized to outline company affairs.Responsible for documenting monthly billing and account receivables.22Nd Century Technologies-RESEARCH ,05/2003-04/2004Assisted in database management, data auditing and analysis for the Prevention of Events with Angiotensin Converting Enzyme Inhibition (PEACE) Study, a large multi-center trial in cardiovascular health.Programmed and ran edit checks on study data to look for inconsistencies or missing data.Monitored clinical sites in the United States, Canada and Italy to ensure adherence to study protocol and quality of data.Resolved data discrepancies by reviewing patient records and effectively communicating and coordinating with external clients.Prepared ad-hoc reports and analyses as deemed necessary.Bd (Becton, Dickinson And Company)-EPIDEMIOLOGISTGlens ,2003-05/2003Served as the lead analyst for collaboration between The George Washington University and Minority Health Communications to prepare a publication of the leading causes of death and mortality rates at the zip code level for each state in the United States.Utilized SAS statistical software to calculate age-adjusted standardized premature mortality rates at the zip code level for major US cities.Collaborated with Geographic Information System (GIS) mappers to place premature mortality rates on maps for review and action by government officials and policymakers.Boundless Networks-CLINICAL DATA ,01/1-01/1Designed and implemented Data Management Plan for a major pharmaceutical firm's key study, resulting in the acquisition of a strategic account for the company.Performed data comparisons, data edit checks and data auditing for clinical trial projects, resulting in 99.9% data accuracy.Maintained clinical trial data accuracy through review and analysis of case report forms.St. Louis Arc-CLINICAL DATA ,01/1-01/1Designed, developed and managed clinical trial databases using SAS Programming.Conducted data comparisons, edit checks and auditing for clinical trial projects.Queried data inconsistencies and revised case report forms in compliance with operating procedures, client guidelines and regulatory agency procedures.UNIVERSITY OF MICHIGAN-PROGRAM COORDINATORCity,STATE,01/1-01/1Successfully recruited corporate partners for expansion of internship program, resulting in 50% increase in student participants.Supervised student support staff from seven departments.Oversaw summer and Saturday engineering program for high school students from across the country.UNIVERSITY OF NORTH CAROLINA - CHARLOTTE-ASSISTANT COORDINATORCity,STATE,01/1-01/1MATH AND SCIENCE EDUCATION NETWORK.Coordinated enrichment activities in math and science for students in grades 7-12.Proposed ways to increase student retention by providing more class selections and by increasing student participation through internships.Initiated method to evaluate program success through surveys.
SkillsClient Management, Data management/analysis, Outcomes Research, SAS.
```
</details>

### 💼 Job Description Text Comparison

<details>
<summary>Show Original Job Description</summary>

```text
Are you passionate about the clean tech automotive industry? Looking to make an impact with an global automotive company?
Our client is on a mission to provide innovative energy management solutions for electric and conventional vehicles. They are actively growing their team in the US, and they are looking for a SeniorLead Software Engineer who'd love to make an impact and help them pave a way to a more sustainable future!

What You'll Be Doing:Develop & debug real-time firmware in C for automotive microcontrollers.Assist in the design and development of control software for versatile actuators and valves, including BLDC motor, brushed DC motor controls, electronic valves, and sensors.Wok with hardware engineers to debug electronic circuit designs and develop firmware to support those designs.Participate in the full product development cycle from specification to release.Work collaboratively with cross-functional teams to ensure all software meets performance specifications and requirements.Mentor other junior developers with your technical expertise.
Requirements:Bachelor's or Master's Degree in Computer Science, Computer Engineering, or Electrical Engineering5+ years of experience working in firmware and embedded software design.Strong C Programming and embedded firmware development experience for microcontrollers.Strong ASPICE experience.Familiarity with LIN and CAN automotive protocols and Vector testing tools
Why You'll Love This Opportunity:$100-130k base salary + bonus!Hybrid working environment, based in the Detroit, MI area!Growth opportunities, they love to promote within!Amazing PTO Package, full medical & dental, and 401k match!Relocation package & Visa sponsorship if needed!Work with an amazing team and make a difference in the automotive industry!
```
</details>

<details>
<summary>Show Cleaned Job Description</summary>

```text
Are you passionate about the clean tech automotive industry? Looking to make an impact with an global automotive company?
Our client is on a mission to provide innovative energy management solutions for electric and conventional vehicles. They are actively growing their team in the US, and they are looking for a SeniorLead Software Engineer who'd love to make an impact and help them pave a way to a more sustainable future!

What You'll Be Doing:Develop & debug real-time firmware in C for automotive microcontrollers.Assist in the design and development of control software for versatile actuators and valves, including BLDC motor, brushed DC motor controls, electronic valves, and sensors.Wok with hardware engineers to debug electronic circuit designs and develop firmware to support those designs.Participate in the full product development cycle from specification to release.Work collaboratively with cross-functional teams to ensure all software meets performance specifications and requirements.Mentor other junior developers with your technical expertise.
Requirements:Bachelor's or Master's Degree in Computer Science, Computer Engineering, or Electrical Engineering5+ years of experience working in firmware and embedded software design.Strong C Programming and embedded firmware development experience for microcontrollers.Strong ASPICE experience.Familiarity with LIN and CAN automotive protocols and Vector testing tools
Why You'll Love This Opportunity:$100-130k base salary + bonus!Hybrid working environment, based in the area!Growth opportunities, they love to promote within!Amazing PTO Package, full medical & dental, and 401k match!Relocation package & Visa sponsorship if needed!Work with an amazing team and make a difference in the automotive industry!
```
</details>

---

## Sample 6 (Original Row Index: 1770)

- **Label:** `No Fit` ➔ `No Fit`
- **Before Lengths:** Resume = 5259 chars, JD = 2422 chars
- **After Lengths:** Resume = 5242 chars, JD = 2420 chars

### 📄 Resume Text Comparison

<details>
<summary>Show Original Resume</summary>

```text
Professional SummaryTo achieve a responsible position that gives me a chance to apply my innovative skills and knowledge. I aim to be a valuable member of the team that works dynamically towards success and growth of organization. Strong Knowledge in Electronics and computer Engineering background with 1+ experience as Automotive Embedded Software Engineer. Good Knowledge in simulation tools such as MATLAB and Simulink. Thorough Knowledge in CAN Communication and Basic knowledge in AUTOSAR Architecture. Familiar with Version control systems such as SVN, IBM Synergy, Clear case and requirements analysis tools such as Doors. Worked on all phases of V model software development and Version control systems. Communicated with the other Engineering personnel to coordinate the interrelated design and assure project completion. Coordinating with software and target teams to find bugs, testing debug build.
SkillsGuest servicesInventory control proceduresMerchandising expertiseLoss preventionCash register operationsProduct promotions
EducationNorthwestern Polytechnic University,CA.Expected inJan'16––M.S:Electrical and Computer Engineering-GPA:3.6Electrical and Computer Engineering 3.6Jawaharlal Nehru Institute of Technology,Expected inMay'14––Bachelors:Electronics and communication Engineering-GPA:3.4Electronics and communication Engineering 3.4
Work HistoryOneblood-Embedded SoftwareDeland,,India01/2016-07/2016Responsible for developing Safety and Engine related software.Special focus on areas such as CAN protocols.Embedded software component development for Engine ECU, and maintenance of existing software components.Supported all phases of the software development process (V - Model).Understand and negotiate specifications, designed and implemented code, created documents and descriptions maintained existing software.Stored, retrieved and manipulated data for close analysis of system capabilities.Prepared detailed reports concerning project specifications and activities.Worked effectively with design teams to ensure software solutions elevated client side experience.Defense Electronics Research Laboratory DLRL-Project TraineeCity,STATE,India11/2012-04/2013Undergone a training program in Industrial Automation, which gives a hands on experience in 8051 programming, AVR programming for Embedded Systems applications, Digital logic and Electronic Control, using commonly used transducers, sensors and output devices and components in automation and controlling.Projects Fault Management, TCS, India Responsible for development and testing of Fault management module.It contains the list of all the faults that a system can have.Fault Management basic functionality is to store the faults (current & previous ignition cycles) in EEPROM.It also supports clearing of the particular fault and also clearing of entire fault memory based on     the customer requirement.Event Data Recorder, TCS, India Responsible for development and testing of accident recorder modules.It is utilized to store the information identified with vehicle (e.g.Vehicle speed, Buckle switch status, Brake status, Airbag sensors) amid accident through CAN communication protocol Monitoring Various ECU's for Engine control, TCS, India Safety and preventive measures for engine ECU (Electronic Control Unit) are mainly considered.Different inputs from various modules like cruise control, Adaptive cruise control, Acceleration pedal etc.are considered and monitored.Concentrates on the security levels (Levels defines the cautions to be taken based on the priority of module failures) provided for different modules (driver safety is mainly considered).In critical cases pre-defined values are loaded for safety purpose.Drive by wire - electronic throttle valve system" on Altera DE2 FPGA board Programmed and configured Altera DE2 board to implement a "drive by wire - electronic throttle valve system.Interfaced Accelerator position sensor, Throttle position sensor, Throttle actuator motor (used a Servo Motor), relays, LEDs & LCD present on the board to the NIOS II software and to the NIOS II microprocessor present with in the Altera Cyclone II FPGA IC on the DE2 board Simulated the modules in Modelsim and synthesize on Altera Quartus II software.Accident avoidance system An Arduino based accident prevention using higher end alert mechanisms, which prevents the accidents by alerting the driver when he/she falls asleep.Project involves Arduino Uno - Atmega 328 Microcontroller to measure and counts the eye blink using IR sensor.It gets trigger from the sensor information to identify an accident.JNTU-H-Lab Assistant,,IndiaCurrent-CurrentMicroprocessor, Analog and Digital Communications.Hands on experience in Microprocessor, Analog and Digital Communications and E-Cad Laboratories.Monitor the lab setups and guide the students for the effective usage of labs.
SkillsDreamweaver, Assembly language, Automation, basic, C, C++, Cad, CSS, LCD, DOORS, Embedded Systems, focus, HTML, PHP, Java, Labview, logic, Mac OS, MATLAB, memory, Microprocessor, Microsoft Office, Office 3.0, SharePoint, Windows XP, Office Automation, Operating Systems, Programming, protocols, PSPICE, requirement, Safety, software development, switch, UNIX, Verilog, VHDL, Vista
```
</details>

<details>
<summary>Show Cleaned Resume</summary>

```text
Professional SummaryTo achieve a responsible position that gives me a chance to apply my innovative skills and knowledge. I aim to be a valuable member of the team that works dynamically towards success and growth of organization. Strong Knowledge in Electronics and computer Engineering background with 1+ experience as Automotive Embedded Software Engineer. Good Knowledge in simulation tools such as MATLAB and Simulink. Thorough Knowledge in CAN Communication and Basic knowledge in AUTOSAR Architecture. Familiar with Version control systems such as SVN, IBM Synergy, Clear case and requirements analysis tools such as Doors. Worked on all phases of V model software development and Version control systems. Communicated with the other Engineering personnel to coordinate the interrelated design and assure project completion. Coordinating with software and target teams to find bugs, testing debug build.
SkillsGuest servicesInventory control proceduresMerchandising expertiseLoss preventionCash register operationsProduct promotions
EducationNorthwestern Polytechnic .Expected inJan'16––M.S:Electrical and Computer Engineering-GPA:3.6Electrical and Computer Engineering 3.6Jawaharlal Nehru Institute of Technology,Expected inMay'14––Bachelors:Electronics and communication Engineering-GPA:3.4Electronics and communication Engineering 3.4
Work HistoryOneblood-Embedded SoftwareDeland,,India01/2016-07/2016Responsible for developing Safety and Engine related software.Special focus on areas such as CAN protocols.Embedded software component development for Engine ECU, and maintenance of existing software components.Supported all phases of the software development process (V - Model).Understand and negotiate specifications, designed and implemented code, created documents and descriptions maintained existing software.Stored, retrieved and manipulated data for close analysis of system capabilities.Prepared detailed reports concerning project specifications and activities.Worked effectively with design teams to ensure software solutions elevated client side experience.Defense Electronics Research Laboratory DLRL-Project TraineeCity,STATE,India11/2012-04/2013Undergone a training program in Industrial Automation, which gives a hands on experience in 8051 programming, AVR programming for Embedded Systems applications, Digital logic and Electronic Control, using commonly used transducers, sensors and output devices and components in automation and controlling.Projects Fault Management, TCS, India Responsible for development and testing of Fault management module.It contains the list of all the faults that a system can have.Fault Management basic functionality is to store the faults (current & previous ignition cycles) in EEPROM.It also supports clearing of the particular fault and also clearing of entire fault memory based on the customer requirement.Event Data Recorder, TCS, India Responsible for development and testing of accident recorder modules.It is utilized to store the information identified with vehicle (e.g.Vehicle speed, Buckle switch status, Brake status, Airbag sensors) amid accident through CAN communication protocol Monitoring Various ECU's for Engine control, TCS, India Safety and preventive measures for engine ECU (Electronic Control Unit) are mainly considered.Different inputs from various modules like cruise control, Adaptive cruise control, Acceleration pedal etc.are considered and monitored.Concentrates on the security levels (Levels defines the cautions to be taken based on the priority of module failures) provided for different modules (driver safety is mainly considered).In critical cases pre-defined values are loaded for safety purpose.Drive by wire - electronic throttle valve system" on Altera DE2 FPGA board Programmed and configured Altera DE2 board to implement a "drive by wire - electronic throttle valve system.Interfaced Accelerator position sensor, Throttle position sensor, Throttle actuator motor (used a Servo Motor), relays, LEDs & LCD present on the board to the NIOS II software and to the NIOS II microprocessor present with in the Altera Cyclone II FPGA IC on the DE2 board Simulated the modules in Modelsim and synthesize on Altera Quartus II software.Accident avoidance system An Arduino based accident prevention using higher end alert mechanisms, which prevents the accidents by alerting the driver when he/she falls asleep.Project involves Arduino Uno - Atmega 328 Microcontroller to measure and counts the eye blink using IR sensor.It gets trigger from the sensor information to identify an accident.JNTU-H-Lab Assistant,,IndiaCurrent-CurrentMicroprocessor, Analog and Digital Communications.Hands on experience in Microprocessor, Analog and Digital Communications and E-Cad Laboratories.Monitor the lab setups and guide the students for the effective usage of labs.
SkillsDreamweaver, Assembly language, Automation, basic, C, C++, Cad, CSS, LCD, DOORS, Embedded Systems, focus, HTML, PHP, Java, Labview, logic, Mac OS, MATLAB, memory, Microprocessor, Microsoft Office, Office 3.0, SharePoint, Windows XP, Office Automation, Operating Systems, Programming, protocols, PSPICE, requirement, Safety, software development, switch, UNIX, Verilog, VHDL, Vista
```
</details>

### 💼 Job Description Text Comparison

<details>
<summary>Show Original Job Description</summary>

```text
LHH Recruitment Solutions is looking for a Software Engineer V for a global people analytics and consulting firm focused on improving employee work experiences and driving better business results.
We're seeking a skilled Software Engineer with experience in data, reporting, and business processes. You'll support software development, testing, and troubleshooting for key applications. Collaboration with business and IT teams is crucial to ensure requirements are met and issues are resolved.
Position is Remote, Direct HireW2, and it is Full Time. 
Responsibilities:Support requirements definition, software development, and testing for key applications.Collaborate with business and IT teams to meet emerging needs and resolve application issues.Manage vendor relationships for 3rd party application development.Assist with application installation and testing.

Technical Skills:Experience with relational and unstructured data.Proficiency in front-end and back-end web development.Strong understanding of data architectures, flows, and ETL processes.Experience designing and managing distributed systems.Familiarity with DevOps practices is a plus.

Software Requirements:Foundational: Windows Server, .NET framework, Visual Studio, C#, Microsoft Azure, Git, Application InsightsIdentityAuthentication: SSO, SAML, WIF, OpenId Connect, Azure Active DirectoryData: SQL ServerSSIS, Mongo, Azure StorageFront-end: Angular, HTML, JavaScript, TypeScript, jQuery, KendoBack-end: Entity Framework, WebAPI, Azure Service Bus, Azure App ServicesWebsitesVirtual Machines

Qualifications:Bachelors degree in computing, information technology, or a related field, or significant software engineering experience.3+ years of Full-Stack; software engineering experience supporting information systems.Must have strong recent Front-End experience.Must have recent Angular experience.Must have experience leading or mentoring developers.Experience architecting.Strong technical and problem-solving skills.Ability to work effectively in a small team.Excellent written and oral communication skills.Agile development experience.

Benefits (Medical, Dental, 401(k), PTO)? Unlimited PTO (vacation and sick time) benefits paid 100% by company for employees and dependents. 45% 401 (k) match for every dollar.
What % of benefits do you cover? 100% paid for by employer for employee + dependents
Internal mobility  career growth options? Yes
```
</details>

<details>
<summary>Show Cleaned Job Description</summary>

```text
LHH Recruitment Solutions is looking for a Software Engineer V for a global people analytics and consulting firm focused on improving employee work experiences and driving better business results.
We're seeking a skilled Software Engineer with experience in data, reporting, and business processes. You'll support software development, testing, and troubleshooting for key applications. Collaboration with business and IT teams is crucial to ensure requirements are met and issues are resolved.
Position is Remote, Direct HireW2, and it is Full Time.
Responsibilities:Support requirements definition, software development, and testing for key applications.Collaborate with business and IT teams to meet emerging needs and resolve application issues.Manage vendor relationships for 3rd party application development.Assist with application installation and testing.

Technical Skills:Experience with relational and unstructured data.Proficiency in front-end and back-end web development.Strong understanding of data architectures, flows, and ETL processes.Experience designing and managing distributed systems.Familiarity with DevOps practices is a plus.

Software Requirements:Foundational: Windows Server, .NET framework, Visual Studio, C#, Microsoft Azure, Git, Application InsightsIdentityAuthentication: SSO, SAML, WIF, OpenId Connect, Azure Active DirectoryData: SQL ServerSSIS, Mongo, Azure StorageFront-end: Angular, HTML, JavaScript, TypeScript, jQuery, KendoBack-end: Entity Framework, WebAPI, Azure Service Bus, Azure App ServicesWebsitesVirtual Machines

Qualifications:Bachelors degree in computing, information technology, or a related field, or significant software engineering experience.3+ years of Full-Stack; software engineering experience supporting information systems.Must have strong recent Front-End experience.Must have recent Angular experience.Must have experience leading or mentoring developers.Experience architecting.Strong technical and problem-solving skills.Ability to work effectively in a small team.Excellent written and oral communication skills.Agile development experience.

Benefits (Medical, Dental, 401(k), PTO)? Unlimited PTO (vacation and sick time) benefits paid 100% by company for employees and dependents. 45% 401 (k) match for every dollar.
What % of benefits do you cover? 100% paid for by employer for employee + dependents
Internal mobility career growth options? Yes
```
</details>

---

## Sample 7 (Original Row Index: 1617)

- **Label:** `No Fit` ➔ `No Fit`
- **Before Lengths:** Resume = 5769 chars, JD = 2224 chars
- **After Lengths:** Resume = 5692 chars, JD = 2220 chars

### 📄 Resume Text Comparison

<details>
<summary>Show Original Resume</summary>

```text
Summary8+ years of accomplished experience in the field of accounting Team and organizational training from a major global public corporation Exceptionally fast, efficient and organized Knowledge of all accounting functions: GL, PL, and BS - budgets, forecasting, variance analysis, trend analysis, financial reporting, reconciliations, work papers, journal entries, accruals, AP, AR Experience in GAAP and Statutory accounting and monthly and year-end closing processes
HighlightsOracle Financial, PeopleSoft, Microsoft Dynamics Nav, Microsoft Office Suite, Outlook, Lotus Notes
Experience06/2015toPresentSenior AccountantGartner|Redwood City,CA,Prepare, examine, or analyze accounting records, financial statements, or other financial reports to assess accuracy, completeness, and conformance to reporting and procedural standards.Process, prepare and maintain reporting related to Inventory, and all associated recurring and/or ad hoc journal entries, account analysis, financial reporting, account reconciliation and system interface analysis, (COGS, Rebates, Adjustments, Other Revenues) in accordance with established general accounting policies and procedures Summarize vendor contracts and/or annual contract amendments to extract financial pertinent information to determine rebate configuration for monthly/quarterly invoicing Create, review revenue loaders, rebate, billing invoices and track the payment status Prepare communications such as memos, presentation charts, and process documentation, and coordinate with other departments with assembling information for reporting results Maintain Sox controls and departmental documentation Train new staff and review the work of less experienced staff Cross training with other team members in other accounting functions.09/2013to05/2014Accountant IIGraphic Packaging|West Monroe,LA,Completed assigned reconciliations accurately, completely and in the time frame required by corporate policies Prepared and ensured accuracy and integrity of accounting and transactional records to ensure proper financial reporting Worked with internal Financial Reporting personnel to support timely and accurate completion of monthly, quarterly and annual internal and external reporting Processed and maintained assigned ad hoc or recurring journal entries in a timely and accurate manner Ensured that interfaces between ancillary systems and the general ledger are processed timely and accurately so that the affected assigned general ledger accounts are complete, accurate and properly classified Independently reviewed revenue and expense accounts for accuracy; determined proper accruals Jessica Claire Resume 	     			Page 2 of 2 Independently provided prompt, courteous and professional customer service to internal and external users of information provided by the Accounting department Worked with external audit firm to support timely completion of audits or compliance reporting Assisted other departments with compiling information and reporting results and variances.12/2008to01/2013Accountant IIGraphic Packaging|Shelbyville,IL,Assisted in the month/year end close and preparation of associated journal entries Performed detailed analysis of the general ledger in conjunction with the month end close Responsible for the preparation of foreign branch balance sheets, income statements, and fixed assets schedules and reconciliations Verified and analyzed monthly and quarterly underwriting activity as reported by foreign branches, subsidiaries and affiliates, Pools and Syndicates Recognized and investigated unusual results utilizing all available resources and effectively communicated findings to management Analyzed and recorded foreign branch results on home office books, interacting with other areas, to ensure the accuracy of journal entries Reconciled ledger balances resulting from underwriting activity, account settlements, and profit and loss on foreign exchange and between sub-ledger and general ledger to insure accurate figures before monthly sub-ledger close Cash settlements through wire transfers, electronic receipts, check deposits, ach payments, and check requests.10/2006to06/2008AssociateAce Hardware|Clarks Summit,PA,Developed, coordinated and planned expense budgets, forecasts, headcount monitoring and tracking and consolidated and analyzed trends of the expenses for Compensation and Planning within Agency Division successfully ended the year within +/- 2% variance to forecast.Prepared, updated and monitored monthly Financial Analysis Summaries and budget templates for the monthly financial management presentations including actual and projected results.Coordinated with section managers to prepare budget uploads and monthly Budget versus Actual meetings.Prepared recurring and ad-hoc journal entries and provided ad hoc analysis reporting to management as needed, such as identifying spending trends, analyzing variances, or for other purposes as requested.
EducationExpected intotoMasters of Science|AccountingKEAN UNIVERSITY,,NJGPA:AccountingExpected intotoBachelor of Science|Management Science,,GPA:Management Science
Skillsaccount reconciliation, Accounting, general accounting, accruals, ad, Agency, balance sheets, billing, budgets, Budget, charts, compliance reporting, contracts, customer service, documentation, financial, Financial Analysis, financial management, financial reports, Financial Reporting, financial statements, fixed assets, foreign exchange, frame, general ledger, general ledger accounts, home office, Inventory, invoicing, ledger, Lotus Notes, meetings, Microsoft Dynamics, Microsoft Office Suite, Outlook, month end close, Oracle Financial, PeopleSoft, personnel, policies, presentations, profit and loss, reporting, settlements, underwriting
```
</details>

<details>
<summary>Show Cleaned Resume</summary>

```text
Summary8+ years of accomplished experience in the field of accounting Team and organizational training from a major global public corporation Exceptionally fast, efficient and organized Knowledge of all accounting functions: , and BS - budgets, forecasting, variance analysis, trend analysis, financial reporting, reconciliations, work papers, journal entries, accruals, Experience in GAAP and Statutory accounting and monthly and year-end closing processes
HighlightsOracle Financial, PeopleSoft, Microsoft Dynamics Nav, Microsoft Office Suite, Outlook, Lotus Notes
Experience06/2015toPresentSenior AccountantGartner| ,Prepare, examine, or analyze accounting records, financial statements, or other financial reports to assess accuracy, completeness, and conformance to reporting and procedural standards.Process, prepare and maintain reporting related to Inventory, and all associated recurring and/or ad hoc journal entries, account analysis, financial reporting, account reconciliation and system interface analysis, (COGS, Rebates, Adjustments, Other Revenues) in accordance with established general accounting policies and procedures Summarize vendor contracts and/or annual contract amendments to extract financial pertinent information to determine rebate configuration for monthly/quarterly invoicing Create, review revenue loaders, rebate, billing invoices and track the payment status Prepare communications such as memos, presentation charts, and process documentation, and coordinate with other departments with assembling information for reporting results Maintain Sox controls and departmental documentation Train new staff and review the work of less experienced staff Cross training with other team members in other accounting functions.09/2013to05/2014Accountant IIGraphic Packaging| ,Completed assigned reconciliations accurately, completely and in the time frame required by corporate policies Prepared and ensured accuracy and integrity of accounting and transactional records to ensure proper financial reporting Worked with internal Financial Reporting personnel to support timely and accurate completion of monthly, quarterly and annual internal and external reporting Processed and maintained assigned ad hoc or recurring journal entries in a timely and accurate manner Ensured that interfaces between ancillary systems and the general ledger are processed timely and accurately so that the affected assigned general ledger accounts are complete, accurate and properly classified Independently reviewed revenue and expense accounts for accuracy; determined proper accruals Jessica Claire Resume Page 2 of 2 Independently provided prompt, courteous and professional customer service to internal and external users of information provided by the Accounting department Worked with external audit firm to support timely completion of audits or compliance reporting Assisted other departments with compiling information and reporting results and variances.12/2008to01/2013Accountant IIGraphic Packaging| ,Assisted in the month/year end close and preparation of associated journal entries Performed detailed analysis of the general ledger in conjunction with the month end close Responsible for the preparation of foreign branch balance sheets, income statements, and fixed assets schedules and reconciliations Verified and analyzed monthly and quarterly underwriting activity as reported by foreign branches, subsidiaries and affiliates, Pools and Syndicates Recognized and investigated unusual results utilizing all available resources and effectively communicated findings to management Analyzed and recorded foreign branch results on home office books, interacting with other areas, to ensure the accuracy of journal entries Reconciled ledger balances resulting from underwriting activity, account settlements, and profit and loss on foreign exchange and between sub-ledger and general ledger to insure accurate figures before monthly sub-ledger close Cash settlements through wire transfers, electronic receipts, check deposits, ach payments, and check requests.10/2006to06/2008AssociateAce Hardware| ,Developed, coordinated and planned expense budgets, forecasts, headcount monitoring and tracking and consolidated and analyzed trends of the expenses for Compensation and Planning within Agency Division successfully ended the year within +/- 2% variance to forecast.Prepared, updated and monitored monthly Financial Analysis Summaries and budget templates for the monthly financial management presentations including actual and projected results.Coordinated with section managers to prepare budget uploads and monthly Budget versus Actual meetings.Prepared recurring and ad-hoc journal entries and provided ad hoc analysis reporting to management as needed, such as identifying spending trends, analyzing variances, or for other purposes as requested.
EducationExpected intotoMasters of Science|AccountingKEAN UNIVERSITY,,NJGPA:AccountingExpected intotoBachelor of Science|Management Science,,GPA:Management Science
Skillsaccount reconciliation, Accounting, general accounting, accruals, ad, Agency, balance sheets, billing, budgets, Budget, charts, compliance reporting, contracts, customer service, documentation, financial, Financial Analysis, financial management, financial reports, Financial Reporting, financial statements, fixed assets, foreign exchange, frame, general ledger, general ledger accounts, home office, Inventory, invoicing, ledger, Lotus Notes, meetings, Microsoft Dynamics, Microsoft Office Suite, Outlook, month end close, Oracle Financial, PeopleSoft, personnel, policies, presentations, profit and loss, reporting, settlements, underwriting
```
</details>

### 💼 Job Description Text Comparison

<details>
<summary>Show Original Job Description</summary>

```text
Role Details:We are seeking a Senior Software Engineer who will help drive our clients systems evolution to join our team. The role will be an integral part of the Video Streaming and Engineering team, working with video engineers to build and release products for various platforms like Desktop, OTT, Mobile. The candidate will be responsible for building, deploying and managing Video Packaging and Delivery applications in cloud (GCP AWS).
Your Day-to-Day: Work with other engineers to maintain and evolve our Video delivery and SVOD platform. Plan, Design and Build out cloud-based microservices to support video processing workflows. Field questions and requests regarding APIs and behavior. Work closely with the partnership team about media delivery to outside partners. Work with other developers and operations team on streamlined CICD solutions. Help in building the shared libraries and architecture to be used across all services.

Key Projects: Work with video engineers in team to modernize and optimize our cloud Video Partner Delivery platform. Building new microservices, features and improving Video Delivery  Content Filtering solutions for Paramount+. Responsible for maintaining cloud services in GCPAWS that power content sharing with partners like Apple, Amazon, Youtube etc. Work with development teams on re-architecturemodernizing existing systems into the cloud.

Qualifications:
You have  4+ years of experience as a Software Engineer Experience building features and maintaining PHP and Golang projects. Experience building microservices in Golang and building shared libraries. Experience with container technology and management such as Docker. Experience working with CloudSaaS services such as Amazon AWS or Google Cloud Strong written, verbal and interpersonal communication skills.

You might also have  Experience with AVC, HEVC, VP9, AV1, AAC video and audio codec standards. Experience with media containers , transcoding and packaging technologies. Experience with technologies like Kubernetes, EKS  GKE is a plus. Strong experience with video broadcasting and streaming media standards BS degree in Computer Science, similar technical field of study or equivalent practical experience
```
</details>

<details>
<summary>Show Cleaned Job Description</summary>

```text
Role Details:We are seeking a Senior Software Engineer who will help drive our clients systems evolution to join our team. The role will be an integral part of the Video Streaming and Engineering team, working with video engineers to build and release products for various platforms like Desktop, OTT, Mobile. The candidate will be responsible for building, deploying and managing Video Packaging and Delivery applications in cloud (GCP AWS).
Your Day-to-Day: Work with other engineers to maintain and evolve our Video delivery and SVOD platform. Plan, Design and Build out cloud-based microservices to support video processing workflows. Field questions and requests regarding APIs and behavior. Work closely with the partnership team about media delivery to outside partners. Work with other developers and operations team on streamlined CICD solutions. Help in building the shared libraries and architecture to be used across all services.

Key Projects: Work with video engineers in team to modernize and optimize our cloud Video Partner Delivery platform. Building new microservices, features and improving Video Delivery Content Filtering solutions for Paramount+. Responsible for maintaining cloud services in GCPAWS that power content sharing with partners like Apple, Amazon, Youtube etc. Work with development teams on re-architecturemodernizing existing systems into the cloud.

Qualifications:
You have 4+ years of experience as a Software Engineer Experience building features and maintaining PHP and Golang projects. Experience building microservices in Golang and building shared libraries. Experience with container technology and management such as Docker. Experience working with CloudSaaS services such as Amazon AWS or Google Cloud Strong written, verbal and interpersonal communication skills.

You might also have Experience with AVC, HEVC, VP9, AV1, AAC video and audio codec standards. Experience with media containers , transcoding and packaging technologies. Experience with technologies like Kubernetes, EKS GKE is a plus. Strong experience with video broadcasting and streaming media standards BS degree in Computer Science, similar technical field of study or equivalent practical experience
```
</details>

---

## Sample 8 (Original Row Index: 1517)

- **Label:** `No Fit` ➔ `No Fit`
- **Before Lengths:** Resume = 2949 chars, JD = 1185 chars
- **After Lengths:** Resume = 2883 chars, JD = 1184 chars

### 📄 Resume Text Comparison

<details>
<summary>Show Original Resume</summary>

```text
Summary•        
Over
Three years of extensive experience as a Front-End UI Developer with solid
understanding of database designing, development and installation of different
modules. 

•        
Professional
understanding of System development life cycle (SDLC) as well as various phases such as Analysis Design,
Development and Testing. 

•        
Expert
in developing User Interface (UI) applications and professional web
applications using JavaScript, JSP, XML,
HTML5 /DHTML, DOM, XHTML, jQuery, CSS3, and Ajax.• Extensive
experience in various UI widgets using JavaScript
libraries like Angular.js, Node.js and developing Rich Internet Applications RIA.• Experience
in implementing Web Services (RESTful/SOAP)
and REST services.•  Experience
in  SQL Server and T-SQL
servers.• Experience in Hadoop,
Hive, Postgres, Cassandra, Mongo.• Sound
knowledge in working with browsers compatibility issues with browsers like IE, Firefox, Safari, Opera, Chrome.Good
experience in automation testing
with Mocha and Jasmine using Selenium.•  Good
Experience in Jasmine framework to
write the unit tests in order to
prevent the functional defects from being deployed to production.•Good
knowledge in the configuration management and version control software like TFS, Bit bucket, GitHub.• Highly motivated self-starter, hard worker, team player and research orientated.•Flexible, team player, “get-it-done” personality.
SkillsProgramming Languages: C, Java, PythonOperating Systems: WindowsDatabase: MySQLWeb Technologies: HTML, CSS, JavaScript, JQuery, Java Servlets, BootstrapProject DetailsPlay TombolaDuration: 30 DaysTeam size: 1 Java, MySQL, CSS, JavaScript, JQuery, HTML, Bootstrap, Java Servlets
ExperienceSoftware Engineer Intern,10/2016-CurrentViasat Inc.–AR,State,Responsibilities:

·  Designed
Frontend with in VB Scripting.

·        
Developed
Single page application using the Router concept.

·        
Used  CISA,
PYTHON,CISM.

·        
 Used Powershell,  Perl for fast going application.

·        
Improved the performance of the application by replacing the
existing process and controls with most suitable process flow, optimized
queries and code snippets

·        
Introduced
methodologies and best practices that enhanced product definition, release processes and customization of applications
to user needs.
Education and TrainingMaster Of Science:Information Technology,Expected in--Hyderabad,GPA:Status-Information TechnologyB.Tech:Electrical and Electronics Engineering,Expected in2016--,GPA:Status-Electrical and Electronics Engineering Kakinada with 70.40% marksDiploma:Electrical and Electronics Engineering,Expected in2013--,GPA:Status-Electrical and Electronics Engineering from SBTET Andhra Pradesh with 69.49% marks
*S.S.C. (2010) from State Board of Andhra Pradesh with 74.00% marks
SkillsC, CSS, Database, HTML, Java, Java Servlets, JavaScript, JQuery, Windows, MySQL, Operating Systems, Developer, Programming, Python
```
</details>

<details>
<summary>Show Cleaned Resume</summary>

```text
Summary•
Over
Three years of extensive experience as a Front-End UI Developer with solid
understanding of database designing, development and installation of different
modules.

•
Professional
understanding of System development life cycle (SDLC) as well as various phases such as Analysis Design,
Development and Testing.

•
Expert
in developing User Interface (UI) applications and professional web
applications using JavaScript, JSP, XML,
HTML5 /DHTML, DOM, XHTML, jQuery, CSS3, and Ajax.• Extensive
experience in various UI widgets using JavaScript
libraries like Angular.js, Node.js and developing Rich Internet Applications RIA.• Experience
in implementing Web Services (RESTful/SOAP)
and REST services.•  Experience
in  SQL Server and T-SQL
servers.• Experience in Hadoop,
Hive, Postgres, Cassandra, Mongo.• Sound
knowledge in working with browsers compatibility issues with browsers like IE, Firefox, Safari, Opera, Chrome.Good
experience in automation testing
with Mocha and Jasmine using Selenium.•  Good
Experience in Jasmine framework to
write the unit tests in order to
prevent the functional defects from being deployed to production.•Good
knowledge in the configuration management and version control software like TFS, Bit bucket, GitHub.• Highly motivated self-starter, hard worker, team player and research orientated.•Flexible, team player, “get-it-done” personality.
SkillsProgramming Languages: C, Java, PythonOperating Systems: WindowsDatabase: MySQLWeb Technologies: HTML, CSS, JavaScript, JQuery, Java Servlets, BootstrapProject DetailsPlay TombolaDuration: 30 DaysTeam size: 1 Java, MySQL, CSS, JavaScript, JQuery, HTML, Bootstrap, Java Servlets
ExperienceSoftware Engineer Intern,10/2016-CurrentViasat Inc.–AR,State,Responsibilities:

·  Designed
Frontend with in VB Scripting.

·
Developed
Single page application using the Router concept.

·
Used  CISA,
PYTHON,CISM.

·
 Used Powershell,  Perl for fast going application.

·
Improved the performance of the application by replacing the
existing process and controls with most suitable process flow, optimized
queries and code snippets

·
Introduced
methodologies and best practices that enhanced product definition, release processes and customization of applications
to user needs.
Education and TrainingMaster Of Science:Information Technology,Expected in--Hyderabad,GPA:Status-Information TechnologyB.Tech:Electrical and Electronics Engineering,Expected in2016--,GPA:Status-Electrical and Electronics Engineering Kakinada with 70.40% marksDiploma:Electrical and Electronics Engineering,Expected in2013--,GPA:Status-Electrical and Electronics Engineering from SBTET Andhra Pradesh with 69.49% marks
*S.S.C. (2010) from State Board of Andhra Pradesh with 74.00% marks
SkillsC, CSS, Database, HTML, Java, Java Servlets, JavaScript, JQuery, Windows, MySQL, Operating Systems, Developer, Programming, Python
```
</details>

### 💼 Job Description Text Comparison

<details>
<summary>Show Original Job Description</summary>

```text
LHH Recruitment Solutions is partnering with a company that will be relocating to St. Louis Park and looking for an experienced Accountant to support their centrally located clients in Food production. Here you will establish relationships within the home office as well as support manufacturing locations in month end procedure, journal entries as well as participate with the budgeting and forecasting processes.
Key Responsibilities: Perform a variety of accounting responsibilities as well as forecasting and budgeting in fixed assetsSupport centralized functions for 5 manufacturing locationsMonth end close, journal entries, account reconciliations, month end reportingProvide parent company communication including monthly reporting

Qualifications: 2+ years experience with month end close, journal entriesSame industry experience a plusBachelors Accounting or Finance
Skills:MS Excel, ERP system experienceStrong communication skills and ability to communicate with other teams 
CompensationBenefits: $65,000-$85,000Benefits apply to hiring company
Worksite TypeScheduleTime zone: Hybrid 3 days in office, 2 days homeEqual opportunity employer minoritieswomenveteransdisabled.
```
</details>

<details>
<summary>Show Cleaned Job Description</summary>

```text
LHH Recruitment Solutions is partnering with a company that will be relocating to St. Louis Park and looking for an experienced Accountant to support their centrally located clients in Food production. Here you will establish relationships within the home office as well as support manufacturing locations in month end procedure, journal entries as well as participate with the budgeting and forecasting processes.
Key Responsibilities: Perform a variety of accounting responsibilities as well as forecasting and budgeting in fixed assetsSupport centralized functions for 5 manufacturing locationsMonth end close, journal entries, account reconciliations, month end reportingProvide parent company communication including monthly reporting

Qualifications: 2+ years experience with month end close, journal entriesSame industry experience a plusBachelors Accounting or Finance
Skills:MS Excel, ERP system experienceStrong communication skills and ability to communicate with other teams
CompensationBenefits: $65,000-$85,000Benefits apply to hiring company
Worksite TypeScheduleTime zone: Hybrid 3 days in office, 2 days homeEqual opportunity employer minoritieswomenveteransdisabled.
```
</details>

---

## Sample 9 (Original Row Index: 5830)

- **Label:** `Good Fit` ➔ `Fit`
- **Before Lengths:** Resume = 3748 chars, JD = 916 chars
- **After Lengths:** Resume = 3719 chars, JD = 916 chars

### 📄 Resume Text Comparison

<details>
<summary>Show Original Resume</summary>

```text
Professional SummarySOFTWARE ENGINEER with over 5 years of professional software development experience in highly
scalable backend systems, web development, and product management. Adept in critical thinking, advanced
software proficiency, programming languages, and system design for enabling solutions with enhanced
efficiency, faster time to market, as well as low operation costs.
 ACCOMPLISHMENTSCo-Authored 4 patents filed at USPTO.Invited to VMware Radio 2016 for a paper presentation on Geo Distributed Monitoring Systems.Certificate of Recognition awards at VMware.Successfully led 4 major projects at Amazon unblocking 100+ internal customers and many retail
 initiates.
SkillsShell ScriptingJava, C++Testing, Troubleshooting and debuggingDocker, VMWare ESXI, vCenter, vCloudTeamwork, CollaborationDirector, Zabbix, LinuxAgile, ScrumHTML & JavaScriptTestNG, JenkinsSQLPerformance and scalability optimizationObject-Oriented ProgrammingTechnical writingPython, R & Shell scriptingRESTful Web ServicesAgileAPIC++DebuggingDeliveryHTMLJavaJavaScriptLinuxDirectorObject-Oriented ProgrammingOptimizationPressProcessesPythonReal-timeRetailScrumSDLCShell ScriptingSoftware DevelopmentSQLTeamworkTechnical writingTroubleshooting
Work HistorySOFTWARE DEVELOPMENT ENGINEER,04/2018toCurrentRing–North Reading,MA,Working in platform team running the core of Amazon's retail business.Led development of multi-tenant, highly scalable software solutions.Engineered software release for efficient and highly scalable web solutions.Completed four major projects, from Press Release to Final Delivery covering all SDLC processes.Building solution with 30% adoption rate, handling 1.4 Million Transactions Per Second leading to 7-
 9% improvement in backend requests for Amazon products including Amazon Music and Alexa.Carried out performance optimizations leading to IMR savings of approximately 7% or $10 Million.Ran campaigns for migrating close to ~400 internal customers to improve platform availability and
 security.SOFTWARE DEVELOPMENT ENGINEER INTERN,05/2017to07/2017Leidos Holdings Inc.–Camp Lejeune,NC,Responsible for requirements, analysis, design, and implementation of a stateless POST request service
 running the core of Amazon's retail business.Unblocked close to 40+ key customers including Amazon's cart and checkout leading to the increased
 adoption rate of platform.MEMBER OF TECHNICAL STAFF,07/2013to08/2016Advance Energy–Vancouver,,INDIADesigned and implemented Geo-distributed monitoring solution for real-time monitoring of various
 vCloud Air systems using open source technologies.Collaborated with an agile development team to build Java annotation-based framework for writing and
 orchestrating simple and efficient test libraries for RESTful API services.Built orchestration tools for system engineers across 6 teams performing load tests, stress tests, and
 writing user workflows for testing vCloud Air systems.
EducationMaster of Science:Computer Science, Twin Cities,Expected in2017toUniversity of Minnesota-,GPA:GPA: 3.82Bachelor of Engineering:Computer Science, Bangalore,Expected in2013toBMSCE-,GPA:GPA: 8.9
SkillsShell ScriptingJJava, C++TTesting, Troubleshooting and debuggingDDocker, VMWare ESXI, vCenter, vCloudTTeamwork, CollaborationDDirector, Zabbix, LinuxAAgile, ScrumHHTML & JavaScriptTTestNG, JenkinsSSQLPPerformance and scalability optimizationOObject-Oriented ProgrammingTTechnical writingPPython, R & Shell scriptingRRESTful Web Services,Agile, API, C++, debugging, Delivery, HTML, Java, JavaScript, Linux, Director, Object-Oriented Programming, optimization, Press, processes, Python, real-time, retail, Scrum, SDLC, Shell Scripting, Software Development, SQL, Teamwork, Technical writing, Troubleshooting
```
</details>

<details>
<summary>Show Cleaned Resume</summary>

```text
Professional SummarySOFTWARE ENGINEER with over 5 years of professional software development experience in highly
scalable backend systems, web development, and product management. Adept in critical thinking, advanced
software proficiency, programming languages, and system design for enabling solutions with enhanced
efficiency, faster time to market, as well as low operation costs.
 ACCOMPLISHMENTSCo-Authored 4 patents filed at USPTO.Invited to VMware Radio 2016 for a paper presentation on Geo Distributed Monitoring Systems.Certificate of Recognition awards at VMware.Successfully led 4 major projects at Amazon unblocking 100+ internal customers and many retail
 initiates.
SkillsShell ScriptingJava, C++Testing, Troubleshooting and debuggingDocker, VMWare ESXI, vCenter, vCloudTeamwork, CollaborationDirector, Zabbix, LinuxAgile, ScrumHTML & JavaScriptTestNG, JenkinsSQLPerformance and scalability optimizationObject-Oriented ProgrammingTechnical writingPython, R & Shell scriptingRESTful Web ServicesAgileAPIC++DebuggingDeliveryHTMLJavaJavaScriptLinuxDirectorObject-Oriented ProgrammingOptimizationPressProcessesPythonReal-timeRetailScrumSDLCShell ScriptingSoftware DevelopmentSQLTeamworkTechnical writingTroubleshooting
Work HistorySOFTWARE DEVELOPMENT ENGINEER,04/2018toCurrentRing– ,Working in platform team running the core of Amazon's retail business.Led development of multi-tenant, highly scalable software solutions.Engineered software release for efficient and highly scalable web solutions.Completed four major projects, from Press Release to Final Delivery covering all SDLC processes.Building solution with 30% adoption rate, handling 1.4 Million Transactions Per Second leading to 7-
 9% improvement in backend requests for Amazon products including Amazon Music and Alexa.Carried out performance optimizations leading to IMR savings of approximately 7% or $10 Million.Ran campaigns for migrating close to ~400 internal customers to improve platform availability and
 security.SOFTWARE DEVELOPMENT ENGINEER INTERN,05/2017to07/2017Leidos Holdings Inc.– ,Responsible for requirements, analysis, design, and implementation of a stateless POST request service
 running the core of Amazon's retail business.Unblocked close to 40+ key customers including Amazon's cart and checkout leading to the increased
 adoption rate of platform.MEMBER OF TECHNICAL STAFF,07/2013to08/2016Advance Energy–Vancouver,,INDIADesigned and implemented Geo-distributed monitoring solution for real-time monitoring of various
 vCloud Air systems using open source technologies.Collaborated with an agile development team to build Java annotation-based framework for writing and
 orchestrating simple and efficient test libraries for RESTful API services.Built orchestration tools for system engineers across 6 teams performing load tests, stress tests, and
 writing user workflows for testing vCloud Air systems.
EducationMaster of Science:Computer Science, Twin Cities,Expected in2017toUniversity of Minnesota-,GPA:GPA: 3.82Bachelor of Engineering:Computer Science, Bangalore,Expected in2013toBMSCE-,GPA:GPA: 8.9
SkillsShell ScriptingJJava, C++TTesting, Troubleshooting and debuggingDDocker, VMWare ESXI, vCenter, vCloudTTeamwork, CollaborationDDirector, Zabbix, LinuxAAgile, ScrumHHTML & JavaScriptTTestNG, JenkinsSSQLPPerformance and scalability optimizationOObject-Oriented ProgrammingTTechnical writingPPython, R & Shell scriptingRRESTful Web Services,Agile, API, C++, debugging, Delivery, HTML, Java, JavaScript, Linux, Director, Object-Oriented Programming, optimization, Press, processes, Python, real-time, retail, Scrum, SDLC, Shell Scripting, Software Development, SQL, Teamwork, Technical writing, Troubleshooting
```
</details>

### 💼 Job Description Text Comparison

<details>
<summary>Show Original Job Description</summary>

```text
Senior Software EngineerSelby Jennings is partnered with a Proprietary Trading firm based in the San Francisco Bay area that uses market-neutral strategies to negate the volatility of digital assets. In their first two years, they were able to double revenue and head count. Now, they are looking for a highly-skilled software engineer to join their core trading systems team.
Responsibilities: Design high-performance trading system components in a distributed architecture Analyze and improve the efficiency, scalability, and stability of our systems Interact with stakeholders (traders, portfolio managers, risk)
Qualifications:5+ years of professional Java experienceExperience working in a buy-side firm requiredExperience using low-latency techniquesMulti-threadedconcurrency programming with lock-free algorithmsExperience with distributed systems design and developmentMS in Computer Science or related field
```
</details>

<details>
<summary>Show Cleaned Job Description</summary>

```text
Senior Software EngineerSelby Jennings is partnered with a Proprietary Trading firm based in the San Francisco Bay area that uses market-neutral strategies to negate the volatility of digital assets. In their first two years, they were able to double revenue and head count. Now, they are looking for a highly-skilled software engineer to join their core trading systems team.
Responsibilities: Design high-performance trading system components in a distributed architecture Analyze and improve the efficiency, scalability, and stability of our systems Interact with stakeholders (traders, portfolio managers, risk)
Qualifications:5+ years of professional Java experienceExperience working in a buy-side firm requiredExperience using low-latency techniquesMulti-threadedconcurrency programming with lock-free algorithmsExperience with distributed systems design and developmentMS in Computer Science or related field
```
</details>

---

## Sample 10 (Original Row Index: 3930)

- **Label:** `Potential Fit` ➔ `Partial Fit`
- **Before Lengths:** Resume = 1923 chars, JD = 6174 chars
- **After Lengths:** Resume = 1891 chars, JD = 6089 chars

### 📄 Resume Text Comparison

<details>
<summary>Show Original Resume</summary>

```text
Career OverviewHighly motivated Sales Associate with extensive customer service and sales experience. Outgoing sales professional with track record of driving increased sales, improving buying experience and elevating company profile with target market.
QualificationsDevelopment: Using Apache Tomcat Server, Web Services, MVC pattern and OOP.
*Programming Languages: C#, Java, JavaScript, CSS3 and HTML5
Work ExperienceSoftware Development Intern,11/2016-PresentKion Group–Indianapolis,IN,Design, develop and test Android and iOS applications.Involving with all phases of mobile app development from initial concept, through design, development, testing and deployment.Work with product managers to clarify function flows and provide technical insight on optimization.Work with the entire project team to balance creative objectives with business and technical requirements.Data Center Operations Associate,01/2016-PresentBoulder County, Co–Boulder,CO,Develop internal application to process tracking data.Responsible for on-site support of, Data Operations Processes and providing Security Access Controls to Life Sys users through various system applications.Troubleshoot production issues reported by end users and demonstrate ability toward the resolution on restoring functionality and monitor network server.IT Intern,01/2013-10/2013Department Of State–City,STATE,Install, configure, and upgrade the network hardware and software.Identify and solve problems with hardware and software.Troubleshoot network connectivity issues, working with remote employees.
Education and Training:Computer Sciences/Mathematics,Expected inMay-2017-University of Lincoln Nebraska-Lincoln,NEGPA:Status-Computer Sciences/Mathematics 3.36
SkillsApache, balance, clarify, hardware, concept, CSS3, HTML5, Java, JavaScript, Access, C#, MVC, network hardware, network, OOP, optimization, Processes, Programming, Tomcat, Troubleshoot, upgrade
```
</details>

<details>
<summary>Show Cleaned Resume</summary>

```text
Career OverviewHighly motivated Sales Associate with extensive customer service and sales experience. Outgoing sales professional with track record of driving increased sales, improving buying experience and elevating company profile with target market.
QualificationsDevelopment: Using Apache Tomcat Server, Web Services, MVC pattern and OOP.
*Programming Languages: C#, Java, JavaScript, CSS3 and HTML5
Work ExperienceSoftware Development Intern,11/2016-PresentKion Group– ,Design, develop and test Android and iOS applications.Involving with all phases of mobile app development from initial concept, through design, development, testing and deployment.Work with product managers to clarify function flows and provide technical insight on optimization.Work with the entire project team to balance creative objectives with business and technical requirements.Data Center Operations Associate,01/2016-PresentBoulder County, Co– ,Develop internal application to process tracking data.Responsible for on-site support of, Data Operations Processes and providing Security Access Controls to Life Sys users through various system applications.Troubleshoot production issues reported by end users and demonstrate ability toward the resolution on restoring functionality and monitor network server.IT Intern,01/2013-10/2013Department Of State– ,Install, configure, and upgrade the network hardware and software.Identify and solve problems with hardware and software.Troubleshoot network connectivity issues, working with remote employees.
Education and Training:Computer Sciences/Mathematics,Expected inMay-2017-University of Lincoln Nebraska-Lincoln,NEGPA:Status-Computer Sciences/Mathematics 3.36
SkillsApache, balance, clarify, hardware, concept, CSS3, HTML5, Java, JavaScript, Access, C#, MVC, network hardware, network, OOP, optimization, Processes, Programming, Tomcat, Troubleshoot, upgrade
```
</details>

### 💼 Job Description Text Comparison

<details>
<summary>Show Original Job Description</summary>

```text
Life at Capgemini
Capgemini supports all aspects of your well-being throughout the changing stages of your life and career. For eligible employees, we offer:
Flexible work Healthcare including dental, vision, mental health, and well-being programs Financial well-being programs such as 401(k) and Employee Share Ownership Plan Paid time off and paid holidays Paid parental leave Family building benefits like adoption assistance, surrogacy, and cryopreservation Social well-being benefits like subsidized back-up childelder care and tutoring Mentoring, coaching and learning programs Employee Resource Groups Disaster Relief 
About Capgemini Engineering
World leader in engineering and R&D services, Capgemini Engineering combines its broad industry knowledge and cutting-edge technologies in digital and software to support the convergence of the physical and digital worlds. Coupled with the capabilities of the rest of the Group, it helps clients to accelerate their journey towards Intelligent Industry. Capgemini Engineering has more than 55,000 engineer and scientist team members in over 30 countries across sectors including Aeronautics, Space, Defence, Naval, Automotive, Rail, Infrastructure & Transportation, Energy, Utilities & Chemicals, Life Sciences, Communications, Semiconductor & Electronics, Industrial & Consumer, Software & Internet.
Capgemini Engineering is an integral part of the Capgemini Group, a global leader in partnering with companies to transform and manage their business by harnessing the power of technology. The Group is guided every day by its purpose of unleashing human energy through technology for an inclusive and sustainable future. It is a responsible and diverse organization of over 360,000 team members in more than 50 countries. With its strong 55-year heritage and deep industry expertise, Capgemini is trusted by its clients to address the entire breadth of their business needs, from strategy and design to operations, fuelled by the fast evolving and innovative world of cloud, data, AI, connectivity, software, digital engineering and platforms. The Group reported in 2022 global revenues of 22 billion.
Get the Future You Want  www.capgemini.com
Capgemini discloses salary range information in compliance with state and local pay transparency obligations. The disclosed range represents the lowest to highest salary we, in good faith, believe we would pay for this role at the time of this posting, although we may ultimately pay more or less than the disclosed range and the range may be modified in the future. The disclosed range takes into account the wide range of factors that are considered in making compensation decisions including, but not limited to, geographic location, relevant education, qualifications, certifications, experience, skills, seniority, performance, sales or revenue-based metrics, and business or organizational needs. At Capgemini, it is not typical for an individual to be hired at or near the top of the range for their role. The base salary range for the tagged location is [$ 65,200 - $138,944 yr].
This role may be eligible for other compensation including variable compensation, bonus, or commission. Full-time regular employees are eligible for paid time off, medicaldentalvision insurance, 401(k), and any other benefits to eligible employees.
Note: No amount of pay is considered to be wages or compensation until such amount is earned, vested, and determinable. The amount and availability of any bonus, commission, or any other form of compensation that is allocable to a particular employee remains in the Company's sole discretion unless and until paid and may be modified at the Companys sole discretion, consistent with the law
Job description:
We are looking for a strong Software Engineer to help one of our Enterprise Clients design, architect and write the documentation for an entire system. This person will code entire software solutions and identify and fix issues within their area of expertise.
Key responsibilities:
Proactively create and review team contributionsParticipate as a "code owner" and partner with collaborators in code-reviews.Automate unit, integration, and end to end testing solutions and incorporate them with the testing lifecycle. Be able to run your code in pre-production and ensure quality.Deploy your solutions across environments and platforms, including production releases. Provide operational support of your code and all code within your domain.Teardown old solutions, products, and resources when no longer needed.Resolve issues within the team and prevent problems from occurring. Be proactive and identify, resolve, mitigate and prevent technical issues, risks, and provide solutions.
Must Haves:
Experience with Microsoft strongly preferred4-6 years of software engineering experienceComputer Science degree or equivalent experience 3+ years of experience with C#, .NET core, .NET3+ years of build experience5+ years of experience in CICD tools (Source Control, Build, Deploy)3+ years (GitHub, Jenkins, Spinnaker)3+ years of experience in DevOps deployments
EEOC
Capgemini is an Equal Opportunity Employer encouraging diversity in the workplace. All qualified applicants will receive consideration for employment without regard to race, national origin, gender identityexpression, age religion, disability, sexual orientation, genetics, veteran status, marital status, or any other characteristic protected by law.
This is a general description of the Duties, Responsibilities and Qualifications required for this position. Physical, mental, sensory, or environmental demands may be referenced in an attempt to communicate the manner in which this position traditionally is performed. Whenever necessary to provide individuals with disabilities an equal employment opportunity, Capgemini will consider reasonable accommodations that might involve varying job requirements andor changing the way this job is performed, provided that such accommodations do not pose an undue hardship.
Click the following link for more information on your rights as an Applicant http:www.capgemini.comresourcesequal-employment-opportunity-is-the-law
```
</details>

<details>
<summary>Show Cleaned Job Description</summary>

```text
Life at Capgemini
Capgemini supports all aspects of your well-being throughout the changing stages of your life and career. For eligible employees, we offer:
Flexible work Healthcare including dental, vision, mental health, and well-being programs Financial well-being programs such as 401(k) and Employee Share Ownership Plan Paid time off and paid holidays Paid parental leave Family building benefits like adoption assistance, surrogacy, and cryopreservation Social well-being benefits like subsidized back-up childelder care and tutoring Mentoring, coaching and learning programs Employee Resource Groups Disaster Relief
About Capgemini Engineering
World leader in engineering and R&D services, Capgemini Engineering combines its broad industry knowledge and cutting-edge technologies in digital and software to support the convergence of the physical and digital worlds. Coupled with the capabilities of the rest of the Group, it helps clients to accelerate their journey towards Intelligent Industry. Capgemini Engineering has more than 55,000 engineer and scientist team members in over 30 countries across sectors including Aeronautics, Space, Defence, Naval, Automotive, Rail, Infrastructure & Transportation, Energy, Utilities & Chemicals, Life Sciences, Communications, Semiconductor & Electronics, Industrial & Consumer, Software & Internet.
Capgemini Engineering is an integral part of the Capgemini Group, a global leader in partnering with companies to transform and manage their business by harnessing the power of technology. The Group is guided every day by its purpose of unleashing human energy through technology for an inclusive and sustainable future. It is a responsible and diverse organization of over 360,000 team members in more than 50 countries. With its strong 55-year heritage and deep industry expertise, Capgemini is trusted by its clients to address the entire breadth of their business needs, from strategy and design to operations, fuelled by the fast evolving and innovative world of cloud, data, AI, connectivity, software, digital engineering and platforms. The Group reported in 2022 global revenues of 22 billion.
Get the Future You Want
Capgemini discloses salary range information in compliance with state and local pay transparency obligations. The disclosed range represents the lowest to highest salary we, in good faith, believe we would pay for this role at the time of this posting, although we may ultimately pay more or less than the disclosed range and the range may be modified in the future. The disclosed range takes into account the wide range of factors that are considered in making compensation decisions including, but not limited to, geographic location, relevant education, qualifications, certifications, experience, skills, seniority, performance, sales or revenue-based metrics, and business or organizational needs. At Capgemini, it is not typical for an individual to be hired at or near the top of the range for their role. The base salary range for the tagged location is [$ 65,200 - $138,944 yr].
This role may be eligible for other compensation including variable compensation, bonus, or commission. Full-time regular employees are eligible for paid time off, medicaldentalvision insurance, 401(k), and any other benefits to eligible employees.
Note: No amount of pay is considered to be wages or compensation until such amount is earned, vested, and determinable. The amount and availability of any bonus, commission, or any other form of compensation that is allocable to a particular employee remains in the Company's sole discretion unless and until paid and may be modified at the Companys sole discretion, consistent with the law
Job description:
We are looking for a strong Software Engineer to help one of our Enterprise Clients design, architect and write the documentation for an entire system. This person will code entire software solutions and identify and fix issues within their area of expertise.
Key responsibilities:
Proactively create and review team contributionsParticipate as a "code owner" and partner with collaborators in code-reviews.Automate unit, integration, and end to end testing solutions and incorporate them with the testing lifecycle. Be able to run your code in pre-production and ensure quality.Deploy your solutions across environments and platforms, including production releases. Provide operational support of your code and all code within your domain.Teardown old solutions, products, and resources when no longer needed.Resolve issues within the team and prevent problems from occurring. Be proactive and identify, resolve, mitigate and prevent technical issues, risks, and provide solutions.
Must Haves:
Experience with Microsoft strongly preferred4-6 years of software engineering experienceComputer Science degree or equivalent experience 3+ years of experience with C#, .NET core, .NET3+ years of build experience5+ years of experience in CICD tools (Source Control, Build, Deploy)3+ years (GitHub, Jenkins, Spinnaker)3+ years of experience in DevOps deployments
EEOC
Capgemini is an Equal Opportunity Employer encouraging diversity in the workplace. All qualified applicants will receive consideration for employment without regard to race, national origin, gender identityexpression, age religion, disability, sexual orientation, genetics, veteran status, marital status, or any other characteristic protected by law.
This is a general description of the Duties, Responsibilities and Qualifications required for this position. Physical, mental, sensory, or environmental demands may be referenced in an attempt to communicate the manner in which this position traditionally is performed. Whenever necessary to provide individuals with disabilities an equal employment opportunity, Capgemini will consider reasonable accommodations that might involve varying job requirements andor changing the way this job is performed, provided that such accommodations do not pose an undue hardship.
Click the following link for more information on your rights as an Applicant http:
```
</details>

---

