import time
import turtle
from turtle import Turtle, Screen
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball

turtle.tracer(0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.listen()


scoreboard = ScoreBoard()
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-378, 0))
ball = Ball()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")



is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -279:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 345 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    if ball.xcor() > 372:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -388:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()