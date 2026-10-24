#!/usr/bin/env python3
"""Runs the five worked exercises from evidence/ai-use-record.md and prints the results.

Usage:  python3 scripts/run_exercises.py
Needs only the Python 3 standard library (sqlite3 is built in).
Save your own run with:  python3 scripts/run_exercises.py | tee evidence/exercise-run-output.txt
"""
import math
import random
import sqlite3
import sys
import platform
from datetime import datetime


def header(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# ---------------------------------------------------------------- 1. DBMS
def exercise_dbms():
    header("1. DBMS: departments whose DBMS average beats the overall DBMS average")
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.executescript("""
        CREATE TABLE students(id INTEGER PRIMARY KEY, dept TEXT);
        CREATE TABLE enrolments(student_id INTEGER, course TEXT, score REAL);
        INSERT INTO students VALUES (1,'CSE'),(2,'CSE'),(3,'ECE'),(4,'ECE'),(5,'MECH');
        INSERT INTO enrolments VALUES
            (1,'DBMS',90),(2,'DBMS',80),   -- CSE avg 85
            (3,'DBMS',60),(4,'DBMS',70),   -- ECE avg 65
            (5,'DBMS',75),                 -- MECH avg 75
            (1,'OS',10);                   -- non-DBMS row must be ignored
    """)
    overall = cur.execute("SELECT AVG(score) FROM enrolments WHERE course='DBMS'").fetchone()[0]
    rows = cur.execute("""
        SELECT s.dept
        FROM students AS s
        JOIN enrolments AS e ON e.student_id = s.id
        WHERE e.course = 'DBMS'
        GROUP BY s.dept
        HAVING AVG(e.score) > (SELECT AVG(score) FROM enrolments WHERE course = 'DBMS')
        ORDER BY s.dept;
    """).fetchall()
    result = [r[0] for r in rows]
    print(f"Overall DBMS average = {overall:.2f}  (CSE 85, ECE 65, MECH 75)")
    print("Query result:", result)
    assert result == ["CSE"], result
    print("CHECK PASSED: only CSE is above the overall average.")


# ------------------------------------------------------------ 2. Algorithms
CALLS = 0


def f(n):
    """The exact function from the exercise."""
    global CALLS
    CALLS += 1
    return 1 if n <= 1 else f(n // 2) + f(n // 2) + n


def exercise_algorithms():
    global CALLS
    header("2. Algorithms: running time of f(n) = f(n//2) + f(n//2) + n  (f(1)=1)")
    print(f"{'n':>10} {'calls':>10} {'2n-1':>10} {'calls/n':>9} {'calls/(n log2 n)':>17}")
    for k in (4, 8, 12, 16, 20):
        n = 2 ** k
        CALLS = 0
        f(n)
        print(f"{n:>10} {CALLS:>10} {2*n-1:>10} {CALLS/n:>9.3f} {CALLS/(n*k):>17.4f}")
        assert CALLS == 2 * n - 1
    print("calls/n stays at about 2 (constant), while calls/(n log2 n) keeps shrinking.")
    print("Each call does O(1) work (one addition), so T(n) = 2T(n/2) + Theta(1) = Theta(n).")
    print("CHECK PASSED: number of calls is exactly 2n-1, i.e. Theta(n), not Theta(n log n).")


# ---------------------------------------------------------- 3. Probability
def exercise_probability():
    header("3. Probability: P(disease | positive)")
    sens, spec, prev = 0.95, 0.90, 0.02
    tp = sens * prev
    fp = (1 - spec) * (1 - prev)
    ppv = tp / (tp + fp)
    print(f"true positive  = {tp:.4f}")
    print(f"false positive = {fp:.4f}")
    print(f"P(positive)    = {tp+fp:.4f}")
    print(f"P(disease|+)   = {ppv:.4f}  ({ppv*100:.1f}%)")
    assert abs(ppv - 0.1624) < 1e-4
    # Monte-Carlo cross-check
    random.seed(1)
    pos = hit = 0
    for _ in range(400_000):
        d = random.random() < prev
        t = random.random() < (sens if d else 1 - spec)
        if t:
            pos += 1
            hit += d
    print(f"Monte-Carlo cross-check (400k people): {hit/pos:.4f}")
    print("CHECK PASSED.")


# ---------------------------------------------------------- 4. Round Robin
def round_robin(procs, q):
    """procs: list of (name, arrival, burst). New arrivals join the queue before a pre-empted process."""
    procs = sorted(procs, key=lambda p: p[1])
    remaining = {n: b for n, a, b in procs}
    arrival = {n: a for n, a, b in procs}
    burst = {n: b for n, a, b in procs}
    t, i, queue, timeline, done = 0, 0, [], [], {}
    while len(done) < len(procs):
        while i < len(procs) and procs[i][1] <= t:
            queue.append(procs[i][0]); i += 1
        if not queue:
            t = procs[i][1]; continue
        n = queue.pop(0)
        run = min(q, remaining[n])
        timeline.append((n, t, t + run))
        t += run
        remaining[n] -= run
        while i < len(procs) and procs[i][1] <= t:   # arrivals first ...
            queue.append(procs[i][0]); i += 1
        if remaining[n] > 0:
            queue.append(n)                           # ... then the pre-empted process
        else:
            done[n] = t
    wait = {n: done[n] - arrival[n] - burst[n] for n in done}
    return timeline, done, wait


def exercise_round_robin():
    header("4. Operating systems: Round Robin, quantum = 2")
    timeline, done, wait = round_robin([("P1", 0, 5), ("P2", 1, 3), ("P3", 2, 1), ("P4", 3, 2)], 2)
    print(" | ".join(f"{n} {s}-{e}" for n, s, e in timeline))
    print("Completion:", dict(sorted(done.items())))
    print("Waiting   :", dict(sorted(wait.items())))
    avg = sum(wait.values()) / len(wait)
    print(f"Average waiting time = {avg}")
    assert done == {"P1": 11, "P2": 10, "P3": 5, "P4": 9}
    assert avg == 4.5
    print("CHECK PASSED.")


# ------------------------------------------------- 5. ML: imbalance + leakage
def exercise_ml():
    header("5. ML: why accuracy misleads on imbalanced data; leakage demo (pure Python)")
    random.seed(7)
    y = [1 if random.random() < 0.02 else 0 for _ in range(10_000)]
    pred = [0] * len(y)                                  # 'always negative' classifier
    tp = sum(1 for a, b in zip(y, pred) if a == 1 and b == 1)
    fn = sum(1 for a, b in zip(y, pred) if a == 1 and b == 0)
    acc = sum(1 for a, b in zip(y, pred) if a == b) / len(y)
    recall = tp / (tp + fn)
    print(f"positives = {sum(y)} of {len(y)}")
    print(f"'Always negative' model: accuracy = {acc:.3f}, recall = {recall:.3f}")
    assert acc > 0.97 and recall == 0
    # leakage: scaling statistics computed on ALL data vs TRAIN only
    data = [random.gauss(0, 1) for _ in range(900)] + [random.gauss(6, 1) for _ in range(100)]
    train, test = data[:800], data[800:]
    mean_all = sum(data) / len(data)
    mean_train = sum(train) / len(train)
    print(f"mean using all rows (leaky) = {mean_all:.4f}; mean using train only = {mean_train:.4f}")
    print("The two differ, so fitting preprocessing before the split lets test data influence training.")
    print("CHECK PASSED (conceptual demonstration, no real dataset or model).")


if __name__ == "__main__":
    print("run_exercises.py")
    print("Run date/time :", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Python        :", sys.version.split()[0], "on", platform.platform())
    for fn in (exercise_dbms, exercise_algorithms, exercise_probability, exercise_round_robin, exercise_ml):
        fn()
    print("\nALL FIVE EXERCISES RAN AND PASSED THEIR CHECKS.")
