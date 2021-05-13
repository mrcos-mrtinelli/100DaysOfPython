import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setup
wn = Screen()
wn.setup(width=600, height=600)
wn.title("Turtle Crossing!")
wn.tracer(0)
wn.listen()

# Game setup
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

is_game_running = True


def game_off():
    global is_game_running
    is_game_running = False
    print("Game off")


wn.onkey(game_off, "q")
wn.onkey(player.move, "Up")

while is_game_running:
    time.sleep(0.1)
    wn.update()

    cars.create_car()
    cars.move_cars()

    # Collision
    for car in cars.all_cars:
        if car.distance(player) < 20:
            print("squish")
            scoreboard.game_over()
            game_off()

    # Finish line
    if player.is_at_finish_line():
        scoreboard.level_up()
        cars.level_up()
        player.reset()

wn.exitonclick()
