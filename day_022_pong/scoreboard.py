from turtle import Turtle

SCORE_ALIGNMENT = 'center'
SCORE_FONT = ('Courier', 20, 'normal')
SCORE_COLOR = 'white'
SCORE_POS = (0, 265)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.penup()
        self.hideturtle()
        self.color(SCORE_COLOR)
        self.goto(SCORE_POS)
        self.write(F'{self.score_l} : {self.score_r}', move= False, align=SCORE_ALIGNMENT, font=SCORE_FONT)

    def gain_point_l(self):
        self.score_l += 1
        self.clear()
        self.write(F'{self.score_l} : {self.score_r}', move=False, align=SCORE_ALIGNMENT, font=SCORE_FONT)

    def gain_point_r(self):
        self.score_r += 1
        self.clear()
        self.write(F'{self.score_l} : {self.score_r}', move=False, align=SCORE_ALIGNMENT, font=SCORE_FONT)

