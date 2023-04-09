# Purpose: create a question in the form of object
class Question:
    def __init__(self, q_text: str, q_answer: str):
        self.text = q_text
        self.answer = q_answer.lower()
