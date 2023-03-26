from tkinter import *
#Tạo cửa sổ giao diện với biến "win"
win = Tk()

#để thay đổi tên tiêu đề tk mặc định của cửa sổ
win.title("CHOICE")
#để thay đổi kích thước mặc định của cửa sổ hiển thị (400:width, 500:height)
win.geometry("400x500")
#thay đổi background(màu nền của cửa sổ hiển thị)
win["bg"] = "lightcoral"

#Tạo Label
label=Label(win, text="Các đồ cần mua", font=("Arial",11), bg="gainsboro").pack()
#Tạo listbox
listbox = Listbox(win)

#Thêm các phần tử vào listbox
listbox.insert(1, "Thịt")
listbox.insert(2, "Sữa")
listbox.insert(3, "Trứng")

#Đóng gói listbox để listbox được hiển thị ngoài cửa sổ
listbox.pack()
win.mainloop()#giúp lặp lại các dòng code --> hiển thị giao diện, nếu không cửa sổ giao diện sẽ không được hiển thị.