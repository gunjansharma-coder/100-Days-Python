import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    if reps % 8 == 0:
        label.config(text="Long Break Timer", font=(FONT_NAME,35,"bold"),foreground=RED, bg=YELLOW)
        count_down(LONG_BREAK_MIN * 60)

    elif reps % 2 == 0:
        label.config(text="Short Break Timer", font=(FONT_NAME,35,"bold"),foreground=PINK, bg=YELLOW)
        count_down(SHORT_BREAK_MIN * 60)
        
    else:
        label.config(text="Work Timer", font=(FONT_NAME,35,"bold"),foreground=GREEN, bg=YELLOW)
        count_down(WORK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min=math.floor(count/60)
    count_second=count % 60
    if count_second==0:
        count_second="00"
    elif count_second<=9:
        count_second=f"0{count_second}"
    
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_second}")
    if count>0:
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        work_session=math.floor(reps/2)
        for _ in range(work_session):
            mark+="✓"
        check_marks.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_png=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_png)
timer_text=canvas.create_text(112,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(column=1,row=1)

label=Label(text="Timer",font=(FONT_NAME,35,"bold"),foreground=GREEN,bg=YELLOW)
label.grid(column=1,row=0)

reset_button=Button(text="Reset",command=reset_timer)
reset_button.grid(column=2,row=2)

check_marks = Label(font=(FONT_NAME, 20), foreground=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

start_button=Button(text="Start",command=start_timer)
start_button.grid(column=0,row=2)

window.mainloop()