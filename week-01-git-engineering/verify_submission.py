#!/usr/bin/env python3
"""
verify_submission.py — Automated Sprint Self-Grader for Week 1
Data Science Club (DSC KLE) — KLE Technological University

Run this script locally inside your week-01-git-engineering/ folder:
    python verify_submission.py
"""

import sys
import os
import subprocess
import re
from pathlib import Path

# Ensure UTF-8 output handling on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# ANSI colors for terminal feedback (supported across modern Windows Terminal & Unix)
C_RESET = "\033[0m"
C_BOLD = "\033[1m"
C_GREEN = "\033[32m"
C_RED = "\033[31m"
C_YELLOW = "\033[33m"
C_CYAN = "\033[36m"
C_BLUE = "\033[34m"

def print_banner():
    print(f"\n{C_BOLD}{C_CYAN}+--------------------------------------------------------------+{C_RESET}")
    print(f"{C_BOLD}{C_CYAN}|     DSC KLE 2026 -- WEEK 1 SPRINT AUTO-VERIFICATION SUITE    |{C_RESET}")
    print(f"{C_BOLD}{C_CYAN}+--------------------------------------------------------------+{C_RESET}")
    print(f"{C_BLUE}Auditorium 2 * KLE Tech * Lead: Sarosh Kumar * Faculty: Prof. Sneha{C_RESET}\n")

def run_cmd(cmd_list, cwd=None):
    try:
        res = subprocess.run(cmd_list, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)
        return res.returncode == 0, res.stdout.strip(), res.stderr.strip()
    except Exception as e:
        return False, "", str(e)

def find_git_root(start_dir):
    curr = Path(start_dir).resolve()
    while curr != curr.parent:
        if (curr / ".git").exists():
            return curr
        curr = curr.parent
    return None

