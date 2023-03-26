import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    ERROR = 'Error.TLabel'
    SUCCESS = 'Success.TLabel'

    def __init__(self):
        super().__init__()
        self.title('Thay đổi mật khẩu')
        self.geometry("300x130")

        self.password_var = tk.StringVar()
        self.confirm_password_var = tk.StringVar()

        self.confirm_password_var.trace('w', self.validate) # trace: "w" gọi lại

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.create_widgets()

    def create_widgets(self):
        # Tạo một widget
        padding = {'padx': 5, 'pady': 5, 'sticky': tk.W}
        # message
        self.message_label = ttk.Label(self)
        self.message_label.grid(column=0, row=0, columnspan=3, **padding)

        # password
        ttk.Label(self, text='Mật khẩu mới:').grid(column=0, row=1, **padding)

        password_entry = ttk.Entry(self, textvariable=self.password_var, show='*')
        password_entry.grid(column=1, row=1, **padding)
        password_entry.focus()

        # Confirm password
        ttk.Label(self, text='Xác nhận lại mật khẩu:').grid(
            column=0, row=2, **padding)

        confirm_password = ttk.Entry(
            self, textvariable=self.confirm_password_var, show='*')
        confirm_password.grid(column=1, row=2, **padding)
        confirm_password.focus()

    def set_message(self, message, type=None):

        self.message_label['text'] = message
        if type:
            self.message_label['style'] = type

    def validate(self, *args):

        password = self.password_var.get()
        confirm_password = self.confirm_password_var.get()

        if confirm_password == password:
            return self.set_message("Mật khẩu xác nhận lại đúng", self.SUCCESS)

        if password.startswith(confirm_password):
            self.set_message('Tiếp tục nhập!')

        self.set_message("Mật khẩu nhập lại sai", self.SUCCESS)

if __name__ == "__main__":
    app = App()
    app.mainloop()