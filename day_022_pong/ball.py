from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.bounced_this_frame = False
        self.BALL_SPEED = 3

    def serve(self):
        """Randomly set the initial angle of the ball within 45 degrees from the vertical"""
        direction = ['left', 'right']
        choice = random.choice(direction)
        angle = random.randint(0, 90)
        if choice == 'left':
            self.setheading(135 + angle)
        else:
            if angle <= 45:
                self.setheading(angle)
            else:
                self.setheading(angle + 270)
        print(F'seed angle: {angle}\n'
              F'direction: {choice}\n'
              F'initial angle: {self.heading()}')

    def move(self):
        self.forward(self.BALL_SPEED)

    def wall_bounce(self, height):
        """Change the angle of the ball to reflection angle"""
        if abs(self.ycor()) > (height/2 - 20):
            angle_in = self.heading()
            angle_out = 360 - angle_in
            self.setheading(angle_out)
            self.bounced_this_frame = True
            print(F'wall bounce, angle in {angle_in}, angle out: {angle_out}')

    def paddle_bounce(self, dis_paddle_center):
        """Change the angle of the ball to reflection angle"""
        angle_in = self.heading()
        # first calculate reflection angle
        if 0 < angle_in < 90 or 180 < angle_in < 270:
            angle_out = 180 - angle_in
        elif 90 < angle_in < 180 or 270 < angle_in < 360:
            angle_out = 540 - angle_in
        else:
            angle_out = angle_in
            print('angle_out = angle_in, something went wrong')
        # then add in edge factor, the closer to the edge of paddle, the greater the angle change
        if 90 < angle_out < 270:
            angle_out -= int((self.ycor() - dis_paddle_center))
        elif 0 < angle_out < 90 or 270 < angle_out < 360:
            angle_out += int((self.ycor() - dis_paddle_center))

        self.setheading(angle_out)
        self.bounced_this_frame = True
        print(F'paddle, bounce, angle in {angle_in}, angle out: {angle_out}')