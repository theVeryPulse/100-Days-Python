from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 2
INITIAL_CARS = 10
INTERVAL = (-200, 220)
DENSITY = 0.05    # the smaller the value the fewer cars spawned
FACING_WEST = 180


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.initial_cars = INITIAL_CARS
        self.interval = INTERVAL

    def make_a_new_car(self, xcor, ycor):
        """Spawn a car at input coordinates, facing west (left)"""
        new_car = Turtle()
        new_car.penup()
        new_car.shape('square')
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(FACING_WEST)
        color = random.choice(COLORS)
        new_car.color(color)
        new_car.setpos(x=xcor, y=ycor)
        self.cars.append(new_car)

    def spawn_cars(self, window_width):
        reciprocal = int(1/DENSITY)
        if random.randint(1, reciprocal) <= reciprocal * DENSITY:
            x = int(window_width / 2) + 20
            y = random.randint(INTERVAL[0], INTERVAL[1])
            self.make_a_new_car(x, y)

    def cars_move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def next_level(self):
        self.car_speed += MOVE_INCREMENT

    def remove_outside_cars(self, window_width):
        for car in self.cars:
            if car.xcor() < - (window_width / 2) - 20:
                car.hideturtle()
                self.cars.remove(car)

    def car_number_check(self):
        print(F'total number of cars: {len(self.cars)}')

    def test_car(self):
        self.make_a_new_car(+300, -280)

