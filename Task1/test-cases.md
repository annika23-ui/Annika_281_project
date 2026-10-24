# Five synthetic test cases

These cases test the **design on paper**. They are invented examples, not real student submissions. No software was executed.

| # | Scenario and synthetic input | Expected workflow | Recovery / control |
|---|---|---|---|
| 1 | **Normal:** “The water cooler on the second floor has been empty for a week.” Category: Facilities. | Code issued; status `Received`; coordinator triages at weekly review; assigns to the facilities role; status changes to `Assigned` and `In progress`; final status and a safe summary are visible through the private code lookup. | If no action-owner update arrives within 14 days after assignment, escalate to the supervisor. Do not promise the repair date. |
| 2 | **Missing information:** “Fix the thing near the gate.” Category: Other. | Status becomes `Needs information`; tracking page asks, “Which item and which gate/area do you mean?” | If no clarification arrives within 14 days, close as `Declined — insufficient information`, with the reason visible. Allow resubmission. |
| 3 | **Duplicate:** Three submissions over two weeks ask for more evening bus timings. | Coordinator checks they concern the same route/time issue, links later items to the first, marks them `Duplicate`, and shows an aggregate count of three on the coordinator's internal view. | If the requests concern different routes, split them into separate items and correct the links. Do not expose one student's text to another. |
| 4 | **Outside authority:** “Please reduce the examination fee.” | Status becomes `Out of scope` for the coordinator; it is routed to the authorised administrative/fee decision role only if college policy permits. The tracking page says a decision is pending and does not promise a reduction. | If no acknowledgement arrives within 14 days, escalate through the approved channel. The coordinator cannot approve fee changes. |
| 5 | **Failed step:** Coordinator is absent and the weekly review is missed. | The deputy is notified and takes ownership of the queue; existing items retain their statuses and next-review dates. | If both roles are unavailable, escalate to the supervisor. For a system outage, use the authorised physical-box fallback and review it weekly. Safety concerns follow the college's existing urgent procedure. |

## Walkthrough result

All five designs include a status, responsible role and recovery path. The duplicate case includes a correction path; the out-of-scope case respects approval limits; the failure case includes a backup. **Result: design walkthrough passed against the stated requirements, but operational testing is not applicable because no software was built.**
