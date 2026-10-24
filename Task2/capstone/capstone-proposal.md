# Capstone proposal — Student Suggestion Workflow Lab

**Connection to Task 1:** this capstone models the proposed replacement for a physical college suggestion box checked around monthly: an anonymous online intake (preferably through an existing feedback portal if it supports anonymous tracking) and weekly triage. The current process details and delays are based on the student's description; the time/volume figures in Task 1 are illustrative estimates, not measured results.

| Field | Entry |
|---|---|
| Host course | SP301 Special Project (existing published structure; verify against the 2023–2027 cohort rules) |
| Workflow | Anonymous student suggestions: intake, triage, assignment, approval, status update and closure |
| Data | Synthetic only: `../data/synthetic_suggestions.csv`; no real names, student IDs, marks, fees, credentials or private messages |
| Status | Proposed lab, not a deployed or college-approved system |

## Learning outcomes
1. Map a manual request process as steps, handoffs, statuses, owners and approval boundaries.
2. Build a small request tracker with role checks and an audit log using synthetic data.
3. Handle normal, missing-information, duplicate, unauthorized and failed-step cases.
4. Compare estimated/manual handling time with a proposed workflow, including review and support costs.
5. Test AI-generated classifications or reply drafts against explicit examples and require human review before sending anything.

## Proposed workflow
- **Intake:** accept suggestion text and optional category. Do not collect identifying information unless the college has a justified, approved need.
- **Tracking:** issue a random reference code; explain that anonymity depends on portal configuration and metadata, not just a form field.
- **Statuses:** Submitted → Needs information / Pending triage → Assigned → Under review → Accepted / Declined → Closed; also Duplicate and Failed-retry.
- **Owner:** a named coordinator and deputy manage weekly triage. The actual college role must be agreed before any pilot.
- **Approval:** only the authorised college role may mark a suggestion accepted for implementation. The system must not promise implementation merely because a suggestion was submitted.
- **Audit:** record status transitions, timestamp and role. Keep access limited and set a retention period under college policy.
- **Fallback:** if the portal fails, retain the physical box or a college-approved manual process; reconcile entries after recovery.
- **AI (optional):** may suggest a category or draft a missing-information message. A human reviews the draft before it is sent; AI must not decide approval or rejection.

## Synthetic acceptance tests

| Case | Expected result | Recovery / decision |
|---|---|---|
| Normal complete suggestion | Submitted, assigned for triage and given a reference code | Coordinator reviews during weekly triage |
| Missing information | Needs information; no claim of acceptance | Requester may add details if an anonymous follow-up method exists; otherwise keep the suggestion reviewable without assuming contact is possible |
| Duplicate | Duplicate flag and link to the earlier record | Coordinator decides whether to merge records |
| Unauthorized action | Action blocked and logged | Only an authorised role can approve or change restricted statuses |
| Failed step | Failed-retry status; no silent data loss | Coordinator retries or uses the approved manual fallback |

These cases are encoded as rows in the synthetic dataset and are checked by `check_suggestions.py` (rule checks on invented data, not user testing or a deployed system). Prerequisites, milestones and the demonstration of approval control, failure recovery and measured value are in `capstone-addendum.md`. The time-saved calculation should use the Task 1 model only as an illustrative scenario until real measurements are collected. A pilot should measure submission volume, time to first review, time to assignment, closure time, duplicate rate, handling time, support effort and privacy incidents before deciding whether to continue.

See also: [Capstone addendum](capstone-addendum.md).
