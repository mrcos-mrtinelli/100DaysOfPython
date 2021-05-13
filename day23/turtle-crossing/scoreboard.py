from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")
LEVEL_POS = {
    "x": -230,
    "y": 260
}
GAME_OVER_POS = {
    "x": 0,
    "y": 0
}


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.level = 1
        self.update()

    def level_up(self):
        self.level += 1
        self.update()

    def update(self):
        self.clear()
        self.setposition(LEVEL_POS["x"], LEVEL_POS["y"])
        self.write(f"Level: {self.level}", False, ALIGN, FONT)

    def game_over(self):
        self.setposition(GAME_OVER_POS["x"], GAME_OVER_POS["y"])
        self.write("GAME OVER", False, ALIGN, FONT)


