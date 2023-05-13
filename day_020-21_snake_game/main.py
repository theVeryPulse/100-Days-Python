# This is a snake game, players can control snake with keyboard,
# skills: class inheritance, class, Turtle,

from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# initialise the window
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# initialise the snake
snake = Snake()
snake.init_snake()
snake.head = snake.segments[0]
screen.update()

# bind key control to functions
screen.listen()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.right, 'Right')

# initialise the boundaries
wall = Turtle()
T_UNIT = 21
WALL_SIZE = 13
wall.hideturtle()
wall.penup()
wall.goto(T_UNIT * WALL_SIZE, T_UNIT * WALL_SIZE)
wall.pendown()
wall.pencolor('white')
wall.setheading(180)
for i in range(4):
    wall.forward(2 * T_UNIT * WALL_SIZE)
    wall.left(90)

# initialise elements
food = Food()
scoreboard = Scoreboard()
bound = T_UNIT * (WALL_SIZE - 1)

# main loop
while snake.is_alive:
    snake.move()
    screen.update()

    # when snake eats food
    if snake.head.distance(food) < 18:
        print('Food in mouth!')
        snake.grow()
        scoreboard.gain_point()
        scoreboard.refresh()
        for segment in snake.segments:
            if segment.distance(food) < 18:
                food.refresh()

    # check collision with wall
    if snake.head.xcor() > bound or snake.head.ycor() > bound or \
            snake.head.xcor() < -bound or snake.head.ycor() < -bound:
        print('Hit the wall')
        snake.is_alive = False
        scoreboard.game_over()

    # check if snake bites itself
    for i in range(1, len(snake.segments)):
        if abs(snake.head.xcor() - snake.segments[i].xcor()) < 5 and \
                abs(snake.head.ycor() - snake.segments[i].ycor()) < 5:
            print(F'bite itself (segment {i})')
            snake.is_alive = False
            scoreboard.game_over()
        # else:
            # print(F'not biting segment {i}')
            # print(F'Head: {snake.head.xcor()}, {snake.head.ycor()}')
            # print(F'Segment {i}: {snake.segments[i].xcor()},{snake.segments[i].ycor()}')

screen.exitonclick()