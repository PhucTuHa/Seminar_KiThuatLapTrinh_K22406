from tkinter import *
import time
window= Tk()
window.geometry("400x100")
window.title("CLOCK")
window.config(bg='#C0C0C0')

def update():
    clock.config(text=time.strftime("%I:%M:%S"))
    clock.after(1000,update)

clock = Label(window, background = 'black',foreground = 'white', font = ('arial', 40, 'bold'))
clock.pack()
update()
window.title('clock')
window.mainloop()