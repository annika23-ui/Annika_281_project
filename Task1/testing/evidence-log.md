# Evidence log

**Prepared:** 24 October 2026  
**Scope:** suggestion-box workflow; no personal data collected.

## Classification

- **USER-SUPPLIED:** information provided in the assignment conversation or brief; not independently checked.
- **OBSERVED:** directly seen by the student.
- **TOLD:** supplied by a person with relevant responsibility.
- **ESTIMATE:** calculated from stated assumptions.
- **ASSUMPTION:** unverified working assumption.

| ID | Date | Entry | Classification | Source | Follow-up |
|---|---|---|---|---|---|
| E1 | 24 Oct 2026 | The workflow under study is a physical suggestion box in a college building/entrance. | USER-SUPPLIED | User's description of the task | Confirm the exact location by permitted observation. |
| E2 | 24 Oct 2026 | The box is checked around month-end / once a month. | USER-SUPPLIED | User's description of the task | Ask the responsible staff role whether this is accurate and whether exceptions exist. |
| E3 | 24 Oct 2026 | Slips may be untracked and students may not receive a status update. | ASSUMPTION | Not independently verified | Ask what happens after collection and whether any response channel exists. |
| E4 | 24 Oct 2026 | An existing online faculty-feedback system may be available for reuse. | USER-SUPPLIED / TO VERIFY | User's description of a similar online feedback form | Confirm whether it accepts suggestions, supports anonymity and allows tracking; do not access private submissions. |
| E5 | 24 Oct 2026 | If a box is checked every 30 days and submissions arrive evenly, expected wait to first review is 15 days and maximum wait is 30 days. | ESTIMATE | 30 ÷ 2; see `calculations.md` | Replace the 30-day cycle with the real schedule if confirmed. |
| E6 | 24 Oct 2026 | If submissions are reviewed every 7 days and arrive evenly, expected wait is 3.5 days and maximum wait is 7 days. | ESTIMATE | 7 ÷ 2; see `calculations.md` | Confirm the review schedule can be staffed. |
| E7 | 24 Oct 2026 | Actual submission volume is unknown. The model uses 20, 40, 80 and 160 submissions/month as scenarios. | ASSUMPTION | Scenario analysis only | Ask for a rough monthly range if staff can share it. |
| E8 | 24 Oct 2026 | Per-item handling times and category shares are assumed rather than measured. | ASSUMPTION | `calc.py` | Replace with measured times or estimates from the responsible role. |
| E9 | 24 Oct 2026 | Campus-level qualitative observation: suggestions can take a long time to be implemented. | USER-REPORTED OBSERVATION | User's account of the campus experience | This indicates a perceived delay but does not establish a measured average, number of delayed suggestions, or the cause of each delay. |
| E10 | 24 Oct 2026 | Verbal permission to proceed with the assignment/observation was given. | USER-REPORTED | User's clarification in this conversation | The name of the person, exact date, and scope of permission were not provided; do not invent them. Confirm any additional permission required before accessing records or the suggestion box. |
| E11 | 24 Oct 2026 | No timed observation, count of suggestions, or staff interview results have been supplied. | NOT MEASURED / NOT PROVIDED | Current project information | Treat the implementation-delay observation as qualitative; do not present it as a measured result. |

## Ethics

No names, student IDs, grades, contact details, private messages or identifiable staff details are included. The qualitative observation about slow implementation is not a measured delay. All test inputs are synthetic. Do not open the box, read private submissions, or access records unless the verbal permission explicitly covers that activity and the college's rules allow it.
