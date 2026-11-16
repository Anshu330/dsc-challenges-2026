# 🌿 Week 1 Sprint Challenge: Modern Git Engineering & Python Fundamentals
> **Track**: Credit Track (2nd Year) & Growth Track (1st Year)  
> **Deadline**: Sunday, November 22, 2026 @ 11:59 PM IST  
> **Submission Platform**: DSC Nexus (`/modules` → Week 1)

---

## 🎯 Learning Objectives
1. **Git CLI Mastery**: Configure your terminal identity, build an industry-standard Data Science project layout, and practice branching & conventional commits.
2. **Core Python Fundamentals**: Solidify control flow (`if`/`else`, `try`/`except`), collections (`set`, `dict`, list comprehensions), standard file I/O (`csv`, `json`), and object-oriented programming (`class`).
3. **Automated Verification**: Pass the automated local self-grader (`python verify_submission.py`) covering all 10 checks.

---

## 📁 Files in This Folder
```
week-01-git-engineering/
├── README.md               ← Complete challenge guide
├── verify_submission.py    ← Local automated self-grader (checks all 10 tasks)
├── exercises.py            ← Complete Python fundamentals tasks here
├── sample_cohort.csv       ← Sample dataset for Task 7 (File I/O)
├── .gitignore              ← Production gitignore rules
├── data/raw/.gitkeep       ← Raw dataset folder
├── notebooks/.gitkeep      ← Exploration notebooks
└── src/
    └── fetch_metadata.py   ← Environment diagnostic script
```

---

## 📋 Part 1: Git & GitHub Engineering Tasks

### Task 1: Terminal Identity Setup
Make sure your Git CLI is identified with your own name and university/personal email:
```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.usn@kletech.ac.in"
```

### Task 2: Build the Directory Layout
Ensure the following folders exist inside `week-01-git-engineering/`:
- `data/raw/`
- `notebooks/`
- `src/`

*(Tip: Empty folders are ignored by Git unless they contain a `.gitkeep` file!)*

### Task 3: Complete `src/fetch_metadata.py`
Open `src/fetch_metadata.py` and:
1. Fill in your `STUDENT_USN`, `STUDENT_NAME`, `BRANCH`, and `TRACK`.
2. Implement the `collect_environment_metadata()` function.
3. Run `python src/fetch_metadata.py` to verify it prints your JSON metadata correctly.

### Task 4: Terminal Branching & Atomic Commits
In industry, you never commit directly to production `main`.
1. Create and switch to a feature branch:
   ```bash
   git checkout -b feature/setup-eda
   ```
2. Stage and commit your changes in logical, atomic units using semantic commit prefixes:
   ```bash
   git add src/fetch_metadata.py
   git commit -m "feat(metadata): implement environment diagnostic script"
   ```
3. Switch back to `main` and merge your feature branch:
   ```bash
   git checkout main
   git merge feature/setup-eda
   ```

---

## 📋 Part 2: Python Fundamentals Practice (`exercises.py`)

Open `exercises.py` and implement the 4 core tasks:

### Task 5: Conditionals & Defensive Input (`try/except`)
- Implement `evaluate_attendance_status(attended, total)` returning `"ELIGIBLE"` ($\ge 75\%$), `"WARNING"` ($65\% \le \text{pct} < 75\%$), or `"SHORTAGE"` ($< 65\%$), handling `total <= 0` safely.
- Implement `safe_parse_float(raw_value, default=0.0)` using `try/except ValueError` so messy inputs do not crash your pipeline.

### Task 6: Collections & Comprehensions
- Implement `analyze_pod_scores(records)`:
  - Deduplicate USNs using a `set`.
  - Group pod averages with a `dict`.
  - Filter high scorers ($\ge 80$) using a **list comprehension**.

### Task 7: File I/O Pipeline (`with open`, `csv`, `json`)
- Implement `summarize_csv_to_json(csv_path, json_path)` using Python's built-in `csv.DictReader` and `json.dump` to read `sample_cohort.csv` and write summary statistics to JSON without external libraries.

### Task 8: Object-Oriented Programming (`class`)
- Complete the `StudentRecord` class with `__init__(self, usn, name)`, `add_score(self, score)` (validating $0 \le \text{score} \le 100$), `average(self)`, and `is_passing(self, threshold=50.0)`.

---

## ✅ Run the Auto-Grader Script
Run the built-in verification script from inside the `week-01-git-engineering/` directory:
```bash
python verify_submission.py
```
Keep working until you achieve **10/10 checks passed**!

---

## 🚀 How to Submit on DSC Nexus
1. Stage, commit, and push your local `main` branch to your GitHub fork:
   ```bash
   git add .
   git commit -m "feat(week01): complete git and python challenges"
   git push origin main
   ```
2. Copy your fork's GitHub repository link:  
   `https://github.com/<your-username>/dsc-challenges-2026`
3. Log into **DSC Nexus** ([dsc-nexus-app-production.up.railway.app](https://dsc-nexus-app-production.up.railway.app)), open **Challenges → Week 1**, paste your URL, and click **Submit sprint work**.
4. Your assigned pod mentor will review your submission and provide feedback.
