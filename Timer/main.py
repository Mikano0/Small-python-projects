from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = "✔"
reps = 0

timer = None
# ---------------------------- Pause Timer------------------------------- #
def pause_timer():
    # still have to update and remake
    window.after_cancel(timer)
    
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig (timer_text, text = "00:00")
    title.config(text = "Timer", fg = GREEN)
    check_label.config(text= "")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        title.config(text = "Working", fg = GREEN)
        count_down(work_sec)
    elif reps % 8 == 0:
        title.config(text = "Break", fg = RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title.config(text = "Break", fg = PINK)
        count_down(short_break_sec)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(10, count_down, count - 1)
    elif count == 0:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += CHECK
        check_label.config(text = marks)
            
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Pomodoro")
window.config(padx = 100, pady= 50, bg= YELLOW)

check_label = Label(text= "", width=10, fg= GREEN, bg= YELLOW, font = (FONT_NAME, 14, "bold"))

check_label.grid(column= 1, row = 4)

canvas = Canvas(width= 200, height= 224, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file = "Day 28/tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "White", font=(FONT_NAME, 34, "bold"))
canvas.grid(column= 1, row= 2)

title = Label(text = "Timer", bg = YELLOW, fg= GREEN, font = (FONT_NAME, 24, "bold"))
title.grid(column=1, row = 1)

start = Button(text = "Start",  highlightthickness=0, command = start_timer)
start.grid(column= 0 , row = 3)

reset = Button(text = "Reset",  highlightthickness=0, command = reset_timer)
reset.grid(column= 3 , row = 3 )

pause = Button(text= "Pause",  highlightthickness=0, command= pause_timer)
pause.grid(column= 1 , row = 3 )



window.mainloop()