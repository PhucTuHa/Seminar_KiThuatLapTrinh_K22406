from tkinter import *
import tkinter as tk

win = Tk()
win.title("Pack")
frame = Frame(win)
frame.pack()

label1 = Label(win, text='Bảng cân đối kế toán', fg ='blue', bg='#add8e6', font='Arial,16',padx=10,pady=10)
label1.pack(side=TOP, fill=BOTH)

label2 = Label(win, text='Tài sản', fg ='white', bg='red', font='Arial,16', padx=30, pady=10)
label2.pack(side=LEFT)

label3 = Label(win, text='Nguồn vốn', fg ='green', bg='yellow', font='Arial,16', padx=30, pady=10)
label3.pack(side =RIGHT)

win.mainloop()