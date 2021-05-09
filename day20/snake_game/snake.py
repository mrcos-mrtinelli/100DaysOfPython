from turtle import Turtle


class Snake:
    snake = []

    for x in range(0, 3):
        x_pos = float(x * -20)
        body = Turtle("square")
        body.speed(2)
        body.color("white")
        body.penup()
        body.goto(x=x_pos, y=0)
        snake.append(body)

    def move(self):
        snake = self.snake
        for segment_num in range(len(snake) - 1, 0, -1):
            new_x = snake[segment_num - 1].xcor()
            new_y = snake[segment_num - 1].ycor()
            snake[segment_num].goto(new_x, new_y)
        snake[0].forward(20)
