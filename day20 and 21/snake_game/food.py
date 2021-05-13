import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('yellow')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed('fastest')
        self.penup()
        self.new_food()

    def new_food(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)
