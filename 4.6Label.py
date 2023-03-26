from tkinter import *
master = Tk()
master.geometry("400x400")

# tạo label, entry cho tên người dùng
user_name = Label(master,text="Tên người dùng:").place(x=40,y=60)
user_name_input = Entry(master,width=30).place(x=140, y=60)

# tạo label, entry cho mật khẩu
user_password = Label(master,text="Mật khẩu:").place(x=40,y=100)
user_password_entry = Entry(master,width=30).place(x=140,y=100)

master.mainloop()