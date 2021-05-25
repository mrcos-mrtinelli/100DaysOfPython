from tkinter import *


def calculate():
    miles = int(input.get())
    result_label.config(text=f"{miles * 1.609}")


window = Tk()
window.title("My First GUI Program")
window.minsize(width=300, height=200)
window.config(padx=30, pady=50)

#dummy label
label_1 = Label(text="")
label_1.grid(column=0, row=0)

#Entry
input = Entry(width=10)
input.grid(column=1, row=0)

#Label
mi_label = Label(text="Miles", font=("Arial", 14, "bold"))
mi_label.grid(column=2, row=0)

#Label
desc_label = Label(text="is equal to", font=("Arial", 14, "bold"))
desc_label.grid(column=0, row=1)

#Label
result_label = Label(text="0", font=("Arial", 14, "bold"))
result_label.grid(column=1, row=1)

#Label
km_label = Label(text="Km", font=("Arial", 14, "bold"))
km_label.grid(column=2, row=1)

#Button
calc_btn = Button(text="Calculate", command=calculate)
calc_btn.grid(column=1, row=2)













window.mainloop()