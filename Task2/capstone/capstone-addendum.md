# Capstone addendum — prerequisites, milestones and demonstration of value

This addendum is appended to `capstone-proposal.md` and closes the gaps between that proposal and the Task 2 brief. The capstone is a **proposed** lab inside SP301 Special Project (Semester VI). It is not an approved or deployed system.

## 1. Prerequisite knowledge

| Needed before the lab | Where students get it (published course map / proposal) |
|---|---|
| Relational tables, constraints, SQL queries | DS202 Database Management Systems (Sem III, updated in this proposal to include audit tables and role-based access) |
| Programming and basic automation in Python | ES202 Industry Coding Practices (Sem IV); ADD-01 API Design, Integration and Python Automation (proposed, Sem II) |
| Data cleaning and simple summaries | DS305 Data Wrangling and Visualization (Sem V) |
| Checking AI output against examples | ADD-03 AI Output Verification and Governance (proposed, Sem VI); this lab is where it is practised |

Where a prerequisite is a proposed course, a student who has not taken it can use the DS202 and ES202 material alone; the lab does not depend on the new courses being approved.

## 2. Synthetic dataset

`../data/synthetic_suggestions.csv` replaces the earlier `synthetic_requests.csv`, which described booking requests and did not match the suggestion workflow. The new file has 12 invented rows (G001–G012). Each row has an actor role, a requested action, whether the details are complete, a duplicate pointer, whether the actor is authorised, the result of the step, a synthetic days-to-first-review figure and the expected status. It contains no names, IDs, marks, fees, signatures, credentials or private messages.

## 3. Milestones (one semester, about 14 weeks)

| Week | Milestone | Evidence students submit |
|---|---|---|
| 2 | Process map and status model agreed with the supervisor | Diagram; list of statuses, owners, approval boundary |
| 5 | Intake form and tracker with reference codes | Working tracker on synthetic data |
| 8 | Role checks and audit log | Log showing a blocked unauthorised action |
| 10 | Acceptance tests pass | Output of `check_suggestions.py`-style tests, all five cases |
| 12 | Failure drill and measured-value comparison | Recovery notes; before/after table |
| 14 | Reflection and handover | What would make them stop the pilot |

## 4. Acceptance tests

The five required cases are rows in the dataset and are run by `check_suggestions.py`:

| Case | Rows | Expected result |
|---|---|---|
| Normal request | G001, G002, G012 | Assigned |
| Missing information | G003, G009 | Needs information |
| Duplicate | G004, G010 | Duplicate, linked to the earlier record |
| Unauthorised request | G005, G011 | Blocked (logged) |
| Failed step | G006 | Failed-retry, nothing lost |

Approved and declined outcomes (G007, G008) are only possible for the coordinator role. A student passes the milestone when the program's computed status matches `expected_status` on all rows.

## 5. How students demonstrate the three required qualities

**Approval control.** Only the coordinator role can approve, decline or change a status. Rows G005 and G011 attempt these actions as an anonymous student; the tracker must refuse and write an audit entry (timestamp, role, attempted action). No suggestion becomes "Accepted" because it was submitted.

**Failure recovery.** Row G006 simulates a failed notification. The suggestion must stay stored with status Failed-retry. Students run a drill: switch the portal off, record three suggestions in the manual fallback (physical box or approved manual process), switch it back on and reconcile. They submit the reconciliation notes. Success means the count of stored suggestions before and after is identical.

**Measured value.** Students compare two measured quantities from the audit log: time to first review and the share of suggestions that need no follow-up. The checker shows the method on synthetic numbers (median 5 days, maximum 7 days, n = 9). These numbers only demonstrate the calculation. They are **not** evidence about the real college process, which has not been measured. A pilot must replace them with real timestamps before any claim about time saved.

## 6. Limits

- The lab uses only synthetic data and has no real users.
- No college role has approved it. Using an existing college feedback portal, or collecting any real suggestions, needs approval from an authorised college role.
- The tests are rule checks on invented rows, not user testing.
