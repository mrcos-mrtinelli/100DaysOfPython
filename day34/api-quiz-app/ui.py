from quiz_brain import QuizBrain
from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz_brain = quiz
        self.w = Tk()
        self.w.title("Quizzler")
        self.w.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(
            150,
            125,
            text="Quiz Question",
            font=('Arial', 20, 'italic'),
            fill=THEME_COLOR,
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.true_png = PhotoImage(file='images/true.png')
        self.true_btn = Button(image=self.true_png,
                               bd=0,
                               highlightbackground=THEME_COLOR,
                               highlightthickness=0,
                               command=lambda: self.get_correct_answer("true")
                               )
        self.true_btn.grid(row=2, column=0, padx=20, pady=20)
        self.false_png = PhotoImage(file='images/false.png')
        self.false_btn = Button(image=self.false_png,
                                bd=0,
                                highlightbackground=THEME_COLOR,
                                highlightthickness=0,
                                command=lambda: self.get_correct_answer("false")
                                )
        self.false_btn.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.w.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            q = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q)
        else:
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
            self.canvas.itemconfig(self.canvas_text, text=f"Final Score: {self.quiz_brain.score}/10")

    def get_correct_answer(self, answer):
        self.give_feedback(self.quiz_brain.check_answer(answer))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
            self.score.config(text=f"Score: {self.quiz_brain.score}")
        else:
            self.canvas.config(bg="red")

        self.w.after(1000, func=self.get_next_question)





