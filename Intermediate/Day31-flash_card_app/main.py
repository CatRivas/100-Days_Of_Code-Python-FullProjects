import tkinter as tk
import pandas as pd
import random 

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"


########################    LOGIC   #########################
list_dict = {}
new_word = {}

try:
    new_data_path = 'data/words_to_learn.csv'
    new_df = pd.read_csv(new_data_path)
except FileNotFoundError:
    data_path = 'data/french_words.csv'
    df = pd.read_csv(data_path)
    list_dict = df.to_dict(orient="records")
else:
    list_dict = new_df.to_dict(orient="records")


def check_word():
    # press the check button
    list_dict.remove(new_word)

    new_df = pd.DataFrame(list_dict)
    new_df.to_csv('data/words_to_learn.csv', index=False)

    update_word()


def random_word():
    random_item = random.choice(list_dict)
    
    return random_item    


def update_word():
    global new_word
    global timer_id
    
    window.after_cancel(timer_id)

    new_word = random_word()
    canvas.itemconfig(title_label, text='French', fill='black')
    canvas.itemconfig(word_label, text=new_word['French'], fill='black')
    canvas.itemconfig(card_image, image = front_image)

    timer_id =window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_image, image = back_image)
    canvas.itemconfig(title_label, text='English', fill='white')
    canvas.itemconfig(word_label, text=new_word['English'], fill='white')
    


########################    UI   ###########################
window = tk.Tk()
window.title('Flash card app 14-09-2024')
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# card images 
front_image = tk.PhotoImage(file='images/card_front.png')
back_image = tk.PhotoImage(file='images/card_back.png')

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image= front_image)
canvas.grid(row = 0, column=0, columnspan = 2)

# labels on the canvas
title_label = canvas.create_text(400, 150, text='Title', font = (FONT_NAME, 40, 'italic'))
word_label = canvas.create_text(400, 263, text='word', font = (FONT_NAME, 60, 'bold'))

# buttons
def button_generator(**kwargs):
    image = kwargs.get('image', None)
    command = kwargs.get('command', None)
    width = kwargs.get('width', 0)
    row = kwargs.get('row', 0)
    column = kwargs.get('column', 0)
    highlightthickness=0

    new_button = tk.Button(image = image, command = command, width=width, highlightthickness=highlightthickness)
    new_button.grid(row = row, column = column)

    return new_button


# photo objects for the buttons 
right_image = tk.PhotoImage(file='images/right.png')
wrong_image = tk.PhotoImage(file='images/wrong.png')

wrong_button =  button_generator(image=wrong_image, command = update_word, row = 1, column = 0)
right_button =  button_generator(image=right_image, command = check_word, row = 1, column = 1)


# Flip the card every 3 seconds
timer_id = window.after(3000, flip_card) 


# Start by showing the first word
update_word()


window.mainloop()

