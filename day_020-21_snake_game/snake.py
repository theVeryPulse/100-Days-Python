from turtle import Turtle
import time

# turning angles used for tutle.heading()
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

# the pixel size of each square of a turtle object
T_UNIT = 21

# initial number of segments of the snake
INIT_LEN = 10
STEP_SPEED = 0.1


class Snake:
    def __init__(self):
        self.length = INIT_LEN    # the number of segments in the snake
        self.segments = []
        self.step_speed = STEP_SPEED  # the interval between steps
        self.is_alive = True

    def init_snake(self):
        """Initialise a snake in the middle of window"""
        for i in range(self.length):
            new_seg = Turtle()
            new_seg.color('white')
            new_seg.shape('square')
            new_seg.penup()
            x_cor = int(-i * T_UNIT)
            new_seg.setpos(x=x_cor, y=0)
            self.segments.append(new_seg)

    def move(self):
        """snake moves towards the direction of the head, the body follows"""
        goto_pos = self.segments[0].pos()
        self.segments[0].forward(T_UNIT)
        for segment in self.segments[1:]:
            cur_pos = segment.pos()
            segment.goto(goto_pos)
            goto_pos = cur_pos
        time.sleep(STEP_SPEED)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def grow(self):
        """add a new segments at the tail"""
        new_seg = Turtle()
        new_seg.color('white')
        new_seg.shape('square')
        new_seg.penup()
        cor= self.segments[-1].pos()
        new_seg.setpos(cor)
        self.segments.append(new_seg)


