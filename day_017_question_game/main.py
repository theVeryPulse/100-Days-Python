from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Read in data to creat quiz list
question_bank = []
for question_dic in question_data:
    new_question = Question(question_dic["text"], question_dic["answer"])
    question_bank.append(new_question)
    print("hint: ", question_dic["text"], question_dic["answer"])

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()
