from turtle import Turtle
import time

# the pixel size of each square of a turtle object
T_UNIT = 21

# live score info
ALIGNMENT = 'center'
FONT = ('Courier', 14, 'normal')
Y_LOCATION = 13

# game over info
GAME_OVER_FONT = ('Courier', 30, 'bold')
GAME_OVER_SCORE_POS = (-50, -50)
GAME_OVER_SCORE_FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.header_pos = (0, Y_LOCATION * T_UNIT)
        self.goto(self.header_pos)
        self.score = 0
        self.high_score = 0
        self.write(arg=F"SCORE: {self.score}  HIGH SCORE: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def gain_point(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score

    def refresh(self):
        self.clear()
        self.write(arg=F"SCORE: {self.score}  HIGH SCORE: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.color('white')
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=GAME_OVER_FONT)
        self.goto(GAME_OVER_SCORE_POS)
        self.write(F"SCORE: {self.score}\nHIGH SCORE: {self.high_score}", move=False, align=ALIGNMENT, font=GAME_OVER_SCORE_FONT)

    def restart(self):
        time.sleep(3)
        self.clear()
        self.score = 0
        self.goto(self.header_pos)
        self.write(arg=F"SCORE: {self.score}  HIGH SCORE: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
