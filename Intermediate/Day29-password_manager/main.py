import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    pass

# ---------------------------- UI SETUP ------------------------------- #
# main window
window = tk.Tk()
window.title('Password Manager 30-08-2024')
window.config(padx=50, pady=20)

logo_image = tk.PhotoImage(file='logo.png')

# the image canvas
canvas = tk.Canvas(window, width=200, height=200)
canvas.create_image(100, 100, image= logo_image)

canvas.grid(row=0, column=1)


def label_generator(column = 0, **kwargs):
    text = kwargs.get('text', '')
    row = kwargs.get('row', 0)
    column = kwargs.get('column', column)

    new_label = tk.Label(text=text)
    new_label.grid(row=row, column=column)


def button_generator(**kwargs):
    text = kwargs.get('text', '')
    command = kwargs.get('command', None)
    width = kwargs.get('width', 0)
    row = kwargs.get('row', 0)
    column = kwargs.get('column', 0)
    columnspan = kwargs.get('columnspan', 1)

    new_button = tk.Button(text = text, command = command, width=width)
    new_button.grid(row = row, column = column, columnspan=columnspan)

    return new_button



def entry_generator(**kwargs):
    initial_text = kwargs.get('initial_text', '')
    width = kwargs.get('width', 0)
    row = kwargs.get('row', 0)
    column = kwargs.get('column', 1)
    columnspan = kwargs.get('columnspan', 1)

    new_entry = tk.Entry(width = width)
    new_entry.insert(index = 0, string = initial_text)
    # new_entry.grid(row=row, column=column, columnspan=columnspan, sticky='W')
    new_entry.grid(row=row, column=column, columnspan=columnspan)

    return new_entry


label_generator(text='Website:', row=1)
label_generator(text='Email/Username:', row=2)
label_generator(text='Password:', row=3)

entry_generator(initial_text= 'website name', width= 52, row=1, columnspan=2)
entry_generator(initial_text= 'email or name', width= 52, row=2, columnspan=2)
entry_generator(initial_text= 'password', width= 33, row=3)


button_generator(text = 'Generate Password', command = generate_password, row=3, column = 2)
button_generator(text = 'Add', command = save_password, width=44, row = 4, column= 1, columnspan = 2)






window.mainloop()















