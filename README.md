# QuestionAnswerAgent

AI Interview Simulator — generates multiple-choice interview questions and saves a report.

## Quick setup

1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your API key to `.env` (do not commit this file):

```bash
echo "DEEPSEEK_API_KEY=your_key_here" > .env
```

## Run locally

```bash
python3 main.py -t "Machine Learning" -n 5
```

## Prepare and push to GitHub

```bash
# Initialize git (if not already)
git init
git add .
git commit -m "Initial project commit"
# Create a GitHub repo (using gh CLI) or create on the website
# With gh CLI:
# gh repo create my-repo --public --source=. --remote=origin --push
# Or add remote manually:
# git remote add origin https://github.com/<you>/<repo>.git
# git push -u origin main
```

Security: the repository contains an `.env` file with a DEEPSEEK_API_KEY; do NOT commit it. If you previously added secrets to a public repo, rotate the key immediately.
