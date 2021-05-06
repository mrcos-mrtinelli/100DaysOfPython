import turtle
from turtle import Turtle, Screen
import random


def colors():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    return r, g, b


turtle.colormode(255)
t1 = Turtle()
screen = Screen()

screen.bgcolor("black")

# t1.shape("circle")
t1.color("green")
t1.speed("fastest")


def draw_spirograph(size):
    for _ in range(int(360 / size)):
        t1.pencolor(colors())
        t1.circle(100)
        t1.setheading(t1.heading() + size)


draw_spirograph(15)

screen.exitonclick()
