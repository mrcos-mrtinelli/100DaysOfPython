from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
w = Tk()
w.config(padx=50, pady=50)
w.title("Password Manager")

logo_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# LABELS
website_label = Label(text="Website:")
username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
# - Positions
website_label.grid(column=0, row=1)
username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# ENTRY
website_input = Entry(width=35,)
username_input = Entry(width=35)
password_input = Entry(width=18)
# - Positions
website_input.grid(column=1, row=1, columnspan=2)
username_input.grid(column=1, row=2, columnspan=2)
password_input.grid(column=1, row=3)

# Buttons
password_generate_btn = Button(text="Generate Password")
add_btn = Button(width=36, text="Add")
# - Positions
password_generate_btn.grid(column=2, row=3)
add_btn.grid(column=1, row=4, columnspan=2)

w.mainloop()
