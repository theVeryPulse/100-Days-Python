# This is a simple stimulation of the famous Pomodoro timer
# It will track the number of work cycles completed
# Users can reset the timer at any time
# SKILLS: tkinter, GUI, tkinter canvas
# Difficulty: hard

from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
SECONDS_IN_MIN = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global check_marks, timer, reps
    check_marks = ''
    check_mark_dp.config(text='')
    reps = 0
    title_dp.config(text='Timer')
    window.after_cancel(timer)
    canvas.itemconfig(count_down_dp, text='00:00')


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, title_dp
    print(f'reps {reps}')
    # count_down_in_seconds = 10
    # count_down(count_down_in_seconds)
    # print(count_down_in_seconds)
    if reps % 8 == 0 and reps != 0:  # after 4 works and 4 breaks
        print('Long break')
        count_down(LONG_BREAK_MIN * SECONDS_IN_MIN)
        reps = 0
        title_dp.config(text='Long break', fg=RED)
    elif reps % 2 == 0:
        print('work')
        reps += 1
        count_down(WORK_MIN * SECONDS_IN_MIN)
        title_dp.config(text='Work', fg=GREEN)
    else:
        print('short break')
        reps += 1
        count_down(SHORT_BREAK_MIN * SECONDS_IN_MIN)
        title_dp.config(text='Break', fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global check_marks, timer
    count_minutes = count // 60
    count_seconds = count % 60
    minutes_dp = f'{count_minutes}' if count_minutes >= 10 else f'0{count_minutes}'
    seconds_dp = f'{count_seconds}' if count_seconds >= 10 else f'0{count_seconds}'
    canvas.itemconfig(count_down_dp, text=f'{minutes_dp}:{seconds_dp}')
    if count >= 0:
        timer = window.after(1000, count_down, count - 1)
        print(f'count: {count}')
    else:  # count down to zero
        start_timer()
        if reps % 2 == 0:
            check_marks += '✓'
            check_mark_dp.config(text=check_marks)


# ---------------------------- UI SETUP ------------------------------- #
check_marks = ''
# window
window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=95, bg=YELLOW)

# tomato image and timer
tmt_img = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tmt_img)
count_down_dp = canvas.create_text(102, 132, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)
# Timer text
title_dp = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), bg=YELLOW, fg=GREEN, )
title_dp.grid(row=0, column=1)
# Start button
start_bt = Button(text='START', command=start_timer)
start_bt.grid(row=2, column=0)
# Reset Button
reset_bt = Button(text='RESET', command=reset_timer)
reset_bt.grid(row=2, column=2)
# Check mark
check_mark_dp = Label(text=check_marks, font=(FONT_NAME, 20, 'bold'), bg=YELLOW, fg=GREEN)
check_mark_dp.grid(row=3, column=1)

window.mainloop()