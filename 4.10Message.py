from tkinter import *
#Tạo cửa sổ giao diện với biến "win"
win = Tk()

#để thay đổi tên tiêu đề tk mặc định của cửa sổ
win.title("MESSAGE")

#để thay đổi kích thước mặc định của cửa sổ hiển thị (400:width, 500:height)
win.geometry("400x500")

#thay đổi background(màu nền của cửa sổ hiển thị)
win["bg"] = "navyblue"

#Tạo message
mes = Message(win,text = "What's your name ?",bg = "lightcoral",
              font = ("Times New Roman",35), fg = "ghostwhite").place(x=60,y=120)

win.mainloop()#giúp lặp lại các dòng code --> hiển thị giao diện, nếu không cửa sổ giao diện sẽ không được hiển thị.