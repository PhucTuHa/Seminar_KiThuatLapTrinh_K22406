from tkinter import *
import random
import string

def ngauNhien():
    password= []
    for i in range(4):
        lower=random.choice(string.ascii_lowercase)
        upper=random.choice(string.ascii_uppercase)
        password.append(lower)
        password.append(upper)
        passs=" ".join(str(x)for x in password)
        label.config(text=passs)

window =Tk()
window.geometry("300x400")
window.title("password ")
label = Label(window, font = ('arial', 40, 'bold'))
label.pack()
button1 =Button(window, text="Click", font = ('arial', 30, 'bold'),command= ngauNhien).pack()
window.mainloop()
