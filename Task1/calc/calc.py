"""Illustrative workload model for the college suggestion-box workflow.

All inputs are assumptions until replaced by measured or staff-confirmed values.
Run with: python3 calc.py
"""
ASSUMPTIONS = {
    "actionable_share": 0.50,
    "duplicate_share": 0.15,
    "unusable_share": 0.10,
    "cur_collect": 15,
    "cur_read_per_slip": 1.5,
    "cur_route_per_actionable": 6,
    "new_triage_per_slip": 1.0,
    "new_merge_per_duplicate": 0.5,
    "new_route_per_actionable": 3,
    "new_weekly_check": 5,
    "new_moderate_per_unusable": 3,
    "new_status_update_per_actionable": 1,
    "new_student_queries": 5,
    "new_student_query_time": 5,
    "new_maintenance_OWN_TOOL": 30,
    "new_maintenance_EXISTING_PORTAL": 10,
    "new_owner_review_per_week": 15,
    "student_drop_physical": 3.0,
    "student_drop_online": 1.5,
}
A = ASSUMPTIONS

def current(n):
    actionable = n * A["actionable_share"]
    return A["cur_collect"] + n * A["cur_read_per_slip"] + actionable * A["cur_route_per_actionable"]

def proposed(n, option):
    actionable = n * A["actionable_share"]
    duplicates = n * A["duplicate_share"]
    unusable = n * A["unusable_share"]
    if option == "own":
        maintenance = A["new_maintenance_OWN_TOOL"]
    elif option == "portal":
        maintenance = A["new_maintenance_EXISTING_PORTAL"]
    else:
        raise ValueError("option must be 'own' or 'portal'")
    return (
        n * A["new_triage_per_slip"]
        + duplicates * A["new_merge_per_duplicate"]
        + actionable * A["new_route_per_actionable"]
        + 4 * A["new_weekly_check"]
        + unusable * A["new_moderate_per_unusable"]
        + actionable * A["new_status_update_per_actionable"]
        + A["new_student_queries"] * A["new_student_query_time"]
        + maintenance
        + 4 * A["new_owner_review_per_week"]
    )

def student_saved(n):
    return n * (A["student_drop_physical"] - A["student_drop_online"])

def breakeven(option):
    for n in range(1, 10000):
        if current(n) - proposed(n, option) >= 0:
            return n
    return None

if __name__ == "__main__":
    print("slips/month | current | proposed(own tool) | net staff saving (own) | proposed(existing portal) | net staff saving (portal) | student time saved")
    for n in (20, 40, 80, 160):
        c, own, portal = current(n), proposed(n, "own"), proposed(n, "portal")
        print(f"{n:>11} | {c:>7.1f} | {own:>18.1f} | {c-own:>22.1f} | {portal:>25.1f} | {c-portal:>25.1f} | {student_saved(n):>18.1f}")
    print()
    print("Break-even submissions/month (staff time only):")
    print(f"  New tool: {breakeven('own')}")
    print(f"  Existing portal: {breakeven('portal')}")
    print()
    for label, days in (("monthly review (30-day cycle)", 30), ("weekly review (7-day cycle)", 7), ("daily review (1-day cycle)", 1)):
        print(f"Average wait before first review, {label}: {days/2:.1f} days; maximum {days} days")
