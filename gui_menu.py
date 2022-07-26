from tkinter import *

import time
import random
import tkinter

menulist = ['1', '2', '3' ]
root = Tk() 
root.title('사진불러오기')
root.geometry('800x600')
img = [
    tkinter.PhotoImage(file="1.png"),
    tkinter.PhotoImage(file="2.png"),
    tkinter.PhotoImage(file="3.png")]



py_img = tkinter.PhotoImage(file="1.png")
label_img = tkinter.Label(root, image=img[1])
label_img.pack()
label = Label(root,text=' \n AI가 추천해주는 메뉴는 ?  \n   ') 
label.pack()
def event():
    menu = random.choice(menulist) 
    print(menu)
    button['text'] = f'{menu} 추천!'
    label_img = tkinter.PhotoImage(file=img[menu])
    label_img.pack()

button = Button(root,text='추천 메뉴',command=event)


button.pack(side=LEFT,padx=10,pady=10) #side로 배치설정, padx로 좌우 여백설정, pady로 상하 여백설정 
#button2.pack(side=LEFT, padx=10, pady= 10)
root.mainloop()