import turtle

TOTAL_STATES = 50


class Game_Manager:

    def __init__(self):
        self.all_states = []
        self.score = 0

    def get_user_input(self):
        title = f"{self.score} / {TOTAL_STATES} States Guessed"
        prompt = "Enter the name of a state"
        state_name = turtle.textinput(title, prompt)
        return state_name

    def is_input_correct(self, state_named):
        for state in self.all_states:
            if state_named.lower() in state.lower():
                self.score += 1
                state_name = state.split(",")[0]
                x_pos = state.split(",")[1]
                y_pos = state.split(",")[2].replace("\n", "")
                return state_name, x_pos, y_pos

    def add_state_label(self, state, x, y):
        x_pos = int(x)
        y_pos = int(y)
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.setposition(x_pos, y_pos)
        writer.write(state, False, "center", ("Arial", 16, "normal"))

