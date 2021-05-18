import turtle as t
from game_manager import Game_Manager

BG_IMAGE = "blank_states_img.gif"

gm = Game_Manager()

with open("50_states.csv") as states_file:
    gm.all_states = states_file.readlines()

screen = t.Screen()
screen.title("Name the 50 U.S. States Game")
screen.addshape(BG_IMAGE)
t.shape(BG_IMAGE)


while gm.score < 50:
    state_input = gm.get_user_input()
    label_data = gm.is_input_correct(state_input)
    if label_data != "":
        gm.add_state_label(label_data[0], label_data[1], label_data[2])
