from turtle import Screen
from snake import Snake
from food import Food
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

wn.onkey(snake.snake_up, "Up")
wn.onkey(snake.snake_left, "Left")
wn.onkey(snake.snake_right, "Right")
wn.onkey(snake.snake_down, "Down")

# move snake
keep_moving = True
while keep_moving:
    wn.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        print("nomnomnom")

    if snake.head.pos()[0] > 290 or snake.head.pos()[0] < -290:
        keep_moving = False
    elif snake.head.pos()[1] > 290 or snake.head.pos()[1] < -290:
        keep_moving = False

wn.exitonclick()

