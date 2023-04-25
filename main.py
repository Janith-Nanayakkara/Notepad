from tkinter import LEFT
from tkinter.filedialog import *

import tkinter as tk
canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg = "white")
top= tk.Frame(canvas)
top.pack(padx=10,pady=5,anchor="nw")

b1 = tk.Button(canvas, text ="open", bg ="white")
b1.pack(in_=top ,side=LEFT)
tk.Button
b2 = tk.Button(canvas, text ="save", bg ="white")
b2.pack(in_=top,side=LEFT)

b3 = tk.Button(canvas, text ="clear", bg ="white")
b3.pack(in_=top,side=LEFT)

b4 = tk.Button(canvas, text ="exit", bg ="white")
b4.pack(in_=top,side=LEFT)
canvas.mainloop()


