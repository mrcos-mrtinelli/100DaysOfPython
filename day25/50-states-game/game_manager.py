import turtle
import pandas

TOTAL_STATES = 50


class GameManager:

    def __init__(self, file):
        self.df = pandas.read_csv(file)
        self.state_list = self.df.state.tolist()
        self.score = 0

    def get_user_input(self):
        title = f"{self.score} / {TOTAL_STATES} States Guessed"
        prompt = "Enter the name of a state"
        state_name = turtle.textinput(title, prompt)
        return state_name.lower()

    def is_answer_correct(self, state_named):
        for state in self.state_list:
            if state_named == state.lower():
                self.score += 1
                return True
        else:
            return False

    def add_state_label(self, state):
        state_data = self.df[self.df.state.str.lower() == state]
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.setposition(int(state_data.x), int(state_data.y))
        writer.write(state_data.state.item(), False, "center", ("Courier", 12, "normal"))

