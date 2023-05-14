# this is a turtle crossing road game
# cars are randomly spawned on the right hand side and moves leftwards
# press 'Up' key to move turtle to finish line to win and enter next level
# when the turtle gets hit by car, the game ends
# skills: class inheritance, class, Turtle

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
GAME_SPEED = 0.01    # the smaller the value the quicker
CAR_HIT_BOX_LEN = 20
CAR_HIT_BOX_WID = 10
TURTLE_HIT_BOX_RAD = 10


def collision():
    """Detect collision between turtle and each car"""
    print(car_manager.cars)
    for car in car_manager.cars:
        print(F'car number: {car_manager.cars.index(car)}')
        x_distance = abs(car.xcor() - player.xcor())
        y_distance = abs(car.ycor() - player.ycor())
        print(F'x_distance: {x_distance}, y_distance: {y_distance}')
        if x_distance < CAR_HIT_BOX_LEN + TURTLE_HIT_BOX_RAD:
            if y_distance < CAR_HIT_BOX_WID + TURTLE_HIT_BOX_RAD:
                print('Collision!')
                return True
            else:
                print('no collision 1')
        else:
            print('no collision 2')
    return False


screen = Screen()
screen.setup(width=600, height=WINDOW_HEIGHT)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkeypress(player.move, 'Up')

scoreboard = Scoreboard()
car_manager = CarManager()

# generate a number of cars on map before game begins
for i in range(2000):
    car_manager.spawn_cars(WINDOW_WIDTH)
    car_manager.cars_move()
    car_manager.remove_outside_cars(WINDOW_WIDTH)

# main loop
game_is_on = True
while game_is_on:
    time.sleep(GAME_SPEED)
    car_manager.spawn_cars(WINDOW_WIDTH)
    car_manager.cars_move()
    # car_manager.car_number_check()    # monitor code
    car_manager.remove_outside_cars(WINDOW_WIDTH)
    screen.update()
    if player.reach_finish_line():
        car_manager.next_level()
        scoreboard.next_level()
        player.reset_turtle()
        time.sleep(1)
    if collision():
        game_is_on = False

screen.exitonclick()