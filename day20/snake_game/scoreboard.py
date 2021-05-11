from turtle import Turtle

FONT = ('Courier', 24, 'normal')
ALIGN = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.goto(0.0, 276)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f'Score: {self.score}', move=False, align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align=ALIGN, font=FONT)
