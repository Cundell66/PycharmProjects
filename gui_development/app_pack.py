import tkinter as tk

root = tk.Tk()

tk.Label(root, text='label 1', bg='green').pack(side='top', fill='both', expand=True)
tk.Label(root, text='label 2', bg='red').pack(side='left', fill='both', expand=True)

tk.Label(root, text='label 3', bg='blue').pack(side='left', fill='both', expand=True)

root.mainloop()
