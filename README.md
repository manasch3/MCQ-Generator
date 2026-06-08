# MCQ Generator

An AI-powered interview simulator that generates domain-specific multiple-choice questions, evaluates answers, and produces detailed performance reports using LangChain and DeepSeek.

## Overview

MCQ Generator automates the interview preparation workflow:
- generate contextual multiple-choice questions for any domain,
- provide immediate feedback and explanations,
- track performance metrics,
- export results as polished Markdown reports.

It is ideal for self-assessment, interview prep, and knowledge verification across various technical and non-technical topics.

## Features

- AI-powered question generation tailored to specific domains
- Automatic duplicate-question detection and prevention
- Real-time scoring and performance tracking
- Detailed explanations for each answer
- Export reports as Markdown with timestamps and metrics
- Professional terminal UI with color-coded feedback
- CLI support for non-interactive workflows

## Tech Stack

- Python 3.10+
- LangChain
- LangChain DeepSeek
- Python Dotenv
- Argparse (standard library)

## Project Structure

```text
MCQ-Generator/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── state.py
├── nodes/
│   └── question_generator.py
├── reports/
└── venv/  # local virtual environment, should be ignored
```

## How it Works

1. `main.py` prompts for an interview topic (or accepts via `--topic` flag).
2. The question generator node creates unique multiple-choice questions using the LLM.
3. The user answers each question with A/B/C/D feedback.
4. The system scores answers and provides explanations in real-time.
5. A final report is saved to `reports/<topic>_report.md` with score and performance level.

## Detailed Workflow

- `nodes/question_generator.py` calls DeepSeek to generate unique questions per topic, avoiding duplicates via prompt context.
- `main.py` orchestrates the interview loop, collecting user answers and maintaining session statistics.
- `state.py` defines the Question TypedDict for structured question data.
- Reports capture all questions, user answers, correct answers, and explanations in Markdown format.

## Prerequisites

- Python 3.10+ or compatible Python 3.x
- A valid DeepSeek API key

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/manasch3/MCQ-Generator.git
cd MCQ-Generator
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

Activate it:

**macOS/Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file from `.env.example`:

```bash
cp .env.example .env
```

Then fill in your API key:

```env
DEEPSEEK_API_KEY=your_deepseek_api_key_here
```

### 5. Run the application

**Interactive mode (prompts for topic):**

```bash
python main.py
```

**Non-interactive mode (with CLI flags):**

```bash
python main.py --topic "Machine Learning" --questions 10
```

**Skip report generation:**

```bash
python main.py --topic "Data Science" --no-report
```

## CLI Options

```
python main.py [OPTIONS]

OPTIONS:
  -t, --topic TEXT          Interview topic or domain (optional; prompted if not provided)
  -n, --questions INT       Number of questions to ask (default: 5)
  --no-report               Do not save the interview report
  --report-dir DIR          Directory where reports are saved (default: reports)
```

## Example

**Terminal session:**

```bash
$ python main.py -t "Deep Learning" -n 3
============================================================
AI INTERVIEW SIMULATOR
Topic: Deep Learning | Questions: 3
============================================================

Question 1/3
What is the primary purpose of an activation function in a neural network?

A. To introduce non-linearity into the model
B. To reduce the number of parameters
C. To normalize input data
D. To initialize weights

Choose A/B/C/D: a

✅ Correct!

Explanation:
Activation functions like ReLU or sigmoid enable neural networks to learn
complex patterns by introducing non-linear transformations.

[... more questions ...]

============================================================
FINAL REPORT

Topic: Deep Learning
Score: 3/3
Percentage: 100.00%
Performance: Excellent

Report Saved: reports/Deep_Learning_report.md
============================================================
```

## Report Output

Reports are saved as Markdown with sections including:
- Domain and timestamp
- Final score and percentage
- Performance level (Excellent/Good/Needs Improvement)
- All questions with user answers, correct answers, and explanations
- Formatted for easy sharing and review

Example report excerpt:

```markdown
# Interview Report

**Domain:** Deep Learning
**Score:** 3/3
**Percentage:** 100.00%
**Generated:** 2026-06-08 14:32:15.123456

---

## Question 1

What is the primary purpose of an activation function...

Your Answer: A
Correct Answer: A
Explanation: Activation functions like ReLU or sigmoid...

---
```

## Troubleshooting

- **"Command not found: python"**: Use `python3` instead.
- **ImportError for langchain**: Verify `pip install -r requirements.txt` completed successfully.
- **API key errors**: Confirm `.env` contains a valid `DEEPSEEK_API_KEY`.
- **Duplicate questions appearing**: Restart the session; the duplicate detector resets per interview.
- **Color output not showing**: Terminal may not support ANSI colors; output will still work in plain text.

## Notes

- Do not commit `.env` or API keys to GitHub.
- The `reports/` folder is ignored by `.gitignore` because it contains generated outputs.
- Each interview session tracks seen questions to prevent repetition within that session.
- Reports are always appended to the `reports/` directory; older reports are not overwritten automatically.

## License

This project is intended for educational, research, and interview preparation purposes.
