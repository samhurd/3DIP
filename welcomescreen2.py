import tkinter as tk
from tkinter import ttk










app = app()
app.title('General Revision Quiz')


app.mainloop()



# class app:
#     def __init__(self, master):

#         self.login()

#     def login(self):
#         for i in self.master.winfo_children():
#             i.destroy()
#         self.loginframe = Frame(self.master, width=300, height=300)
#         self.loginframe.pack()
#         self.reg_txt = ttk.Label(self.loginframe, text='login')
#         self.reg_txt.pack()
#         self.welcome_btn = ttk.Button(self.loginframe, text="Go to welcome", command=self.welcome)
#         self.welcome_btn.pack()
    
#     def welcome(self):
#         for i in self.master.winfo_children():
#             i.destroy()
#         self.homeframe = Frame(self.master, width=960, height=720, bg="blue")
#         self.homeframe.pack()
#         self.wel_txt = ttk.Label(self.homeframe, text = "Hello World")
#         self.wel_txt.pack()
#         self.login_btn = ttk.Button(self.homeframe, text="Go to Login", command=self.login)
#         self.login_btn.pack()