from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.color("white")
        self.x_direction = 10
        self.y_direction = 10
        self.move_speed = 0.1

    def move(self):
        x_cor = self.xcor() + self.x_direction
        y_cor = self.ycor() + self.y_direction

        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.y_direction *= -1

    def bounce_x(self):
        self.x_direction *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()
