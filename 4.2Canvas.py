from tkinter import *
import tkinter as tk
from tkinter import ttk

#Khởi tạo
win = Tk()
win.geometry('500x400')
win.title("Canvas")
#Canvas
canvas = Canvas(win, bg ='white', width = 600, height = 400 )
canvas.pack()

# canvas.create_rectangle((50,20,100,200),fill = 'red', width = 2, outline = 'green' )
# canvas.create_line((0,0,50,100), width = 2, fill='blue')

# Theo Default
canvas.create_oval((200,0,300,100), fill="green")
canvas.create_arc((200,0,300,100),fill='red', start = 45, extent=180)

# Style ARC: hình vòng cung
canvas.create_oval((100,100,200,200), fill="green")
canvas.create_arc((100,100,200,200),fill='red', start = 45, extent=180, style = tk.ARC, width = 5, outline = 'red')

# Style Pieslice
canvas.create_oval((10,20,110,120), fill="green")
canvas.create_arc((10,20,110,120),fill='red', start = 45, extent=180, style = tk.PIESLICE, width = 5, outline = 'red')

# Style Chord
canvas.create_oval((250,200,350,300), fill="green")
canvas.create_arc((250,200,350,300),fill='red', start = 45, extent=90, style = tk.CHORD, width = 5, outline = 'red')

canvas.create_polygon((0,0,100,200,300,50), fill='green')
# canvas.create_text(100,300, text ="This is some text", fill='green')
# canvas.create_window((450,100),window = ttk.Button(win, text='This is a text in a canvas'))
win.mainloop()

#Khởi tạo
win = Tk()
win.geometry('400x300')
win.title("Canvas")
#Canvas
canvas = Canvas(win, bg ='#faebd7', width = 350, height = 250 )
canvas.pack()
# Tạo đường thẳng
canvas.create_line (50,50,150,50, width = 2, fill='blue')
canvas.create_line (150,50,150,150, width = 2, fill='green', dash=(4,2))
canvas.create_line (150,150,250,150, width = 2, fill='#800000')
canvas.create_line (250,150,250,250, width = 2, fill='#800080', dash =(4,2))
win.mainloop()

#Khởi tạo
win = Tk()
win.geometry('400x300')
win.title("Canvas")
#Canvas
canvas = Canvas(win, bg = '#faebd7', width = 350, height = 250)
canvas.pack()
#Ghi chữ lên canvas
canvas.create_text((100,100), text = "Lớp học hợp trình", fill = "green")
canvas.create_window((250,100), window = tk.Button(win, text = "Lớp học lập trình"))
win.mainloop()