from langchain_core.messages import HumanMessage
import json


def generate_question(llm, topic, previous_questions=None):
    previous_questions = previous_questions or []
    previous_section = ""
    if previous_questions:
        previous_section = (
            "Previous questions to avoid:\n"
            + "\n".join(f"- {q}" for q in previous_questions)
            + "\n\n"
        )

    prompt = f"""
Generate ONE unique multiple choice interview question for:

{topic}

{previous_section}
Ensure the question is not a repeat of any previous questions.
Use different phrasing, answer choices, and distractors each time.

Return ONLY valid JSON.

{{
    "question": "question text",
    "option_a": "option A",
    "option_b": "option B",
    "option_c": "option C",
    "option_d": "option D",
    "correct_answer": "A",
    "explanation": "short explanation"
}}
"""

    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    content = response.content.strip()

    # remove markdown if model adds it
    content = content.replace("```json", "")
    content = content.replace("```", "")

    return json.loads(content)
