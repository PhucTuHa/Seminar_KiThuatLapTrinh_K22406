# .Grid()
from tkinter import *
master = Tk()

# Tạo các widget Label
l1 = Label(master, text="Tên")
l2 = Label(master, text="Mật khẩu")

# Khai báo vị trí Label trong bảng
l1.grid(row=0, column=0, sticky=W)
l2.grid(row=1, column=0, sticky=W)

# Tạo các widget Entry và khai báo vị trí
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

# Tạo widget Checkbutton và khai báo vị trí
c1 = Checkbutton(master, text="Đã check")
c1.grid(row=2, column=0, sticky=W)

# Tạo các widget Button và khai báo vị trí
b1 = Button(master, text="Nút 1")
b2 = Button(master, text="Nút 2")
b1.grid(row=2, column=2)
b2.grid(row=2, column=3)

mainloop()