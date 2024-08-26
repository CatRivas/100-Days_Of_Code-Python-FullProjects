import tkinter as tk
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.25
work_repetitions = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_pomodoro():
    """
    Resets the Pomodoro timer and related UI elements.
    - Stops the current timer.
    - Resets work repetitions.
    - Resets timer display and title label.
    - Clears the check mark display.
    """
    # reset work repetitions
    global work_repetitions
    work_repetitions = 0

    # stop timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer', fg=GREEN)
    check_mark_label.config(text='')
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_pomodoro():
    """
    Starts the Pomodoro timer based on work_repetition
    """
    
    # global variable
    global work_repetitions, timer

    # cancel any existing timer before starting a new one (you now can press Start and there won't be multiple timers running simultaneously)
    if timer is not None:
        window.after_cancel(timer)

    work_repetitions += 1
    print(work_repetitions)
    
    total_work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if work_repetitions % 8 == 0:
        time_counter(long_break_sec)
        title_label.config(text='FREEDOM!', fg=RED)
    elif work_repetitions % 2 == 0:
        time_counter(short_break_sec)
        title_label.config(text='Break', fg=PINK)
    else:
        time_counter(total_work_sec)
        title_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# after() is used to schedule the execution of a function or command after a specified period of time.
# SYNTAX -> widget.after(milliseconds, function to be executed after the specified time, *args (optional arguments))

def time_counter(counter):
    time_structure = time.gmtime(counter)
    time_format = time.strftime('%M:%S', time_structure)
    canvas.itemconfig(timer_text, text=time_format)
    if counter > 0:
        global timer

        # Continue the countdown every second
        timer = window.after(1000, time_counter, counter - 1)
    else:
        # Start the next session and update check marks
        start_pomodoro()
        update_check_marks()


def update_check_marks():
    """
    Updates the number of check marks displayed based on work sessions completed.
    - For every 2 work sessions, adds a '✔' mark.
    """

    work_sessions = math.floor(work_repetitions/2)
    mark = '✔' * work_sessions
    check_mark_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Pomodoro 22-08-2024')
window.config(padx= 100, pady=50, bg=YELLOW)

bg_image = tk.PhotoImage(file='tomato.png')

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112,  image= bg_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)



# labels
title_label = tk.Label(text='Timer', font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

check_mark_label = tk.Label(font=(FONT_NAME, 20, 'bold'), fg=GREEN, bg=YELLOW)
check_mark_label.grid(row=4, column=1)


# buttons
def create_button(row = 2, **kwargs):
    style = {
        'bg': kwargs.get('bg', PINK),
        'fg': kwargs.get('fg', 'white'),
        'font': kwargs.get('font', (FONT_NAME, 12, 'bold'))
    }

    # unpacking dict
    new_button = tk.Button(text = kwargs['text'], command = kwargs['command'],  **style)

    if 'row' in kwargs:
        new_button.grid(row = kwargs['row'], column = kwargs['column'])
    else:
        new_button.grid(row = row, column = kwargs['column'])

    return new_button

create_button(text='Start', command = start_pomodoro, column = 0)
create_button(text='Reset', command = reset_pomodoro, column = 2, bg=RED)



window.mainloop()
