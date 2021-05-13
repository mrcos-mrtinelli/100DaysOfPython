from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# setup screen
wn = Screen()
wn.title('Snake Game')
wn.setup(width=600, height=600)
wn.bgcolor("black")
wn.tracer(0)
wn.listen()

# setup snake
snake = Snake()
food = Food()
score = Scoreboard()


def game_off():
    global keep_moving
    keep_moving = False


wn.onkey(snake.snake_up, "Up")
wn.onkey(snake.snake_left, "Left")
wn.onkey(snake.snake_right, "Right")
wn.onkey(snake.snake_down, "Down")
wn.onkey(game_off, "q")

# move snake
keep_moving = True

while keep_moving:
    wn.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    for part in snake.snake[1:len(snake.snake) - 1]:
        if snake.head.distance(part) < 10:
            score.reset()
            snake.reset()

wn.exitonclick()

