from tkinter import *
import pandas

BG_COLOR = '#B1DDC6'
FONT_BG = '#FFFFFF'
FONT = 'Arial'

# ===============
#   READ FILE
# ===============
filepath = 'data/french_words.csv'
data = pandas.read_csv(filepath)


# ===============
#   UI SETUP
# ===============
w = Tk()
w.config(padx=50, pady=50, bg=BG_COLOR)
w.title("French to English Flashcards")

# images
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
wrong_png = PhotoImage(file='images/wrong.png')
right_png = PhotoImage(file='images/right.png')

# card
canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front,)
canvas.grid(row=0, column=0, columnspan=2)

# buttons
wrong_btn = Button(image=wrong_png, highlightthickness=0, bd=0)
wrong_btn.grid(row=1, column=0)

right_btn = Button(image=right_png, highlightthickness=0, bd=0)
right_btn.grid(row=1, column=1)

# labels
title_label = Label(text="French", font=(FONT, 40, "italic"), width=33, justify="center", bg=FONT_BG)
title_label.place(x=8, y=150)

word_label = Label(text="trouve", font=(FONT, 60, "bold"), width=22, justify="center", bg=FONT_BG)
word_label.place(x=15, y=263)

w.mainloop()
