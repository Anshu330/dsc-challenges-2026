#!/usr/bin/env python3
"""
verify_python_basics.py — Automated Prep Self-Grader for Week 0
Data Science Club (DSC KLE) — KLE Technological University

Run locally inside week-00-python-fundamentals/:
    python verify_python_basics.py
"""

import json
import sys
import tempfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from exercises import (
    StudentRecord,
    analyze_pod_scores,
    evaluate_attendance_status,
    safe_parse_float,
    summarize_csv_to_json,
)


def run_checks():
    print("\n+--------------------------------------------------------------+")
    print("|    DSC KLE 2026 -- WEEK 0 PYTHON BASICS VERIFICATION         |")
    print("+--------------------------------------------------------------+\n")

    passed = 0
    total = 4

    # Check 1: Conditionals & Error Handling
    try:
        assert evaluate_attendance_status(8, 10) == "ELIGIBLE"
        assert evaluate_attendance_status(7, 10) == "WARNING"
        assert evaluate_attendance_status(4, 10) == "SHORTAGE"
        assert evaluate_attendance_status(0, 0) == "NO_SESSIONS"
        assert safe_parse_float("92.5") == 92.5
        assert safe_parse_float("not-a-number", default=-1.0) == -1.0
        print("[PASS] Check 1/4: Conditionals & try/except input handling")
        passed += 1
    except Exception as exc:
        print(f"[FAIL] Check 1/4: Conditionals & try/except -> {exc}")

    # Check 2: Collections & Comprehensions
    try:
        sample = [
            ("01FE25BCS122", "Parth's POD", 88.0),
            ("01FE25BCS122", "Parth's POD", 88.0),
            ("01FE26BCS027", "Parth's POD", 74.0),
            ("01FE25BCI049", "Aditi's POD", 92.0),
        ]
        res = analyze_pod_scores(sample)
        assert res["unique_student_count"] == 3, f"Expected 3 unique USNs, got {res['unique_student_count']}"
        assert set(res["high_scorers"]) == {"01FE25BCS122", "01FE25BCI049"}
        assert res["pod_averages"]["Aditi's POD"] == 92.0
        print("[PASS] Check 2/4: Sets, Dicts & List Comprehensions")
        passed += 1
    except Exception as exc:
        print(f"[FAIL] Check 2/4: Collections & Comprehensions -> {exc}")

    # Check 3: File I/O Pipeline
    try:
        csv_file = Path(__file__).resolve().parent / "sample_cohort.csv"
        with tempfile.TemporaryDirectory() as tmpdir:
            out_json = Path(tmpdir) / "summary.json"
            summary = summarize_csv_to_json(str(csv_file), str(out_json))
            assert out_json.exists(), "Output JSON file was not created"
            loaded = json.loads(out_json.read_text(encoding="utf-8"))
            assert loaded["total_students"] == 5
            assert loaded["branches"] == ["BAR", "BCI", "BCS", "BMS"]
            assert round(loaded["average_score"], 2) == 86.8
            assert summary["total_students"] == 5
        print("[PASS] Check 3/4: File I/O (with open, csv, json)")
        passed += 1
    except Exception as exc:
        print(f"[FAIL] Check 3/4: File I/O -> {exc}")

    # Check 4: Intro OOP
    try:
        rec = StudentRecord("01fe25bcs122", "Garima")
        assert rec.usn == "01FE25BCS122"
        assert rec.average() == 0.0
        rec.add_score(80.0)
        rec.add_score(90.0)
        assert rec.average() == 85.0
        assert rec.is_passing() is True
        print("[PASS] Check 4/4: StudentRecord OOP Class")
        passed += 1
    except Exception as exc:
        print(f"[FAIL] Check 4/4: OOP Class -> {exc}")

    print(f"\nScore: {passed}/{total} checks passed.")
    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    run_checks()
