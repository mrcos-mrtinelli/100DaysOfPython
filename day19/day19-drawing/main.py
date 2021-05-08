from turtle import Turtle, Screen

trtl = Turtle()
screen = Screen()

def moveforward():
    trtl.forward(10)


def movebackward():
    trtl.backward(10)


def movecounterclock():
    trtl.left(10)


def moveclockwise():
    trtl.right(10)


def clear():
    trtl.clear()
    trtl.penup()
    trtl.home()
    trtl.pendown()


screen.listen()
screen.onkey(key="w", fun=moveforward)
screen.onkey(key="s", fun=movebackward)
screen.onkey(key="a", fun=movecounterclock)
screen.onkey(key="d", fun=moveclockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()