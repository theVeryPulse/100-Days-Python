from turtle import Turtle
import random

T_UNIT = 21    # the pixel size of each square of a turtle object


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('white')
        self.max_unit = 12
        rand_x = random.randint(-self.max_unit, self.max_unit) * T_UNIT
        rand_y = random.randint(-self.max_unit, self.max_unit) * T_UNIT
        self.goto(rand_x, rand_y)

    def refresh(self):
        """generate a new food on the map"""
        rand_x = random.randint(-self.max_unit, self.max_unit) * T_UNIT
        rand_y = random.randint(-self.max_unit, self.max_unit) * T_UNIT
        self.goto(rand_x, rand_y)