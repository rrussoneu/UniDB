# University Database Project

## Getting Started

- [R], [RStudio], and [SQLite] should be installed
  
- Install necessary [R packages](#dependencies)

## Overview

This project aims to simulate a university database system with an emphasis on demonstrating a variety of SQL operations, triggers, and queries ranging from simple to more complex. The first step for the project was to design and create an ER diagram for the database that is in BCNF and ensures a robust and efficient structure. This diagram is included as a PDF file in `University_ERD.pdf`. An R notebook is used to showcase the code execution sequence, using both R and SQL.

### Data Generation
The data for this project was randomly generated using Python found in `generate_data.py`. It simulates a variety of typical university entities such as students, faculty, departments, courses, and classroom data. While synthetic, the dataset provides a realistic representation of a typical university's operational data despite its general randomness. Care was taken to ensure consistency and realism across the data.

### Database Creation
The first step in realizing the database was to initialize tables for the simulated data in an SQLite database. Relationships between tables were carefully defined, maintain data integrity, and reflect real world connections between the entities.

### Queries
Various SQL queries are demonstrated and range from very simple to more complex. The queries were coded with an attention towards typical use cases in a university setting. These include:

- Getting the courses taught by particular faculty members
- Calculating the average GPA of students in each department
- Calculating the university's average GPA and student grades
- Getting the students who earned various Latin Honors
- Getting the top students in each major

### Triggers
SQL triggers were also introduced to automate specific common tasks such as updating students' GPA's as their grades are entered. 

### Result
Ultimately, a local SQLite database file is created and populated with the created tables and generated data. This database serves as a tangible outcome and can be used and expanded for further demonstration and exploration. While the data is fictional, a university setting provides a real world context to explore and demonstrate SQL and its capabilities.

### Areas For Expansion
Areas for expansion include refactoring the python script to generate a variety of times for courses to be held, as well as adding tables for required and elective courses.

### License
This project is licensed under the MIT license.

### Dependencies:
<a name="dependencies"></a>

- **RSQLite**
- **DBI**
- **sqldf**
- **reticulate**

[R]: https://www.r-project.org/about.html
[RStudio]: https://posit.co/download/rstudio-desktop/
[SQLite]: https://www.sqlite.org/index.html
