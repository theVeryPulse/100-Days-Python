from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

GAME_SPEED = 0.01    # the smaller the value the quicker
# default screen size
HEIGHT = 600
WIDTH = 800
# paddle size
PADDLE_HIT_BOX_HALF_WIDTH = 5
PADDLE_HIT_BOX_HALF_LENGTH = 50
# paddle start position
START_POSITION_R = (350, 0)
START_POSITION_L = (-350, 0)

# initialise the window
screen = Screen()
screen.bgcolor('black')
screen.setup(width=WIDTH, height=HEIGHT)
screen.title('PONG')
screen.listen()
screen.tracer(0)

# initialise the paddles
paddle_r = Paddle(START_POSITION_R)
paddle_l = Paddle(START_POSITION_L)
screen.onkeypress(paddle_l.go_up, 'w')
screen.onkeypress(paddle_l.go_down, 's')
screen.onkeypress(paddle_r.go_up, 'Up')
screen.onkeypress(paddle_r.go_down, 'Down')

scoreboard = Scoreboard()
ball = Ball()

while True:
    ball.setposition(0, 0)
    ball.serve()
    keep_hit_wall = 0    # to avoid ball keep hitting the wall
    last_paddle_bounce = 0
    screen.update()
    time.sleep(1)    # a short pause before ball is served

    while True:
        ball.bounced_this_frame = False
        ball.move()
        screen.update()

        # check if ball hits wall
        if abs(ball.ycor()) > (HEIGHT/2 - 10):
            ball.wall_bounce(HEIGHT)
            keep_hit_wall += 1

        if last_paddle_bounce > 30:    # check for reasonable interval between paddle bounces
            # check if ball hits the right paddle
            if (START_POSITION_R[0] + PADDLE_HIT_BOX_HALF_WIDTH) > ball.xcor() > \
                    (START_POSITION_R[0] - PADDLE_HIT_BOX_HALF_WIDTH):
                if abs(ball.ycor() - paddle_r.ycor()) <= PADDLE_HIT_BOX_HALF_LENGTH:
                    ball.paddle_bounce(paddle_r.ycor())
                    last_paddle_bounce = 0
                    keep_hit_wall = 0

            # check if ball hits the left paddle
            if (START_POSITION_L[0] - PADDLE_HIT_BOX_HALF_WIDTH) < ball.xcor() < \
                    (START_POSITION_L[0] + PADDLE_HIT_BOX_HALF_WIDTH):
                if abs(ball.ycor() - paddle_l.ycor()) <= PADDLE_HIT_BOX_HALF_LENGTH:
                    ball.paddle_bounce(paddle_l.ycor())
                    last_paddle_bounce = 0
                    keep_hit_wall = 0
        else:    # not triggering paddle bounce
            last_paddle_bounce += 1

        # ball hits baseline
        if ball.xcor() > (WIDTH / 2):
            scoreboard.gain_point_l()
            break
        if ball.xcor() < -(WIDTH / 2):
            scoreboard.gain_point_r()
            break

        # if ball keeps hitting the wall, reset the ball
        if keep_hit_wall > 10:
            break

        time.sleep(GAME_SPEED)