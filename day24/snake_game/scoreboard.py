from turtle import Turtle

FONT = ('Courier', 24, 'normal')
ALIGN = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.goto(0.0, 276)
        self.hideturtle()
        self.update()

    def save_high_score(self):
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")

    def update(self):
        self.clear()
        self.write(f'Score: {self.score} / High Score: {self.high_score}', move=False, align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

        self.score = 0
        self.update()

