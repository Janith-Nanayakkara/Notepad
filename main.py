from pickle import TRUE
from tkinter import LEFT, WORD, BOTH
from tkinter.filedialog import *

import tkinter as tk

import openFile as openFile
import saveFile as saveFile

canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg = "white")
top= tk.Frame(canvas)
top.pack(padx=10,pady=5,anchor="nw")

b1 = tk.Button(canvas, text ="open", bg ="white", command = openFile)
b1.pack(in_=top ,side=LEFT)
tk.Button
b2 = tk.Button(canvas, text ="save", bg ="white" ,command= saveFile)
b2.pack(in_=top,side=LEFT)

b3 = tk.Button(canvas, text ="clear", bg ="white",command= clearFile)
b3.pack(in_=top,side=LEFT)

b4 = tk.Button(canvas, text ="exit", bg ="white" ,command=exit)
b4.pack(in_=top,side=LEFT)

entry = tk.Text(canvas,wrap=WORD, bg ="F9DDA4", font=("poppins",15))
entry.pack(padx=10 , pady= 5 , expand=TRUE , fill=BOTH)
canvas.mainloop()


