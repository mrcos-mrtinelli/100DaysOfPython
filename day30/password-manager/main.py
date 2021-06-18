import io
from tkinter import *
from tkinter import messagebox as mb
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    pass_letters = [random.choice(letters) for _ in range(nr_letters)]
    pass_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    pass_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = pass_letters + pass_symbols + pass_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) > 0 and len(username) > 0 and len(password) > 0:
        new_login = {
            website: {
                "username": username,
                "password": password
            }
        }
        is_ok = mb.askyesno("Warning!", message="Ok to save the new password?")

        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)
                    data.update(new_login)
            except FileNotFoundError:
                with open("data.json", mode="w") as new_data_file:
                    json.dump(new_login, new_data_file, indent=4)
            else:
                with open("data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)

                website_input.delete(0, END)
                website_input.focus()
                password_input.delete(0, END)
        else:
            website_input.focus()
    else:
        mb.showinfo(title="Error!", message="Please fill out all fields.")


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
website_input = Entry(width=21)
website_input.focus()
username_input = Entry(width=40)
username_input.insert(0, "email@email.com")
password_input = Entry(width=21)
# - Positions
website_input.grid(column=1, row=1, sticky="w")
username_input.grid(column=1, row=2, columnspan=2, sticky="w")
password_input.grid(column=1, row=3, sticky="w")

# Buttons
search = Button(width=15, text="Get Password")
password_generate_btn = Button(width=15, text="Generate Password", command=generate_pass)
add_btn = Button(width=35, text="Add", command=save_to_file)
# - Positions
search.grid(column=2, row=1)
password_generate_btn.grid(column=2, row=3)
add_btn.grid(column=1, row=4, columnspan=2)

w.mainloop()
