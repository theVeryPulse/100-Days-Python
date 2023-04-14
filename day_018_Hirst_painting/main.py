# Purpose: generate a dot painting based on the color of a chosen picture

import colorgram
import turtle as t
import random


# Generate random colors out of all possible RGBs
def turtle_absolute_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    RGB_tuple = (r, g, b)
    the_turtle.color(RGB_tuple)


def turtle_random_color():
    random_color = random.choice(color_set)
    the_turtle.color(random_color)


def draw_dot_painting(row_num: int, col_num: int, dot_rad, center_distance):
    """Draw an array of dots of random colors"""
    y_coord = 0
    for row in range(row_num):
        for column in range(col_num):
            turtle_random_color()
            turtle_absolute_random_color()    # Use completely random colors instead
            the_turtle.dot(dot_rad)
            the_turtle.forward(center_distance)

        y_coord += center_distance
        the_turtle.setpos(x=0, y=y_coord)


# Extract 6 colors from an image.
colors = colorgram.extract('dot painting.jpg', 6)
print(colors)

# Save color RGB as tuples in a list
color_set = []
for color in colors:
    color_set.append((color.rgb.r, color.rgb.g, color.rgb.b))

the_turtle = t.Turtle()
the_turtle.penup()
screen = t.Screen()
screen.colormode(255)

# Determine the parameters
dot_radius = 20
dot_center_distance = 50
rows = 10
columns = 10

# Draw the dot painting
draw_dot_painting(rows, columns, dot_radius, dot_center_distance)

screen.exitonclick()

