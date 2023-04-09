# The main class of the game process
class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank   # A list of objects
        self.score = 0

    # Ask the current question, check the answer, prepare the next question
    def next_question(self):
        current_question = self.question_list[self.question_number]    # Current question object
        self.question_number += 1
        if input(F"Q.{self.question_number}: {current_question.text} True of false?\n").lower() \
                == current_question.answer:
            self.score += 1
            print(F"You are right! Score: {self.score}/{self.question_number}")
        else:
            print(F"You are wrong. Score: {self.score}/{self.question_number}")

    # Check if there are more questions
    def still_has_question(self):
        if self.question_number < len(self.question_list):
            # print("There are more questions")
            return True
        else:
            print("There are no more questions!\n"
                  F"Your final score: {self.score}/{len(self.question_list)+1}")
            return False
