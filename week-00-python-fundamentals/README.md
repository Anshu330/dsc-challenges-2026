# 🐍 Week 0 Prep Bootcamp: Python Fundamentals (Zero to Data-Ready)
> 📌 **Update**: Python Fundamentals has been merged with Git Engineering into **Week 1** (`week-01-git-engineering/`). You can work directly inside `week-01-git-engineering/` where `exercises.py` and `verify_submission.py` test all tasks!
> 
> **Track**: All Recruits New to Python (1st-Year Growth Track & 2nd-Year Credit Track)  
> **Target Window**: Complete before **Week 2 (NumPy)** on Monday, November 23, 2026  
> **Submission Platform**: DSC Nexus (`/modules` → Week 1)

---

## 🎯 Why Start Here?
Starting from scratch with Python? Welcome! Before jumping into NumPy vectorization and Pandas DataFrames, you need confident hands-on command over core Python:
1. **Variables, Types & Strings**: `int`, `float`, `str`, `bool`, casting, f-strings, slicing.
2. **Control Flow & Loops**: `if`/`elif`/`else`, `for` & `while` loops, `range()`, `enumerate()`, `zip()`.
3. **Collections & Comprehensions**: `list`, `tuple`, `set`, `dict` (`.get()`, `.items()`), and Pythonic comprehensions.
4. **Functions & Standard Modules**: `def`, default params, `*args`/`**kwargs`, `lambda`, `csv`, `json`.
5. **File I/O & Error Handling**: Reading/writing files safely with `with open(...)` and `try`/`except`.
6. **Intro OOP**: Classes, `__init__`, attributes, and methods — the foundation behind Pandas & Scikit-Learn APIs.

---

## 📋 Starter Files in This Folder
```
week-00-python-fundamentals/
├── README.md
├── exercises.py              ← Implement the 4 beginner tasks here
├── sample_cohort.csv         ← Input CSV for Task 3 (File I/O)
└── verify_python_basics.py   ← Local self-grader (checks all 4 tasks)
```

---

## 🛠️ Practice Tasks (`exercises.py`)

### Task 1: Conditionals & Defensive Input (`try/except`)
- Implement `evaluate_attendance_status(attended, total)` returning `"ELIGIBLE"` ($\ge 75\%$), `"WARNING"` ($65\% \le \text{pct} < 75\%$), or `"SHORTAGE"` ($< 65\%$), handling `total <= 0` safely.
- Implement `safe_parse_float(raw_value, default=0.0)` using `try/except ValueError` so malformed text never crashes your pipeline.

### Task 2: Lists, Sets, Dicts & Comprehensions
- Implement `analyze_pod_scores(records)` given a list of `(usn, pod_name, score)` tuples:
  - Deduplicate USNs using a `set`.
  - Filter top scores ($\ge 80$) using a **list comprehension**.
  - Group average score per pod using a dictionary (`dict`).

### Task 3: File I/O Pipeline (`with open`, `csv`, `json`)
- Implement `summarize_csv_to_json(csv_path, json_path)` using Python's built-in `csv` and `json` modules (do not use Pandas here yet!) to read `sample_cohort.csv` and write total student count, unique branches, and average score to JSON.

### Task 4: Intro Object-Oriented Programming (`class`)
- Complete the `StudentRecord` class with `__init__(self, usn, name)`, `add_score(self, score)`, `average(self)`, and `is_passing(self, threshold=50.0)`.

---

## ✅ Verify Locally
Run inside `week-00-python-fundamentals/`:
```bash
python verify_python_basics.py
```
Once all checks pass, push your fork and submit your repository link (or Google Colab notebook link) under **Week 0 • Prep** on DSC Nexus!
