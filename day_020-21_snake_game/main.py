# This is a snake game, players can control snake with keyboard,
# Skills: OOP, class, Turtle,

from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# initialise the snake
snake = Snake()
snake.init_snake()

# bind key control to functions
screen.listen()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.right, 'Right')


screen.update()

game_on = True
counter = 0

while game_on:
    snake.move()
    screen.update()
    time.sleep(0.6)




screen.exitonclick()