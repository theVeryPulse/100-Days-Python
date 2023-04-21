# Purpose: practicing controlling the turtle using the keyboard

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def rotate_l():
    tim.left(10)


def rotate_r():
    tim.right(10)


def reset_screen():
    screen.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_l)
screen.onkey(key="d", fun=rotate_r)
screen.onkey(key='c', fun=reset_screen)
# screen.onkeypress(key="w", fun=move_forwards)
# screen.onkeypress(key="s", fun=move_backwards)
# screen.onkeypress(key="a", fun=rotate_l)
# screen.onkeypress(key="d", fun=rotate_r)

screen.exitonclick()
