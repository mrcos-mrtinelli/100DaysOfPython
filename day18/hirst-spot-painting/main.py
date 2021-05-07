import turtle as t
import random

colors_list = [(1, 12, 31), (54, 25, 17), (218, 127, 106), (9, 104, 160), (242, 213, 68), (150, 83, 39), (216, 86, 63),
               (156, 6, 24), (165, 162, 30), (158, 62, 102), (207, 73, 103), (10, 64, 33), (11, 96, 57), (95, 6, 20),
               (175, 134, 162), (7, 173, 217), (1, 61, 145), (2, 213, 207), (158, 32, 23), (8, 140, 85),
               (144, 227, 217), (121, 193, 147), (220, 177, 216), (100, 218, 229), (251, 198, 1), (116, 170, 192)]

mr_t = t.Turtle()
screen = t.Screen()

mr_t.shape('turtle')
mr_t.penup()
screen.colormode(255)


def getcolor():
    return random.choice(colors_list)


def drawdots(size):
    y_pos = -252
    for _ in range(10):
        y_pos += 50
        mr_t.goto(-240, y_pos)
        for _ in range(10):
            mr_t.dot(size, getcolor())
            mr_t.forward(50)

    mr_t.hideturtle()


drawdots(20)

screen.exitonclick()
