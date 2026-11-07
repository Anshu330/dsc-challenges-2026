# 🌿 Week 1 Sprint Challenge: Modern Git Engineering & DS Project Layout
> **Track**: Credit Track (2nd Year) & Growth Track (1st Year)  
> **Deadline**: Sunday, November 22, 2026 @ 11:59 PM IST  
> **Submission Platform**: DSC Nexus (`/modules` → Week 1)

---

## 🎯 Learning Objectives
1. Set up professional Git CLI configurations with your real name and KLE email.
2. Build an industry-standard Data Science project layout (`data/raw/`, `notebooks/`, `src/`).
3. Practice terminal branching: `main` → `feature/setup-eda` → PR merge.
4. Write semantic commit messages (`feat:`, `chore:`, `docs:`) and understand why messy commit logs hurt ML engineering teams.
5. Pass the automated self-grader `python verify_submission.py`.

---

## 📋 Hands-On Challenge Tasks

### Task 1: Terminal Identity Setup
Make sure your Git CLI is identified with your own name and university/personal email:
```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.usn@kletech.ac.in"
```

### Task 2: Build the Directory Layout
Ensure the following folder structure exists inside `week-01-git-engineering/`:
```
week-01-git-engineering/
├── README.md
├── verify_submission.py
├── .gitignore
├── data/
│   └── raw/
│       └── .gitkeep
├── notebooks/
│   └── .gitkeep
└── src/
    └── fetch_metadata.py
```
*(Tip: Empty folders are ignored by Git by default unless they contain a `.gitkeep` file!)*

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

### Task 5: Run the Auto-Grader Script
Run the built-in verification script from inside the `week-01-git-engineering/` directory:
```bash
python verify_submission.py
```
If any check fails, the script will tell you exactly what command to run or file to fix. Keep working until you achieve **6/6 checks passed**.

---

## 🚀 How to Submit on DSC Nexus
1. Push your local `main` branch to your GitHub fork:
   ```bash
   git push origin main
   ```
2. Copy your fork's GitHub repository link:  
   `https://github.com/<your-username>/dsc-challenges-2026`
3. Log into **DSC Nexus** (`http://localhost:5173`), open **My Challenges → Week 1**, paste your URL, and click **Submit Sprint Solution**.
4. Your assigned 3rd-year mentor will review your commit graph and evaluation rubric during the Monday 5:00 PM session in Audi 2.
