
from turtle import Turtle, Screen
import random


def turtle_absolute_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    RGB_tuple = (r, g, b)
    the_turtle.color(RGB_tuple)
    # return RGB_output


def turtle_random_direction():
    turn = random.randint(0, 3)
    if turn == 3:
        the_turtle.left(90)
    else:
        the_turtle.right(turn*90)


screen = Screen()
screen.colormode(255)

the_turtle = Turtle()
the_turtle.shape('turtle')
the_turtle.color('teal')
the_turtle.pensize(10)
the_turtle.speed(0)

# Draw dash line:
# for i in range (20):
#     the_turtle.forward(10)
#     the_turtle.penup()
#     the_turtle.forward(10)
#     the_turtle.pendown()

# N-sided polygon with random colours
# n_sided = 20
# for i in range(3, n_sided+1):
#     turtle_random_color()
#     for j in range(i):
#         the_turtle.forward(40)
#         angle = 360 / i
#         the_turtle.right(angle)

# Random walk:
total_steps = 1000
for i in range(total_steps+1):
    turtle_absolute_random_color()
    turtle_random_direction()
    the_turtle.forward(20)

# Spirograph
# degree_diff = 23
# for i in range(1000):
#     turtle_random_color()
#     the_turtle.circle(200)
#     the_turtle.right(degree_diff)



screen.exitonclick()