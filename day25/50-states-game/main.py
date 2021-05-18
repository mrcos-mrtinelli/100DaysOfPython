import turtle as t
from game_manager import GameManager


BG_IMAGE = "blank_states_img.gif"

gm = GameManager("50_states.csv")


screen = t.Screen()
screen.title("Name the 50 U.S. States Game")
screen.addshape(BG_IMAGE)
t.shape(BG_IMAGE)


while gm.score < 50:
    state_input = gm.get_user_input()

    if gm.is_answer_correct(state_input):
        gm.add_state_label(state_input)

screen.exitonclick()


