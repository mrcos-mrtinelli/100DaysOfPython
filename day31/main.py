import pandas
import random
from tkinter import *

BG_COLOR = '#B1DDC6'
FONT_BG = '#FFFFFF'
FONT = 'Arial'

front_card_word = []
back_card_word = []

# ===============
#   READ FILE
# ===============
filepath = 'data/french_words.csv'
data = pandas.read_csv(filepath).to_dict(orient="records")


# ===============
#   MANAGE WORDS
# ===============
def get_new_word():
    global front_card_word, back_card_word
    word_pair = random.choice(data)
    front_card_word = ['French', word_pair['French']]
    back_card_word = ['English', word_pair['English']]


# ===============
#   MANAGE CARDS
# ===============
def next_card():
    canvas.itemconfig(current_card_image, image=card_front_png)
    get_new_word()
    canvas.itemconfig(card_title, text=front_card_word[0])
    canvas.itemconfig(card_word, text=front_card_word[1])

    w.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(current_card_image, image=card_back_png)
    canvas.itemconfig(card_title, text=back_card_word[0])
    canvas.itemconfig(card_word, text=back_card_word[1])


# ===============
#   UI SETUP
# ===============
w = Tk()
w.config(padx=50, pady=50, bg=BG_COLOR)
w.title("French to English Flashcards")

# images
card_front_png = PhotoImage(file='images/card_front.png')
card_back_png = PhotoImage(file='images/card_back.png')
wrong_png = PhotoImage(file='images/wrong.png')
right_png = PhotoImage(file='images/right.png')

# card
canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
current_card_image = canvas.create_image(400, 263, image=card_front_png)
card_title = canvas.create_text(400, 150, text="TITLE", font=(FONT, 40, "italic"))
card_word = canvas.create_text(400, 263, text="WORD", font=(FONT, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# buttons
wrong_btn = Button(image=wrong_png, highlightthickness=0, bd=0, command=next_card)
wrong_btn.grid(row=1, column=0)

right_btn = Button(image=right_png, highlightthickness=0, bd=0, command=next_card)
right_btn.grid(row=1, column=1)

# labels
# title_label = Label(text="French", font=(FONT, 40, "italic"), width=33, justify="center", bg=FONT_BG)
# title_label.place(x=8, y=150)
#
# word_label = Label(text="trouve", font=(FONT, 60, "bold"), width=22, justify="center", bg=FONT_BG)
# word_label.place(x=15, y=263)

next_card()

w.mainloop()
