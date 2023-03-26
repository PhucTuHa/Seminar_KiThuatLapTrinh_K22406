from tkinter import *
root=Tk()
root.geometry("200x200")
root.title('Button')
button=Button(root, text='Tạo lập một button', activebackground='white', activeforeground='red', state='active')
button.pack()
root.mainloop()