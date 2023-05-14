from turtle import Turtle

FONT = ("Courier", 24, "normal")
SB_POSITION = (0, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(SB_POSITION)
        self.level = 1
        self.write(arg=F'Level {self.level}', move=False, align='center', font=FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.write(arg=F'Level {self.level}', move=False, align='center', font=FONT)