from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 3
LONG_BREAK_MIN = 4

is_work = True
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global is_work, reps
    timer_title.config(text="Ready?", fg=GREEN)
    check_label.config(text="")
    is_work = True
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    if is_work:
        timer_title.config(text="Work!", fg=GREEN)
        countdown(WORK_MIN * 60)
    elif reps < 4:
        timer_title.config(text="Short Break!", fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        timer_title.config(text="Long Break!", fg=RED)
        countdown(LONG_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global is_work, reps
    minutes = count // 60
    seconds = count % 60
    time_str = "{:02d}:{:02d}".format(minutes, seconds)
    canvas.itemconfig(timer_label, text=time_str)
    if count > 0:
        window.after(10, countdown, count - 1)
    elif reps == 4:
        timer_title.config(text="Completed!", fg=GREEN)
        check_label.config(text="✔")
    else:
        if is_work:
            reps += 1
        is_work = not is_work
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

timer_title = Label(text="Ready?", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
timer_title.grid(column=1, row=0)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=250, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(125, 112, image=tomato_img)
timer_label = canvas.create_text(125, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_btn.grid(column=2, row=2)

check_label = Label(text="", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

window.mainloop()
