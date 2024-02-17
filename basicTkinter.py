import tkinter as tk
from tkinter import ttk

#functions
def function():
    print('here we are!!')

def add_text():
    print('hello world!')

def update_text():
    data = entry_1.get()
    print(data)
    
    #update label text
    label_1.config(text = 'update here')

#creat a window
window = tk.Tk()
window.title('Yoo wassup')
window.geometry('600x700')

#create widgets with tk.text
txt = tk.Text(master = window)
txt.pack()

# create widget with ttk.label
label = ttk.Label(master=window, text='Hello World')
label.pack()

#ttk entry
entry = ttk.Entry(master=window)
entry.pack()

exercice_label = ttk.Label(master = window, text = 'my label')
exercice_label.pack()

# ttk button
button = ttk.Button(master = window, text = 'button', command = function)
button.pack()

exercice_button = ttk.Button(master = window, text = 'my button', command = lambda: print('Faaaast!!'))
exercice_button.pack()

# exercice
# adding text lable and button with fuction that print heelo world!
# the label should say my label and be between entry widget and the button

# get data from entry data
label_1 = ttk.Label(master = window, text = 'Add your data here:')
label_1.pack()

entry_1 = ttk.Entry(master = window)
entry_1.pack()

button_1 = ttk.Button(master = window, text = 'Add Data', command = update_text)
button_1.pack()

#run
window.mainloop()