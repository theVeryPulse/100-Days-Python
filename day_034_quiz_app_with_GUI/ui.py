from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    """Create a GUI"""
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quiz Time')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # score text
        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR, font=('Calibri', 20))
        self.score_label.grid(row=0, column=1)
        # question area
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            text='Quiz Time',# self.quiz.current_question.text,
            fill=THEME_COLOR,
            width=280,
            font=('Calibri', 20, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)
        # buttons
        false_img = PhotoImage(file='./images/false.png')
        true_img = PhotoImage(file='./images/true.png')
        self.false_bt = Button(image=true_img, highlightthickness=0, command=self.false_pressed)
        self.false_bt.grid(row=2, column=0)
        self.true_bt = Button(image=false_img, highlightthickness=0, command=self.true_pressed)
        self.true_bt.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f'You have finished all questions')
            self.true_bt.config(state='disabled')
            self.false_bt.config(state='disabled')


    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)