import tkinter as tk
from tkinter import ttk

def greet():
    print('Hello, world!')

root = tk.Tk()
root.title('Hello')

greet_button = ttk.Button(root, text='Hello', command=greet)
greet_button.pack(side='left', fill='x', expand=True)

quit.button = ttk.Button(root, text='Quit', command=root.destroy)
quit.button.pack(side='left', fill='x', expand=True)

root.mainloop()
