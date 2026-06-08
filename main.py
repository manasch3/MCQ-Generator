from dotenv import load_dotenv
load_dotenv()

import argparse
import os
import sys
from datetime import datetime

from langchain.chat_models import init_chat_model

from nodes.question_generator import generate_question


llm = init_chat_model(
    "deepseek-chat",
    model_provider="deepseek",
    temperature=0.7
)

SUPPORTS_COLOR = sys.stdout.isatty()

RESET = "\033[0m" if SUPPORTS_COLOR else ""
BOLD = "\033[1m" if SUPPORTS_COLOR else ""
CYAN = "\033[96m" if SUPPORTS_COLOR else ""
GREEN = "\033[92m" if SUPPORTS_COLOR else ""
YELLOW = "\033[93m" if SUPPORTS_COLOR else ""
RED = "\033[91m" if SUPPORTS_COLOR else ""
WHITE = "\033[97m" if SUPPORTS_COLOR else ""


def style(text, color=""):
    return f"{color}{text}{RESET}" if SUPPORTS_COLOR else text


def print_line(char="=", width=60):
    print(style(char * width, CYAN))


def print_header(title, subtitle=None):
    print_line("=", 60)
    print(style(f"{title}", BOLD + CYAN))
    if subtitle:
        print(style(subtitle, WHITE))
    print_line("=", 60)


def print_section(title):
    print(style(f"\n{title}", BOLD + YELLOW))
    print(style("-" * len(title), YELLOW))


def print_warning(message):
    print(style(message, YELLOW))


def print_error(message):
    print(style(message, RED))


def print_success(message):
    print(style(message, GREEN))


def parse_args():
    parser = argparse.ArgumentParser(
        description="AI Interview Simulator CLI"
    )
    parser.add_argument(
        "-t",
        "--topic",
        help="Interview topic or domain",
        type=str,
    )
    parser.add_argument(
        "-n",
        "--questions",
        help="Number of questions to ask",
        type=int,
        default=5,
    )
    parser.add_argument(
        "--no-report",
        help="Do not save the interview report",
        action="store_true",
    )
    parser.add_argument(
        "--report-dir",
        help="Directory where reports are saved",
        default="reports",
    )
    return parser.parse_args()


def prompt_topic():
    topic = input(style("\nInterview Type: ", BOLD)).strip()
    while not topic:
        print_error("Topic cannot be empty.")
        topic = input(style("Interview Type: ", BOLD)).strip()
    return topic


def prompt_answer():
    valid_choices = {"A", "B", "C", "D"}
    while True:
        answer = input(style("\nChoose A/B/C/D: ", BOLD)).strip().upper()
        if answer in valid_choices:
            return answer
        print_warning("Invalid choice. Please enter A, B, C or D.")


def get_performance_label(percentage):
    if percentage >= 80:
        return "Excellent"
    if percentage >= 60:
        return "Good"
    return "Needs Improvement"


def save_report(topic, score, total_questions, question_history, report_dir="reports"):
    os.makedirs(report_dir, exist_ok=True)
    filename = os.path.join(
        report_dir,
        f"{topic.replace(' ', '_')}_report.md",
    )
    percentage = (score / total_questions) * 100

    with open(filename, "w", encoding="utf-8") as f:
        f.write("# Interview Report\n\n")
        f.write(f"**Domain:** {topic}\n\n")
        f.write(f"**Score:** {score}/{total_questions}\n\n")
        f.write(f"**Percentage:** {percentage:.2f}%\n\n")
        f.write(f"**Generated:** {datetime.now()}\n\n")
        f.write("---\n\n")

        for i, q in enumerate(question_history, start=1):
            f.write(f"## Question {i}\n\n")
            f.write(f"{q['question']}\n\n")
            f.write(f"Your Answer: {q['user_answer']}\n\n")
            f.write(f"Correct Answer: {q['correct_answer']}\n\n")
            f.write(f"Explanation: {q['explanation']}\n\n")
            f.write("---\n\n")

    return filename


def run_interview(topic, total_questions, report_dir, save_report_flag):
    print_line()
    print("AI INTERVIEW SIMULATOR")
    print_line()

    effective_topic = topic or prompt_topic()
    score = 0
    question_history = []

    print_header(
        "AI INTERVIEW SIMULATOR",
        subtitle=f"Topic: {effective_topic} | Questions: {total_questions}",
    )

    seen_questions = set()

    for q_num in range(1, total_questions + 1):
        print_section(f"Question {q_num}/{total_questions}")

        question = None
        question_text = None
        for attempt in range(1, 21):
            candidate = generate_question(
                llm,
                effective_topic,
                previous_questions=list(seen_questions),
            )
            question_text = candidate["question"].strip()
            if question_text and question_text not in seen_questions:
                question = candidate
                seen_questions.add(question_text)
                break
            print_warning("Duplicate question detected, generating a new one...")

        if question is None:
            question = candidate
            print_warning("Using last generated question after multiple attempts.")

        print(style(question["question"], BOLD))
        print(style(f"\nA. {question['option_a']}", WHITE))
        print(style(f"B. {question['option_b']}", WHITE))
        print(style(f"C. {question['option_c']}", WHITE))
        print(style(f"D. {question['option_d']}", WHITE))

        user_answer = prompt_answer()
        correct_answer = question["correct_answer"].strip().upper()

        if user_answer == correct_answer:
            print_success("\n✅ Correct!")
            score += 1
        else:
            print_error("\n❌ Incorrect!")
            print(style(f"Correct Answer: {correct_answer}", YELLOW))

        print(style("\nExplanation:", BOLD))
        print(style(question["explanation"], WHITE))

        question_history.append(
            {
                "question": question["question"],
                "user_answer": user_answer,
                "correct_answer": correct_answer,
                "explanation": question["explanation"],
            }
        )

    percentage = (score / total_questions) * 100
    print_header("FINAL REPORT")
    print(style(f"Topic: {effective_topic}", WHITE))
    print(style(f"Score: {score}/{total_questions}", WHITE))
    print(style(f"Percentage: {percentage:.2f}%", WHITE))
    print(style(f"Performance: {get_performance_label(percentage)}", BOLD + GREEN if percentage >= 60 else BOLD + YELLOW))

    if save_report_flag:
        report_path = save_report(
            effective_topic,
            score,
            total_questions,
            question_history,
            report_dir,
        )
        print_success(f"\nReport Saved: {report_path}")
    else:
        print_warning("\nReport saving skipped.")

    print_line()


def main():
    args = parse_args()
    run_interview(
        topic=args.topic,
        total_questions=args.questions,
        report_dir=args.report_dir,
        save_report_flag=not args.no_report,
    )


if __name__ == "__main__":
    main()
