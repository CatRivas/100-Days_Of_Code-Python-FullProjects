import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"


########################    LOGIC   #########################
def right_funct():
    pass

def wrong_funct():
    pass


########################    UI   #########################
window = tk.Tk()
window.title('Flash card app 14-09-2024')
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# card image
front_image = tk.PhotoImage(file='images/card_front.png')

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image= front_image)
canvas.grid(row = 0, column=0, columnspan = 2)

# labels on the canvas
french_label = canvas.create_text(400, 150, text='French', font = (FONT_NAME, 40, 'italic'))
english_label = canvas.create_text(400, 263, text='english', font = (FONT_NAME, 60, 'bold'))

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

wrong_button =  button_generator(image=wrong_image, command = wrong_funct, row = 1, column = 0)
right_button =  button_generator(image=right_image, command = right_funct, row = 1, column = 1)








window.mainloop()
