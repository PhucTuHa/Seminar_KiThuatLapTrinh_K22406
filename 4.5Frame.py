from tkinter import *
window = Tk()
window.title("Học phần K22406")
window.geometry("300x150")

label = Label(window, text='Kĩ thuật lập trình', font="60").pack()
#Khởi tạo widgets Frame
frame = Frame(window).pack()
bottomframe = Frame(window).pack(side=BOTTOM)
button1 = Button(frame, text="Môn1", fg="red", font="70").pack(side=BOTTOM)
button2 = Button(frame, text="Môn2", fg="brown", font="70").pack(side=BOTTOM)
button3 = Button(frame, text="Môn3", fg="blue", font="70").pack(side=BOTTOM)
window.mainloop()
