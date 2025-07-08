from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TICK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None # create this variable in order to cancel it but don't want it to have any values

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global reps, tick_count, timer
    if timer is not None:
        window.after_cancel(timer) # to cancel the timer that was set up previously
        timer = None
    reps = 0
    tick_count = 0
    timer_label.config(text="\n00:00")
    tick_label.config(text="")
    title_label.config(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
    start_action()

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_action():
    if reps < 8:
        if reps in [0,2,4,6]:
            count_down(0.5 * 60) # custom your time here
            title_label.config(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
        elif reps in [1,3,5]:
            count_down(0.25 * 60) # custom your time here
            title_label.config(text="Short Break", font=(FONT_NAME, 30, "bold"), fg=PINK, bg=YELLOW)
        elif reps == 7:
            count_down(1 * 60) # custom your time here
            title_label.config(text="Long Break", font=(FONT_NAME, 30, "bold"), fg=PINK, bg=YELLOW)
    else:
        window.destroy()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
tick_count = 0
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = int(count%60)
    timer_label.config(text=f"\n{count_min:02d}:{count_sec:02d}")
    # f"{value:02d}" formats the number with at least 2 digits, padding with zero if needed
    global timer
    if count > 0:
        timer = window.after(1000,count_down,count - 1)
    else:
        global tick_count, reps
        if reps in [0, 2, 4, 6]:
            tick_count += 1
            tick_label.config(text=TICK * tick_count) # Update label with more ticks

        reps += 1
        start_action()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Pomodoro")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME,30,"bold"), fg=GREEN, bg=YELLOW)
title_label.pack()

# Load the image
photo = PhotoImage(file="tomato.png")
# Create a label to display the image
timer_label = Label(text="\n00:00", image=photo, font=(FONT_NAME, 28, "bold"),
              fg="white", bg=YELLOW, compound="center") # compound="center" to center the text over the image
timer_label.pack()

# Create a frame to hold the two buttons side by side
button_frame = Frame(window)
button_frame.config(bg=YELLOW)
button_frame.pack()

# START button on the left
start_button = Button(button_frame, text="START", font=(FONT_NAME, 12, "bold"), command=start_action)
start_button.pack(side="left", padx=80)

# RESET button on the right
reset_button = Button(button_frame, text="RESET", font=(FONT_NAME, 12, "bold"), command=reset)
reset_button.pack(side="left", padx=80)

# Text widget below the buttons
tick_label = Label(window, text="", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW, width=8)
tick_label.pack(pady=20)



window.mainloop()