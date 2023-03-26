from tkinter import *
master = Tk()
master.geometry("400x400")
# Tạo menu chính
menu_bar = Menu(master)
# Thiết lập thuộc tính menu cho master
master.config(menu=menu_bar)

# Tạo các mục menu nhỏ cho menu chính
file_menu = Menu(menu_bar)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()

edit_menu = Menu(menu_bar)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_separator()

# Liên kết các menu nhỏ vào trong thanh menu chính
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

master.mainloop()

