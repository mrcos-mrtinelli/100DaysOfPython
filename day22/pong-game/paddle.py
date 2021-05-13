from turtle import Turtle

POSITION = {
    "left": -360,
    "right": 350,
    "offset": 20
}
SCREEN_LIMITS = {
    "top": 250,
    "bottom": -250
}
PADDLE_STRETCH = {
    "width": 5,
    "len": 1
}
SPEED = 25


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        # self.paddle = Turtle()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_STRETCH["width"], stretch_len=PADDLE_STRETCH["len"])
        self.color("white")
        self.goto(POSITION[position], 0)
        self.y_direction = 20

    def move_up(self):
        if self.ycor() < SCREEN_LIMITS["top"]:
            y_cor = self.ycor() + SPEED
            x_cor = self.xcor()
            self.goto(x_cor, y_cor)

    def move_down(self):
        if self.ycor() > SCREEN_LIMITS["bottom"]:
            y_cor = self.ycor() - SPEED
            x_cor = self.xcor()
            self.goto(x_cor, y_cor)

    def auto_move(self):
        x_cor = self.xcor()
        y_cor = self.ycor() + self.y_direction
        self.goto(x_cor, y_cor)

    def reverse(self):
        self.y_direction *= -1
