from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_pos):
        super().__init__()
        self.goto(start_pos)
        self.setheading(90)
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.speed('fastest')
        self.STEP = 40

    def go_up(self):
        new_y = self.ycor() + self.STEP
        self.sety(new_y)

    def go_down(self):
        new_y = self.ycor() - self.STEP
        self.sety(new_y)
