#!/usr/bin/env python3
"""Acceptance-test runner for the Student Suggestion Workflow Lab.

Reads ../data/synthetic_suggestions.csv, recomputes each row's status from the rules below
and compares it with expected_status. Also prints a small 'measured value' summary.
All data is synthetic; the summary shows the METHOD, not a real result.

Usage (from Task2/):  python3 capstone/check_suggestions.py
"""
import csv
import statistics
from collections import Counter
from pathlib import Path

CSV = Path(__file__).resolve().parent.parent / "data" / "synthetic_suggestions.csv"


def decide(row):
    """Rule order matters: authorisation, then step failure, then duplicate, then completeness."""
    if row["authorised"] != "yes":
        return "Blocked (logged)"           # approval boundary: only the coordinator role may approve/decline/change status
    if row["step_result"] != "ok":
        return "Failed-retry"               # failure recovery: nothing is lost, coordinator retries or uses manual fallback
    if row["requested_action"] == "approve":
        return "Accepted"
    if row["requested_action"] == "decline":
        return "Declined"
    if row["duplicate_of"]:
        return "Duplicate"
    if row["details_complete"] != "yes":
        return "Needs information"
    return "Assigned"


def main():
    rows = list(csv.DictReader(CSV.open(newline="")))
    failures = 0
    print(f"{'id':<6}{'action':<15}{'computed':<18}{'expected':<18}result")
    for r in rows:
        got = decide(r)
        ok = got == r["expected_status"]
        failures += not ok
        print(f"{r['suggestion_id']:<6}{r['requested_action']:<15}{got:<18}{r['expected_status']:<18}{'PASS' if ok else 'FAIL'}")
    print(f"\n{len(rows) - failures}/{len(rows)} rows match expected status.")

    # coverage of the five required cases
    required = {"Assigned": "normal", "Needs information": "missing information", "Duplicate": "duplicate",
                "Blocked (logged)": "unauthorized request", "Failed-retry": "failed step"}
    present = Counter(decide(r) for r in rows)
    for status, label in required.items():
        print(f"case coverage - {label:<22}: {present[status]} row(s)")
        assert present[status] >= 1, f"no test row for {label}"

    # measured-value method (synthetic numbers)
    days = [int(r["days_to_first_review"]) for r in rows if r["days_to_first_review"]]
    print(f"\nSynthetic days to first review: median {statistics.median(days)}, max {max(days)} (n={len(days)}).")
    print("Method demo only. A pilot would replace these with real timestamps from the audit log.")
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
