from turtle import Turtle


class Wall(Turtle):
    def __init__(self):
        super().__init__()

    def init_wall(self, t_unit, wall_size):
        self.hideturtle()
        self.penup()
        self.goto(t_unit * wall_size, t_unit * wall_size)
        self.pendown()
        self.pencolor('white')
        self.setheading(180)
        for i in range(4):
            self.forward(2 * t_unit * wall_size)
            self.left(90)
