from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 5
FINISH_LINE_Y = 280
FACING_NORTH = 90



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(FACING_NORTH)
        self.setpos(STARTING_POSITION)
        self.shape('turtle')

    def move(self):
        """move the turtle upwards, return True when reaching finish line"""
        self.forward(MOVE_DISTANCE)

    def reach_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True

    def reset_turtle(self):
        self.hideturtle()
        self.setpos(STARTING_POSITION)
        self.showturtle()




