# Task 2 — Contribution and reflection

## Basis of the redesign

The course audit uses the official public IFHE/IcfaiTech B.Tech CSE (Artificial Intelligence & Data Science) programme-structure page as the course-level source, the full programme totals 165 credits, and a small desk-research sample of three employer-owned role pages recorded in `evidence/source-log.md`.

## Decisions proposed

- Add three applied courses: API Design, Integration and Python Automation (3 credits), Generative AI Application Engineering (4 credits), and AI Output Verification and Governance (3 credits).
- Reduce required-core allocation by 10 credits overall, including moving Computer Vision and Big Data Systems to elective availability and proposing four one-credit reductions. These reductions are low-confidence and require course-outcome mapping and faculty review before adoption.
- Update the content of Industry Coding Practices, Database Management Systems, Data Wrangling and Visualization, and Deep Learning without changing their credits.
- Keep the full programme total at 165 credits in the model. The 21-credit remainder is an aggregate KEEP row because its course-level allocation was not supplied; no course names have been invented.

## Evidence and limitations

- Employer pages are a small exploratory sample from one employer, not a representative job-market study or a forecast of 2030 demand. The access/review date is not a claimed posting date.
- The cohort-specific Academic Regulations were not supplied. All curriculum changes are proposals, not approved IFHE changes.
- The five subject exercises and 12 capstone acceptance cases were executed by scripts in the preparation environment. The data used in capstone checks are synthetic. These runs are reproducible artifacts, not evidence of a live campus deployment.
- The first draft of the algorithms exercise incorrectly suggested Θ(n log n). The corrected recurrence is Θ(n), because the recursion tree has 2n−1 calls and constant work per call.
- No faculty or graduate feedback is claimed.

## Reflection / revision triggers

The most uncertain changes are the one-credit reductions and moving DS307/DS308 from core to elective availability. Revise or reject these if faculty mapping shows essential outcomes cannot fit, the applicable cohort regulations require the existing structure, or a broader employer sample does not support the proposed emphasis. The new courses should be piloted with clear learning outcomes and assessed through code, tests, documentation and an oral explanation rather than tool use alone.
