from tkinter import *
# Khởi tạo
win = Tk()
win.geometry("300x100")
win.title("Widget Radiobutton")
#Radiobutton
var = IntVar()
def lang():
    if var.get() == 1:
       print("English")
    elif var.get() == 2:
        print("Tiếng Việt")
    elif var.get() == 3:
        print("ジャンパン")
    else:
        pass
Label(win, text = "Chọn ngôn ngữ hiển thị", justify = CENTER).pack()
c1 = Radiobutton(win, text="Tiếng Anh", variable=var, value=1, relief = RIDGE, width=20, command = lang).pack()
c2 = Radiobutton(win, text="Tiếng Việt", variable=var, value=2, relief = RIDGE, width=20, command = lang).pack()
c3 = Radiobutton(win, text="Tiếng Nhật", variable=var, value=3, relief = RIDGE, width=20, command = lang).pack()
win.mainloop()