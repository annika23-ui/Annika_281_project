# Calculations: staff effort, student effort and waiting time

**Important:** the figures below are illustrative estimates, not measured campus results. Every workload input is in `calc.py` and labelled as an assumption. Re-run the script after replacing any assumption with evidence.

## Assumptions

- Scenarios: 20, 40, 80 or 160 submissions/month.
- 50% actionable, 15% duplicates and 10% unusable. For the model these are separate workload rates; in real life categories may overlap, so measured categories should be defined consistently.
- Current process: 15 minutes to collect; 1.5 minutes to read/log each slip; 6 minutes to route each actionable slip.
- Proposed process: 1 minute triage per submission; 0.5 minute to merge each duplicate; 3 minutes to route each actionable submission; 5 minutes per weekly queue check; 3 minutes per unusable item for moderation; 1 minute per actionable item for status updates; five student queries per month at five minutes each; 15 minutes of owner review each week.
- Tool upkeep: 30 minutes/month for a new tool, or 10 minutes/month if an existing portal can be reused.
- Student effort: physical submission takes an assumed 3 minutes; online submission takes 1.5 minutes.

## Formulae

Let \(N\) be submissions per month.

**Current staff effort**

\[
15 + 1.5N + 6(0.5N) = 15 + 4.5N
\]

**Proposed staff effort**

\[
N + 0.5(0.15N) + 3(0.5N) + 20 + 3(0.10N) + 1(0.5N) + 25 + 60 + M
\]

where \(M=30\) minutes for a new tool or \(M=10\) minutes for an existing portal. The fixed 20 minutes is four weekly checks; 25 minutes is five student queries; 60 minutes is four weekly owner reviews.

**Student time saved**

\[
N(3.0 - 1.5) = 1.5N \text{ minutes/month}
\]

Net staff saving is current staff minutes minus proposed staff minutes. A negative value means staff time increases. Student minutes are shown separately; adding student and staff minutes is a simple time comparison, not a financial or welfare valuation.

## Results

| Submissions/month | Current staff min | New tool min | Net staff saving (new tool) | Existing portal min | Net staff saving (portal) | Student min saved |
|---:|---:|---:|---:|---:|---:|---:|
| 20 | 105.0 | 202.5 | -97.5 | 182.5 | -77.5 | 30.0 |
| 40 | 195.0 | 270.0 | -75.0 | 250.0 | -55.0 | 60.0 |
| 80 | 375.0 | 405.0 | -30.0 | 385.0 | -10.0 | 120.0 |
| 160 | 735.0 | 675.0 | 60.0 | 655.0 | 80.0 | 240.0 |

At 40 submissions/month, the new process uses an estimated 75 extra staff minutes per month if a new tool is built, or 55 extra staff minutes if the existing portal is reused. Adding estimated student time saved (60 minutes) gives -15 minutes/month for a new tool and +5 minutes/month for an existing portal. This combined measure should be interpreted cautiously: one minute of staff time and one minute of student time are not necessarily equivalent in value.

**Staff-time break-even:** approximately 107 submissions/month for a new tool and 89/month for an existing portal, under the current assumptions.

## Waiting time

If submissions arrive evenly during a review cycle, the average wait before first review is half the cycle length.

| Review cycle | Estimated average wait | Estimated maximum wait |
|---|---:|---:|
| Monthly, assumed 30-day cycle | 15 days | 30 days |
| Weekly, 7-day cycle | 3.5 days | 7 days |
| Daily, 1-day cycle | 0.5 days | 1 day |

These are expected waiting times before first review, not time to resolution. A weekly review is only effective if the coordinator or deputy reliably performs it.

## Interpretation and decision

The proposal does **not** automatically save staff time at low or medium volume because it adds status updates, moderation, student queries, owner reviews and tool upkeep. The model suggests:
- reuse the existing portal rather than create a new tool, if privacy and tracking needs can be met;
- consider a lighter weekly paper-box review if volume is very low and digital tracking is not feasible;
- measure actual volume and time during a short pilot before deciding whether to scale.

The calculations should be treated as a decision aid, not proof of actual savings.
