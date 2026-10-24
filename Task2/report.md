# Task 2 — Curriculum audit and redesign for 2030

> **Student proposal, not an official syllabus revision.** This audit uses the published IFHE/IcfaiTech B.Tech CSE (Artificial Intelligence & Data Science) programme structure as its course-map source. The student identifies their cohort as **2023–2027**. The separate cohort-specific Academic Regulations document was not supplied. The full-programme total is 165 credits. The itemized course map accounts for 144 credits; the remaining 21 credits are represented as an aggregate KEEP entry.

## 1. Scope, programme and evidence status

| Item | Entry | Status |
|---|---|---|
| Institution | IFHE Hyderabad, IcfaiTech | Official public programme page |
| Programme | B.Tech CSE (Artificial Intelligence & Data Science) | Matches the programme name on the public IFHE structure page |
| Cohort | 2023–2027 | Student-provided; public structure page used as the course-map source |
| Baseline | 165-credit full programme (student-confirmed); 144 credits itemized in the published map plus 21 aggregate credits | Full total supplied by student; 21-credit detail not mapped |
| Proposal | Keep, update, reduce or add course content while keeping the full-programme total at 165 credits | Student proposal |

Official public structure: https://www.ifheindia.org/icfai-tech-school-hyderabad/icfaitech-btech-program-structure. Academic-features page: https://www.ifheindia.org/icfai-tech-school-hyderabad/academics/icfaitech-academic-features. 

**Important baseline limitation:** the public page prints 24-credit totals for Semesters V and VI, but the itemized courses for the AI & Data Science branch each add to 23. This report uses the itemized course credits. The itemized map covers 144 credits across Semesters I–VI plus Summer IP201. 165-credit programme total, the remaining 21 credits are included as an aggregate KEEP line. The detailed allocation of those credits must be confirmed against cohort-specific records.

## 2. Summary of proposed changes

| Status | Proposed change | Credits affected |
|---|---|---:|
| ADD | API Design, Integration and Python Automation (Sem II, 3); Generative AI Application Engineering (Sem V, 4); AI Output Verification and Governance (Sem VI, 3) | 10 added |
| REDUCE | ES102 Digital Fabrication 3→2; DS201 Introduction to IoT 3→2; DS212 Machine Learning 4→3; DS303 Blockchain Technology 3→2; move DS307 Computer Vision and DS308 Big Data systems from required core to elective availability (3 credits each) | 10 removed from required-core allocation |
| UPDATE | ES202 Industry Coding Practices (4); DS202 Database Management Systems (4); DS305 Data Wrangling and Visualization (3); DS310 Deep Learning (4) | 15 course credits with revised content |
| KEEP | All remaining courses and foundations, including the 21-credit aggregate remainder pending detailed mapping | 131 unchanged credits plus 9 retained credits in reduced courses, as detailed in the calculator |

The additions total 10 credits and the reductions total 10 credits, so the full-programme total remains **165 credits**. Counting every credit in an updated course as affected gives 35/165 = **21.2%**, within the assignment's approximate 20–25% target. Counting only structural additions and reductions gives 20/165 = **12.1%**; both figures are reported to avoid overstating the size of structural change.

Proposed totals for the itemized rows: I 21, II 24, III 24, IV 24, Summer 5, V 23, VI 23, plus 21 aggregate credits held unchanged. These are a design proposal, not approved course loads.

## 3. Rationale and course-level design

