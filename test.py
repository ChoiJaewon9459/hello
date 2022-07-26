
from tkinter import *
import tkinter

window=tkinter.Tk()
window.title("tk")
window.geometry("640x400+100+100")
window.resizable(True, True)

img = [
    PhotoImage(file="1.png"),
    PhotoImage(file="2.png"),
    PhotoImage(file="3.png")]

image=img[0]

label=tkinter.Label(window, image=image)
label.pack()

window.mainloop()