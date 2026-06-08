from typing import TypedDict

class Question(TypedDict):
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: str
    explanation: str