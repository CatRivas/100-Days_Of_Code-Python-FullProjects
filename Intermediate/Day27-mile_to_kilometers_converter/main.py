import tkinter as tk

KM = 1.60934

def calculate_conversion():
    miles = miles_entry.get()
    km =  float(miles) * KM
    km_label.config(text=f'{km:.2f}')
    

# main window
window = tk.Tk()
window.title('Mile to Km converter (15-08-24)')
window.config(padx= 40, pady=40)
window.minsize(width=200, height=150)


# static labels
def label_generator(**kwargs):
    label = tk.Label(text= kwargs['text'])
    label.grid(row= kwargs['row'], column= kwargs['column'])
    
    if 'padx' in kwargs:
        label.config(padx=kwargs['padx'])
    if 'pady' in kwargs:
        label.config(padx=kwargs['pady'])

label_generator(text= 'Is equal to', row= 1, column=0, padx=15)
label_generator(text= 'Miles', row= 0, column=2, padx=15)
label_generator(text= 'Km', row= 1, column=2, padx=15)

# label to be updated
km_label = tk.Label(text='0', padx=15)
km_label.grid(row=1, column=1)


# entry
miles_entry = tk.Entry(width=10)
miles_entry.grid(row=0, column=1)


# button
calculate_button = tk.Button(text='Calculate', command=calculate_conversion)
calculate_button.grid(row=2, column=1)


window.mainloop()