from turtle import Turtle

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.length = 3    # the number of segments in the snake
        self.segments = []
        self.t_unit = 21    # the pixel size of each square of a turtle object
        self.step_speed = 0.6  # the interval between steps
        self.step = 0

    def init_snake(self):
        """Initialise a snake in the middle of window"""
        for i in range(self.length):
            new_seg = Turtle()
            new_seg.color('white')
            new_seg.shape('square')
            new_seg.penup()
            x_cor = -i * self.t_unit
            new_seg.setpos(x=x_cor, y=0)
            self.segments.append(new_seg)

    def move(self):
        """snake moves towards the direction of the head, the body follows"""

        goto_pos = self.segments[0].pos()
        print(F'the snake begins to move, step {self.step}')
        self.segments[0].forward(self.t_unit)
        for segment in self.segments[1:]:
            cur_pos = segment.pos()
            segment.goto(goto_pos)
            goto_pos = cur_pos
        print(F'the snake has moved, step {self.step}')
        self.step += 1

    def up(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(UP)
            print('the snake has turned')

    def down(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(DOWN)
            print('the snake has turned')

    def left(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(LEFT)
            print('the snake has turned')

    def right(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(RIGHT)
            print('the snake has turned')