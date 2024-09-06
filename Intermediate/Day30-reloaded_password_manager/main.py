import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # print(string.printable) this includes spaces and tabs, so don't use it #0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ ♂♀
    """
    Generates a random password with 8 characters consisting of letters, digits, and punctuation marks.
    Copies the generated password to the clipboard using the pyperclip module.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join(random.choices(characters, k=8))
    pyperclip.copy(random_password)

    # getting the current string from the entry 
    current_password = password_entry.get()
    # If the password entry field is empty, it inserts the generated password     
    if len(current_password) == 0:
        password_entry.insert(index = 0, string = random_password)
    else:
    # But if the field is not empty, it first clears the field and then inserts the new password.
        password_entry.delete(0, tk.END)
        password_entry.insert(index = 0, string = random_password)


# ---------------------------- SEARCH DATA ------------------------------- #
def search_data():
    website = website_entry.get()
    
    try:
        with open('data.json') as f:
            user_data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File Found')
    else:
        if website in user_data:
            email = user_data[website]['email']
            password = user_data[website]['password']

            messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {password}')

        else:
            messagebox.showinfo(title='Not Found', message=f'No details exists for {website}')
        

# ---------------------------- VALIDATION ------------------------------- #
def validate_empty_fields(web, email, passw):
    '''
    Checks if any of the fields are empty. 
    Returns True if all fields are filled, False otherwise.
    '''
    if len(web) == 0 or len(passw) == 0 or len(email) == 0: 
        messagebox.showwarning(title=f"Oops", message=f"Please don't leave any fields empty") 

        return False
    return True


def confirm_user_details(web, email, passw):
    '''
    Asks the user for confirmation before saving the data. 
    Returns True if the user confirms, False otherwise.
    '''
    user_ans = messagebox.askokcancel(title=f"Welcome to MyPass {web}", message=f"These are the details entered:\nEmail: {email}\nPassword: {passw}\nIs it ok to save?") 

    return user_ans


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_credentials():
    website = website_entry.get() 
    email = email_entry.get() 
    password = password_entry.get()
    
    # the Python object (AKA the dictionary)
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    #Empty fields validations
    if not validate_empty_fields(web=website, email=email, passw=password):
        return #stops the execution of this function

    try:
        # using the .load() method to read the JSON FILE  
        with open('data.json') as f:
            data = json.load(f) 
    except FileNotFoundError:
        data = {}
    
    # .upadte() method to update the current data with the new data    
    data.update(new_data)
    # using the .dump() method to write the Python object on the JSON FILE 
    with open('data.json', 'w') as f:
        json.dump(data, f, indent = 4, sort_keys=True)


    # clearing fields
    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)



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
    new_entry.grid(row=row, column=column, columnspan=columnspan)
    new_entry.insert(index = 0, string = initial_text)

    return new_entry


# labels
label_generator(text='Website:', row=1)
label_generator(text='Email/Username:', row=2)
label_generator(text='Password:', row=3)

# entrys
website_entry = entry_generator(width= 33, row=1)
email_entry = entry_generator(initial_text= 'khaleesi@puppyemail.com', width= 52, row=2, columnspan=2)
password_entry = entry_generator(width= 33, row=3)

# buttons
button_generator(text = 'Generate Password', command = generate_password, row=3, column = 2)
button_generator(text = 'Add', command = save_credentials, width=44, row = 4, column= 1, columnspan = 2)

button_generator(text = 'Search', command = search_data, row = 1, column= 2, width= 15)


window.mainloop()










