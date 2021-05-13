import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

game_is_on = True

screen = Screen()
screen.title("Pong!")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

score = Score()
left_paddle = Paddle("left")
right_paddle = Paddle("right")
ball = Ball()


screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # right_paddle.auto_move()
    # if right_paddle.ycor() > 250 or right_paddle.ycor() < -240:
    #     right_paddle.reverse()

    # ball passes right_paddle
    if ball.xcor() > 390:
        score.left_point()
        ball.reset()

    # ball passes left_paddle
    if ball.xcor() < -400:
        score.right_point()
        ball.reset()

    # ball bounces off paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # ball bounce off top
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

screen.exitonclick()
