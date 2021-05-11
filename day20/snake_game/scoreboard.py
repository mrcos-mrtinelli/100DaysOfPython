from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.goto(0.0, 280)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f'Score: {self.score}', move=False, align='center', font=('Arial', 14, 'normal'))
