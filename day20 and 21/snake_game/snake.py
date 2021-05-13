from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for x in range(0, 3):
            x_pos = float(x * -20)
            self.add_segment(x_pos=x_pos)

    def add_segment(self,x_pos, y_pos=0):
        body = Turtle("square")
        body.color("white")
        body.penup()
        body.goto(x=x_pos, y=y_pos)
        self.snake.append(body)

    def extend(self):
        x = self.snake[-1].xcor()
        y = self.snake[-1].ycor()
        self.add_segment(x, y)

    def move(self):
        for segment_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment_num - 1].xcor()
            new_y = self.snake[segment_num - 1].ycor()
            self.snake[segment_num].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def snake_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
