from tkinter import *
#Khởi tạo cửa sổ
window = Tk()
window.title("Window")
window.geometry("300x200")
#Khởi tạo biến bằng StringVar()
user = StringVar()
#Tạo hàm getValue để in ra được giá trị người dùng nhập vào
def getValue():
    print(user.get())
label = Label(window,text="Nhập tên:").place(x = 40, y = 60)
entry = Entry(window, textvariable= user).place(x = 100, y = 60)
submit = Button(window, text = "Summit", command=getValue).place(x = 50, y = 150)
window.mainloop()