1. **API and automation practice (ADD-01).** Add a short applied course in Sem II after introductory programming. Topics: REST APIs, JSON, Python automation, input validation, error handling and basic test design. Verify whether Python is already taught in the cohort's programming course before finalizing prerequisites.
2. **Applied generative AI (ADD-02).** Add a Sem V course covering retrieval-augmented generation (RAG), basic agent workflows, data preparation, evaluation and deployment constraints. It should build on databases, programming and machine-learning concepts rather than assume students can use AI tools without foundations.
3. **AI output verification (ADD-03).** Add a Sem VI course on test design, source checking, evaluation metrics, bias/privacy risks, reproducibility, audit logs and human approval boundaries. Students should compare AI outputs with known test cases and document failures.
4. **ES202 update.** Include AI-assisted coding only when students explain, test and revise the generated code. Require a short record of prompts, changed code and tests.
5. **DS202 update.** Add practical SQL debugging, role-based access, constraints, audit tables and data-quality checks using synthetic data.
6. **DS305 update.** Add data provenance, missing-value handling, leakage checks, reproducible pipelines and validation of AI-generated data-cleaning suggestions.
7. **DS310 update.** Add evaluation beyond accuracy, validation/test separation, reproducibility, model limitations and clear reporting of failure cases.
8. **Elective flexibility.** DS307 Computer Vision and DS308 Big Data systems are proposed to move out of compulsory core status while remaining available as electives, subject to prerequisites and programme rules. This does not mean these topics are obsolete.
9. **Small one-credit trims.** The proposed reductions to ES102, DS201, DS212 and DS303 are the weakest part of the proposal. They should proceed only after mapping every current learning outcome to the reduced credit allocation and obtaining faculty review. A small job-description sample cannot prove that a topic is unnecessary.
10. **Foundations remain.** Retain mathematics, algorithms, programming, databases, operating systems, networks and architecture. A curriculum redesign should add applied capability without weakening the foundations needed to understand and verify AI systems.

## 4. Job-description evidence

Three employer-owned Accenture role pages were reviewed as a small exploratory sample on 23 October 2026. The source log records the experience level, requirements visible on each page and course links. 

| Employer role | Recurring signal | Curriculum implication | Limitation |
|---|---|---|---|
| AI/ML Computational Science Associate (0–1 year) | Python, OOP, data structures, SQL, REST APIs, Git, SDLC, testing | Keep core programming and data foundations; consider ADD-01 for applied API and test practice | One early-career role only |
| AI–Hi Tech–Data Science Associate 3 (0–2 years) | Python, SQL, GenAI fundamentals, prompt engineering, APIs, RAG, cloud exposure, validation and documentation | ADD-02 applied GenAI; ADD-03 evaluation and governance; update database and engineering practice | Mixed AI/analytics role; not all skills are necessarily entry requirements |
| GenAI Engineering Internship | Python prototypes, RAG, prompt design, output evaluation, hallucination checks and documentation | Add practical GenAI labs and explicit evaluation; use SP301 capstone to demonstrate tested workflow | Internship, not permanent employment; page may change |

The three examples come from one employer and are not representative statistics. They support prioritising hands-on practice in programming, APIs, data handling, testing, documentation and AI-output evaluation. They do **not** establish that any current course is unnecessary, or forecast all 2030 roles. The source log includes direct links and limitations.

## 5. Exercises across five subjects

Five worked examples are recorded in `evidence/ai-use-record.md`: DBMS, algorithms, probability, operating systems and machine-learning model verification. `scripts/run_exercises.py` runs all five (SQL through SQLite, the algorithm's call count, the probability calculation, a Round Robin simulation and an imbalance/leakage demonstration). Its saved output is in `evidence/exercise-run-output.txt`. 

## 6. Capstone link to Task 1

The Task 1 suggestion-box workflow becomes a proposed lab inside SP301 Special Project. Students use only synthetic suggestion records (`data/synthetic_suggestions.csv`), implement intake/status/ownership/approval/audit behavior, and test normal, missing-information, duplicate, unauthorized and failed-step cases. The capstone does not claim that the college has approved or deployed the system. Full proposal: `capstone/capstone-proposal.md`; prerequisites, milestones and acceptance tests: `capstone/capstone-addendum.md`.

## 7. Feedback and validation

No faculty or graduate feedback has been obtained. The feedback log says so explicitly. The next validation step is to ask a faculty member or recent graduate to review (a) the one-credit reductions, (b) prerequisites for the new courses, and (c) whether the proposed credit balance is feasible under the actual cohort-specific regulations. Do not add a feedback claim unless a real response is received.

## 8. What would change my mind

The least certain changes are the small one-credit reductions and the move of DS307/DS308 from core to elective availability. I would reverse or revise them if faculty identify essential learning outcomes that cannot fit in fewer credits, if the cohort-specific regulations require the current structure, or if a broader and more relevant sample of entry-level job descriptions shows different priorities. I would also reconsider ADD-02's core status if prerequisites or broader employer evidence do not justify it.

## 9. Limitations

- The public page's Semester V and VI itemized credit totals conflict with its printed totals; the report uses itemized values transparently.
- The job-description sample is small, may include experienced roles, and must be rechecked against employer-owned pages.
- New courses and all proposed credit changes require faculty review and formal approval.
- No faculty/graduate feedback is claimed. 
