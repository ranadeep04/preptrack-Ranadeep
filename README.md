# PrepTrack — Placement Preparation Performance Analyzer

## Project Overview

PrepTrack is a Python console application that analyses a student’s placement-preparation performance. The application collects student details, attendance percentage, project completion status, profile verification status, and seven daily coding-practice scores.

The program validates user input, classifies performance for each practice day, calculates totals and averages, identifies the highest and lowest scores, detects the first critical score, evaluates placement readiness, and displays the first major blocker along with the next recommended action.

---

## Features Implemented

* Student profile input
* Student-name validation
* Attendance validation (0–100)
* Yes/No validation for project completion
* Yes/No validation for profile verification
* Seven-day practice score processing using a loop
* Practice-score validation
* Absent-day handling using `continue`
* Score classification:

  * Strong
  * Satisfactory
  * Needs Improvement
  * Critical
* Passed and failed day counting
* Strong, satisfactory, improvement, and critical day counting
* Highest-score detection
* Lowest-score detection
* First critical-score detection
* Total-score calculation
* Average-score calculation
* Division-by-zero prevention
* Placement-readiness evaluation
* Final status generation
* Primary blocker identification
* Next-action recommendation
* Final report display

---

## Python Concepts Used

* `print()`
* Variables
* Strings
* Integers
* Floating-point values
* Boolean values
* `input()`
* `int()`
* `float()`
* Arithmetic operators
* Relational operators
* Logical operators
* f-strings
* `if`
* `elif`
* `else`
* Compound conditions
* `while` loops
* `for` loops
* `range()`
* `continue`
* Counters
* Accumulators

---

## How to Run the Program

Open the terminal inside the project folder and run:

```bash
python main.py
```

If your system uses Python 3:

```bash
python3 main.py
```

---

## Sample Output

```text
==================================================
              PREPTRACK REPORT
==================================================
Student Name           : Ranadeep
Registration Number    : 23CS001
Graduation Year        : 2026
Attendance             : 85.0%

Attempted Days         : 7
Absent Days            : 0
Passed Days            : 7
Failed Days            : 0

Strong Days            : 5
Satisfactory Days      : 2
Needs Improvement Days : 0
Critical Days          : 0

Total Score            : 548
Average Score          : 78.29

Highest Score          : 90
Lowest Score           : 70

Final Status           : Ready for Mock Interview
Primary Blocker        : All criteria satisfied
Next Action            : Proceed to Mock Interview
==================================================
```

---

## Test Result Summary

| Test ID | Scenario                     | Expected Result                 | Status |
| ------- | ---------------------------- | ------------------------------- | ------ |
| TC-01   | All requirements satisfied   | Ready for Mock Interview        | Pass   |
| TC-02   | Critical score present       | Critical Support Required       | Pass   |
| TC-03   | Fewer than six attempts      | Practice Incomplete             | Pass   |
| TC-04   | Fewer than four passes       | Insufficient Passed Practices   | Pass   |
| TC-05   | Average below 70             | Practice Improvement Required   | Pass   |
| TC-06   | Attendance below 75          | Attendance Improvement Required | Pass   |
| TC-07   | Graduation year not eligible | Graduation Criteria Not Met     | Pass   |
| TC-08   | Project incomplete           | Application On Hold             | Pass   |
| TC-09   | Profile not verified         | Application On Hold             | Pass   |
| TC-10   | All days absent              | Practice Not Evaluated          | Pass   |

---

## Individual Contribution

* **Name:** Ranadeep Reddy
* **Repository URL:** https://github.com/ranadeep04/preptrack-Ranadeep
* **My main contribution:** Complete implementation of the PrepTrack application.Checked team members repositories and explained their mistakes and t
* **Features I implemented:** Input validation, score processing, score classification, counters, highest/lowest score logic, critical-score logic, average calculation, eligibility checks, final status logic, and final report display.
* **Python concepts I used:** Loops, conditions, Boolean expressions, counters, accumulators, and input validation.
* **Most difficult logic:** Determining the final status using the required priority order.
* **Problem I faced:** Correctly validating practice scores and handling absent days without affecting calculations.
* **How I solved it:** Used a validation loop for scores and `continue` for absent days so that calculations only used attempted scores.
---
## Team Lead  Requirement
|Member Name	|	PrepTrack Repository Link |	Submission Status|
|               |                             |                  |
---

## Repository Structure

```text
preptrack-Ranadeep/
├── main.py
└── README.md
```

---

## Final Status

* Program Working: **Yes**
* Mandatory Tests Completed: **Yes**
* README Completed: **Yes**
* Ready for Submission: **Yes**
