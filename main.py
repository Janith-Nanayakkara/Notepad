from tkinter import LEFT
from tkinter.filedialog import *

import tkinter as tk
canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg = "white")

b1 = tk.Button(canvas, text ="open", bg ="white")
b1.pack(side=LEFT)
tk.Button
b2 = tk.Button(canvas, text ="save", bg ="white")
b2.pack(side=LEFT)
canvas.mainloop()


