from turtle import Turtle, Screen
from snake import Snake
import time

def create_snake():
    snake = []
    for x in range(0, 3):
        x_pos = float(x * -20)
        body = Turtle("square")
        body.speed(2)
        body.color("white")
        body.penup()
        body.goto(x=x_pos, y=0)
        snake.append(body)

    return snake


def move_snake(snk):
    for segment_num in range(len(snk) - 1, 0, -1):
        new_x = snk[segment_num - 1].xcor()
        new_y = snk[segment_num - 1].ycor()
        snk[segment_num].goto(new_x, new_y)
    snk[0].forward(20)


# setup screen
wn = Screen()
wn.title("Snake Game")
wn.setup(width=600, height=600)
wn.bgcolor("black")
wn.tracer(0)

wn.onkey(lambda: snake[0].setheading(90), "Up")
wn.onkey(lambda: snake[0].setheading(180), "Left")
wn.onkey(lambda: snake[0].setheading(0), "Right")
wn.onkey(lambda: snake[0].setheading(270), "Down")

wn.listen()

# setup snake
snake = Snake()
wn.update()

# move snake
keep_moving = True
while keep_moving:
    wn.update()
    time.sleep(0.09)

    snake.move()

    if snake.snake[0].pos()[0] > 280:
        keep_moving = False

wn.exitonclick()

