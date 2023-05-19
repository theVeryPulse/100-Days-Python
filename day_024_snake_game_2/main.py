# This is the updated version of the previous snake game,
# it can now record the high score of all games
# skills: read/write file, class inheritance, class, Turtle,

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from wall import Wall

# initialise the window
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# initialise the snake
snake = Snake()
snake.init_snake()
# snake.head = snake.segments[0]
screen.update()

# bind key control to functions
screen.listen()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.right, 'Right')

# basic unit by pixels
T_UNIT = 21

# initialise the boundaries
WALL_SIZE = 13
wall = Wall()
wall.init_wall(t_unit=T_UNIT, wall_size=WALL_SIZE)

# initialise elements
food = Food()
scoreboard = Scoreboard()
bound = T_UNIT * (WALL_SIZE - 1)

# read from save file the high score
save_file_location = './save_file.txt'
with open(save_file_location, 'r') as file:
    content = file.read()
try:
    historic_high_score = int(content)
    scoreboard.high_score = historic_high_score
    print(F'high score: {scoreboard.high_score}')
except Exception as E:
    print(F'high score load error: {E}')
    historic_high_score = 0
else:
    print(F'historic high score loaded from {save_file_location}')

# main loop
while snake.is_alive:
    snake.move()
    # for segment in snake.segments:    # movement trace
    #     print(F"{segment.pos()}")
    scoreboard.refresh()
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

    # 1 check game over
    # 1.1 check collision with wall
    if snake.head.xcor() > bound or snake.head.ycor() > bound or \
            snake.head.xcor() < -bound or snake.head.ycor() < -bound:
        print('Hit the wall')
        snake.is_alive = False
    # 1.2 check if snake bites itself
    for i in range(1, len(snake.segments)):
        if snake.head.distance(snake.segments[i]) < 5:
            print(F'bite itself (segment {i})')
            snake.is_alive = False
    # 2 show score and reset
    if not snake.is_alive:
        # 2.1 display score
        scoreboard.game_over()
        screen.update()
        # 2.2 reset scoreboard
        scoreboard.restart()
        screen.update()
        # 2.3 reset snake and food
        snake.restart()
        snake.init_snake()
        food.refresh()
        snake.is_alive = True
        # 2.4 update alltime high score
        if scoreboard.high_score > historic_high_score:
            with open('save_file.txt', 'w') as file:
                file.write(F'{scoreboard.high_score}')
            print('new high score recorded')



screen.exitonclick()
file.close()