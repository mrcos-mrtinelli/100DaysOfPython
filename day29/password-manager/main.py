from tkinter import *
from tkinter import messagebox as mb
import random
import pyperclip


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
        save_str = f"{website}  |   {username}  |   {password}\n"
        website_input.delete(0, END)
        website_input.focus()
        password_input.delete(0, END)
        is_ok = mb.askyesno("Warning!", message="Ok to save the new password?")

        if is_ok:
            with open("data.txt", mode="a") as pass_db:
                pass_db.write(save_str)
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
website_input = Entry(width=35, )
website_input.focus()
username_input = Entry(width=35)
username_input.insert(0, "email@email.com")
password_input = Entry(width=18)
# - Positions
website_input.grid(column=1, row=1, columnspan=2)
username_input.grid(column=1, row=2, columnspan=2)
password_input.grid(column=1, row=3)

# Buttons
password_generate_btn = Button(width=13, text="Generate Password", command=generate_pass)
add_btn = Button(width=35, text="Add", command=save_to_file)
# - Positions
password_generate_btn.grid(column=2, row=3)
add_btn.grid(column=1, row=4, columnspan=2)

w.mainloop()
