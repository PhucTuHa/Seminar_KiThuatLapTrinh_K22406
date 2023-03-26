from tkinter import *
import tkinter as tk

win = Tk()
win.title("Checkbutton")
win.geometry('400x300')
frame = Frame(win)
frame.pack()
label = Label(frame, text="Bạn thích background màu gì?", padx=15, pady=15)
label.pack()
def doimau():
    if var1.get() == 0 and var2.get() == 0:
        win.config(bg='white')
    elif var1.get() == 1 and var2.get() == 0:
        win.config(bg='#8a2be2')
    else:
        win.config(bg='#228b22')
var1 = IntVar()
var2 = IntVar()
Button1 = tk.Checkbutton(win, text='Màu tím', variable=var1, onvalue =1, offvalue=0, command=doimau)
Button2 = tk.Checkbutton(win, text='Màu xanh lá', variable=var2, onvalue=1, offvalue=0, command=doimau)
Button1.pack()
Button2.pack()
win.mainloop()