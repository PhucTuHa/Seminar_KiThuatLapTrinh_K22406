from tkinter import *

window = Tk()
window.title("Window")
window.geometry("300x200")

user = StringVar()
def getValue():
    print(user.get())
submit = Button(window, text = "Summit", command=getValue).place(x = 50, y = 150)
label = Label(window, textvariable= user).place(x = 80, y = 100)
entry = Entry(window, textvariable= user).place(x = 80, y = 60)

window.mainloop()