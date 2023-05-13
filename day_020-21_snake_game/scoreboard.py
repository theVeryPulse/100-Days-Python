from turtle import Turtle

# the pixel size of each square of a turtle object
T_UNIT = 21

# live score info
ALIGNMENT = 'center'
FONT = ('Courier', 14, 'normal')
Y_LOCATION = 13

# game over info
GAME_OVER_FONT = ('Courier', 30, 'bold')
YOUR_SCORE_POS = (-50, -50)
YOUR_SCORE_FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(x=0, y=Y_LOCATION * T_UNIT)

        self.score = 0
        self.write(arg=F"SCORE: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def gain_point(self):
        self.score += 1

    def refresh(self):
        self.clear()
        self.write(arg=F"SCORE: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=GAME_OVER_FONT)
        self.goto(YOUR_SCORE_POS)
        self.write("YOUR SCORE: {}".format(self.score), move=False, align=ALIGNMENT, font=YOUR_SCORE_FONT)