def main():
    print_banner()

    curr_dir = Path(__file__).parent.resolve()
    git_root = find_git_root(curr_dir)

    passed_checks = 0
    total_checks = 10

    # =========================================================================
    # PART 1: GIT & GITHUB ENGINEERING INFRASTRUCTURE
    # =========================================================================

    # CHECK 1: Git Repository Initialized
    print(f"{C_BOLD}[Check 1/10] Local Git Repository Initialized{C_RESET}")
    if git_root:
        passed_checks += 1
        print(f"  {C_GREEN}[PASS]{C_RESET} Found active Git root at: {git_root}\n")
    else:
        print(f"  {C_RED}[FAIL]{C_RESET} No .git repository found in current or parent directories.")
        print(f"    {C_YELLOW}Hint:{C_RESET} Make sure you cloned your fork using: git clone <your-repo-url>\n")

    # =========================================================================
    # CHECK 2: Git Identity Configured (user.name and user.email)
    # =========================================================================
    print(f"{C_BOLD}[Check 2/10] Terminal Git User Identity{C_RESET}")
    ok_name, user_name, _ = run_cmd(["git", "config", "user.name"], cwd=curr_dir)
    ok_email, user_email, _ = run_cmd(["git", "config", "user.email"], cwd=curr_dir)

    if ok_name and ok_email and user_name and user_email:
        passed_checks += 1
        print(f"  {C_GREEN}[PASS]{C_RESET} Git Author: {user_name} <{user_email}>\n")
    else:
        print(f"  {C_RED}[FAIL]{C_RESET} Git user.name or user.email is not configured.")
        print(f"    {C_YELLOW}Fix by running:{C_RESET}")
        print("      git config --global user.name \"Your Real Name\"")
        print("      git config --global user.email \"your.usn@kletech.ac.in\"\n")

    # =========================================================================
    # CHECK 3: Project Layout Directories (data/raw, notebooks, src)
    # =========================================================================
    print(f"{C_BOLD}[Check 3/10] Production DS Project Structure{C_RESET}")
    required_dirs = [
        curr_dir / "data" / "raw",
        curr_dir / "notebooks",
        curr_dir / "src"
    ]
    all_dirs_exist = True
    for d in required_dirs:
        rel = d.relative_to(curr_dir)
        if not d.exists():
            all_dirs_exist = False
            print(f"  {C_RED}[FAIL] Missing directory:{C_RESET} {rel}/")
        else:
            print(f"  {C_GREEN}[OK] Found directory:{C_RESET} {rel}/")

    if all_dirs_exist:
        passed_checks += 1
        print(f"  {C_GREEN}[PASS]{C_RESET} Standard data science hierarchy verified.\n")
    else:
        print(f"  {C_RED}[FAIL]{C_RESET} Incomplete project hierarchy.")
        print(f"    {C_YELLOW}Fix by creating:{C_RESET} mkdir -p data/raw notebooks src\n")

    # =========================================================================
    # CHECK 4: Production .gitignore
    # =========================================================================
    print(f"{C_BOLD}[Check 4/10] Production .gitignore Configuration{C_RESET}")
    gitignore_candidates = [curr_dir / ".gitignore", git_root / ".gitignore" if git_root else None]
    found_gi = None
    for cand in gitignore_candidates:
        if cand and cand.exists():
            found_gi = cand
            break

    if found_gi:
        with open(found_gi, "r", encoding="utf-8", errors="ignore") as f:
            gi_content = f.read()

        rules_to_check = {
            "virtual_env": re.search(r"\.venv|venv|env", gi_content, re.IGNORECASE),
            "secrets_env": re.search(r"\.env", gi_content),
            "ipynb_checkpoints": re.search(r"\.ipynb_checkpoints", gi_content)
        }

        missing_rules = [k for k, matched in rules_to_check.items() if not matched]

        if not missing_rules:
            passed_checks += 1
            print(f"  {C_GREEN}[PASS]{C_RESET} .gitignore properly ignores .env, .venv, and .ipynb_checkpoints.\n")
        else:
            print(f"  {C_YELLOW}[WARN]{C_RESET} Your .gitignore is missing patterns for: {', '.join(missing_rules)}")
            print(f"    {C_YELLOW}Hint:{C_RESET} Add `.venv/`, `.env`, and `.ipynb_checkpoints/` to your .gitignore.\n")
    else:
        print(f"  {C_RED}[FAIL]{C_RESET} No .gitignore file found in week-01 or repository root.\n")

    # =========================================================================
    # CHECK 5: Git Commit Progression & Conventional Commits
    # =========================================================================
    print(f"{C_BOLD}[Check 5/10] Git Progression & Semantic Commits{C_RESET}")
    ok_log, log_out, _ = run_cmd(["git", "log", "--oneline", "-n", "10"], cwd=curr_dir)

    if ok_log and log_out:
        lines = [line.strip() for line in log_out.splitlines() if line.strip()]
        commit_count = len(lines)
        semantic_prefixes = ("feat", "fix", "chore", "docs", "refactor", "style", "test")
        has_semantic = any(any(prefix in line.lower() for prefix in semantic_prefixes) for line in lines)

        if commit_count >= 2 and has_semantic:
            passed_checks += 1
            print(f"  {C_GREEN}[PASS]{C_RESET} Detected {commit_count} recent commits with conventional semantic prefixes.")
            print(f"    Latest: {lines[0]}\n")
        elif commit_count < 2:
            print(f"  {C_YELLOW}[WARN]{C_RESET} Only {commit_count} commit(s) detected. Please make atomic commits as you build.\n")
        else:
            print(f"  {C_YELLOW}[HINT]{C_RESET} Consider using conventional prefixes like 'feat:', 'chore:', or 'docs:'.\n")
            passed_checks += 1
    else:
        print(f"  {C_RED}[FAIL]{C_RESET} Could not inspect git log history.\n")

    # =========================================================================
    # CHECK 6: src/fetch_metadata.py Verification & Student Details
    # =========================================================================
    print(f"{C_BOLD}[Check 6/10] Metadata Script Implementation (src/fetch_metadata.py){C_RESET}")
    metadata_file = curr_dir / "src" / "fetch_metadata.py"

    if metadata_file.exists():
        try:
            with open(metadata_file, "r", encoding="utf-8") as f:
                code_content = f.read()

            # Syntax compilation check
            compile(code_content, str(metadata_file), "exec")

            # Check if student replaced the default USN placeholder
            is_placeholder_usn = "01FEXXXXXXXX" in code_content or "Your Full Name" in code_content

            if is_placeholder_usn:
                print(f"  {C_YELLOW}[ACTION REQUIRED]{C_RESET} Syntax is valid, but you still have placeholder values!")
                print("    Open `src/fetch_metadata.py` and replace `01FEXXXXXXXX` with your actual university USN.\n")
            else:
                passed_checks += 1
                ok_meta, meta_out, _ = run_cmd([sys.executable, str(metadata_file)], cwd=curr_dir)
                if ok_meta and "Python" in meta_out:
                    print(f"  {C_GREEN}[PASS]{C_RESET} Valid Python syntax and personal student USN confirmed.\n")
                else:
                    print(f"  {C_GREEN}[PASS]{C_RESET} File syntax compiled successfully.\n")
        except SyntaxError as se:
            print(f"  {C_RED}[FAIL]{C_RESET} Python Syntax Error in `src/fetch_metadata.py`: {se}\n")
    else:
        print(f"  {C_RED}[FAIL]{C_RESET} Missing file: src/fetch_metadata.py\n")

    # =========================================================================
    # PART 2: PYTHON FUNDAMENTALS PRACTICE (exercises.py)
    # =========================================================================
    print(f"\n{C_BOLD}{C_BLUE}--- Part 2: Python Fundamentals Practice Tasks ---{C_RESET}\n")

    exercises_file = curr_dir / "exercises.py"
    if not exercises_file.exists():
        print(f"  {C_RED}[FAIL] Missing exercises.py in week-01-git-engineering/{C_RESET}\n")
    else:
        # Import student implementations safely
        import importlib.util
        spec = importlib.util.spec_from_file_location("exercises", exercises_file)
        exercises = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(exercises)
        except Exception as import_err:
            print(f"  {C_RED}[FAIL] Syntax error importing exercises.py: {import_err}{C_RESET}\n")
            exercises = None

        # CHECK 7: Conditionals & try/except
        print(f"{C_BOLD}[Check 7/10] Conditionals & Defensive Input (Task 1){C_RESET}")
        if exercises and hasattr(exercises, "evaluate_attendance_status") and hasattr(exercises, "safe_parse_float"):
            try:
                fn_att = exercises.evaluate_attendance_status
                fn_parse = exercises.safe_parse_float
                assert fn_att(8, 10) == "ELIGIBLE", f"Expected 'ELIGIBLE', got {fn_att(8, 10)}"
                assert fn_att(7, 10) == "WARNING", f"Expected 'WARNING', got {fn_att(7, 10)}"
                assert fn_att(4, 10) == "SHORTAGE", f"Expected 'SHORTAGE', got {fn_att(4, 10)}"
                assert fn_att(0, 0) == "NO_SESSIONS", f"Expected 'NO_SESSIONS', got {fn_att(0, 0)}"
                assert fn_parse("92.5") == 92.5
                assert fn_parse("corrupted", default=-1.0) == -1.0
                passed_checks += 1
                print(f"  {C_GREEN}[PASS]{C_RESET} evaluate_attendance_status & safe_parse_float verified.\n")
            except Exception as exc:
                print(f"  {C_RED}[FAIL]{C_RESET} {exc}\n")
        else:
            print(f"  {C_RED}[FAIL]{C_RESET} Task 1 functions not found in exercises.py\n")

        # CHECK 8: Collections & Comprehensions
        print(f"{C_BOLD}[Check 8/10] Collections & List Comprehensions (Task 2){C_RESET}")
        if exercises and hasattr(exercises, "analyze_pod_scores"):
            try:
                sample = [
                    ("01FE25BCS122", "Parth's POD", 88.0),
                    ("01FE25BCS122", "Parth's POD", 88.0),
                    ("01FE26BCS027", "Parth's POD", 74.0),
                    ("01FE25BCI049", "Aditi's POD", 92.0),
                ]
                res = exercises.analyze_pod_scores(sample)
                assert res["unique_student_count"] == 3, f"Expected 3 unique USNs, got {res.get('unique_student_count')}"
                assert set(res["high_scorers"]) == {"01FE25BCS122", "01FE25BCI049"}, f"Unexpected high scorers: {res.get('high_scorers')}"
                assert res["pod_averages"]["Aditi's POD"] == 92.0
                passed_checks += 1
                print(f"  {C_GREEN}[PASS]{C_RESET} Set deduplication, dict grouping & comprehension verified.\n")
            except Exception as exc:
                print(f"  {C_RED}[FAIL]{C_RESET} {exc}\n")
        else:
            print(f"  {C_RED}[FAIL]{C_RESET} analyze_pod_scores not found in exercises.py\n")

        # CHECK 9: File I/O Pipeline (csv & json)
        print(f"{C_BOLD}[Check 9/10] File I/O Pipeline (Task 3){C_RESET}")
        if exercises and hasattr(exercises, "summarize_csv_to_json"):
            import tempfile
            import json
            csv_sample = curr_dir / "sample_cohort.csv"
            try:
                with tempfile.TemporaryDirectory() as tmpdir:
                    out_json = Path(tmpdir) / "summary.json"
                    summary = exercises.summarize_csv_to_json(str(csv_sample), str(out_json))
                    assert out_json.exists(), "Output JSON file was not created"
                    loaded = json.loads(out_json.read_text(encoding="utf-8"))
                    assert loaded["total_students"] == 5, f"Expected 5 students, got {loaded.get('total_students')}"
                    assert loaded["branches"] == ["BAR", "BCI", "BCS", "BMS"]
                    assert round(loaded["average_score"], 2) == 86.8
                passed_checks += 1
                print(f"  {C_GREEN}[PASS]{C_RESET} CSV parsing & JSON export verified.\n")
            except Exception as exc:
                print(f"  {C_RED}[FAIL]{C_RESET} {exc}\n")
        else:
            print(f"  {C_RED}[FAIL]{C_RESET} summarize_csv_to_json not found in exercises.py\n")

        # CHECK 10: OOP Mini-Model (StudentRecord)
        print(f"{C_BOLD}[Check 10/10] Object-Oriented Programming Class (Task 4){C_RESET}")
        if exercises and hasattr(exercises, "StudentRecord"):
            try:
                rec = exercises.StudentRecord("01fe25bcs122", "Garima")
                assert rec.usn == "01FE25BCS122", f"Expected uppercase USN, got {rec.usn}"
                assert rec.average() == 0.0
                rec.add_score(80.0)
                rec.add_score(90.0)
                assert rec.average() == 85.0
                assert rec.is_passing() is True
                passed_checks += 1
                print(f"  {C_GREEN}[PASS]{C_RESET} StudentRecord class methods & attributes verified.\n")
            except Exception as exc:
                print(f"  {C_RED}[FAIL]{C_RESET} {exc}\n")
        else:
            print(f"  {C_RED}[FAIL]{C_RESET} StudentRecord class not found in exercises.py\n")

    # =========================================================================
    # FINAL READINESS SUMMARY
    # =========================================================================
    print("=" * 64)
    pct = round((passed_checks / total_checks) * 100)
    if passed_checks == total_checks:
        print(f"{C_BOLD}{C_GREEN}[SUCCESS] ALL 10 CHECKS PASSED ({passed_checks}/{total_checks} -- 100%){C_RESET}")
        print(f"{C_GREEN}Your Week 1 Sprint is ready for submission on DSC Nexus!{C_RESET}")
        print("Steps:")
        print("  1. git add .")
        print("  2. git commit -m \"feat(week01): complete git and python challenges\"")
        print("  3. git push origin main")
        print("  4. Submit your GitHub link on DSC Nexus (https://dsc-nexus-app-production.up.railway.app)")
    else:
        print(f"{C_BOLD}{C_YELLOW}[ATTENTION] READINESS SCORE: {passed_checks}/{total_checks} ({pct}%){C_RESET}")
        print(f"{C_YELLOW}Review recommendations above. Solve pending tasks in exercises.py or git setup.{C_RESET}")
    print("=" * 64 + "\n")

    sys.exit(0 if passed_checks == total_checks else 1)

    sys.exit(0 if passed_checks == total_checks else 1)

if __name__ == "__main__":
    main()
