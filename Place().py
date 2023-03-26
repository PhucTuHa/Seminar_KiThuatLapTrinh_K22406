from tkinter import *
#Tạo cửa sổ giao diện với biến "win"
win = Tk()
#để thay đổi tên tiêu đề tk mặc định của cửa sổ
win.title("HELLO")
#để thay đổi kích thước mặc định của cửa sổ hiển thị (250:width, 300:height)
win.geometry("250x300")
#thay đổi background(màu nền của cửa sổ hiển thị)
win["bg"] = "powder blue"

'''gán thuộc tính topmost cho win(để cửa sổ luôn hiện lên trên các cửa sổ khác), 
nếu là False thì không cần dùng vì mặc định đã là False'''
win.attributes("-topmost", True)

#Tạo Label
name=Label(win, text = "Name",bg = "lightcoral",font = ("Times New Roman",12), fg = "ghostwhite")
#name.place(x=60,y=120) :sd dòng code này thì phía trên không dùng '.place'
name.pack()
'''Để label hiển thị thì cần sử dụng pack hoặc sử dụng place để xác định tọa độ hiển thị.'''

win.mainloop() #giúp lặp lại các dòng code --> hiển thị giao diện, nếu không cửa sổ giao diện sẽ không được hiển thị.
'''Khi tạo sẽ hiện 1 cửa sổ với titile mặc định là tk và một kích thước mặc định. 
Khi muốn chạy lại code phải tắt cửa sổ đã chạy,nếu không các dòng code phía trong sẽ không được chạy'''
