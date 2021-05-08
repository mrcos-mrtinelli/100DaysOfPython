from turtle import Turtle, Screen
import random

COLORS = ["red", "blue", "orange", "green", "purple"]
FINISH_LINE = 200
CONTINUE_RACE = True

x_pos = -230
y_pos = 200
space = 50
all_turtles = []

screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win? (pick a color)")

def setup_turtles(x, y, colors):
    y_pos = y

    for _ in range(1, 6):
        trtl = Turtle(shape="turtle")
        y_pos -= space
        trtl.color(colors.pop())
        trtl.speed(2)
        trtl.penup()
        trtl.goto(x=x_pos, y=y_pos)
        all_turtles.append(trtl)


def start_race():
    global CONTINUE_RACE
    while CONTINUE_RACE:
        for trtl in all_turtles:
            speed = random.randint(0, 10)
            trtl.forward(speed)

            if trtl.position()[0] >= FINISH_LINE:
                CONTINUE_RACE = False
                winning_turtle = trtl.color()[1]
                results(winning_turtle)


def results(winning_color):
    if user_bet == winning_color:
        print("You are the lucky winner!")
    else:
        print(f"You lose! The {winning_color} turtle won.")


random.shuffle(COLORS)
setup_turtles(x=x_pos, y=y_pos, colors=COLORS)

if user_bet != "":
    start_race()

screen.exitonclick()