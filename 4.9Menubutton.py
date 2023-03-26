from tkinter import *
#Tạo cửa sổ giao diện với biến "win"
win = Tk()

#để thay đổi tên tiêu đề tk mặc định của cửa sổ
win.title("HI!")
#để thay đổi kích thước mặc định của cửa sổ hiển thị (400:width, 500:height)
win.geometry("400x500")
#thay đổi background(màu nền của cửa sổ hiển thị)
win["bg"] = "violet"

#Tạo menubutton
new_mnbt = Menubutton(win, text="ANIMALS", font=("Arial",12), bg="gainsboro",height=2,width=10)
#Tạo menu trong menubutton
new_mnbt.menu = Menu(new_mnbt,tearoff=0)
#Để hiển thị menu
new_mnbt["menu"] = new_mnbt.menu
#Thêm vào menubutton các menu cùng với checkbutton
new_mnbt.menu.add_checkbutton(label="Cat")
new_mnbt.menu.add_checkbutton(label="Mouse")
new_mnbt.menu.add_checkbutton(label="Dog")
new_mnbt.place(x=70,y=80)

win.mainloop()#giúp lặp lại các dòng code --> hiển thị giao diện, nếu không cửa sổ giao diện sẽ không được hiển thị.