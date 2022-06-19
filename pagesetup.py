import tkinter as tk
from tkinter import ttk


LARGETEXT = ("Verdana", 35)
BODYTEXT = ("Verdana", 20)
SMALLTEXT = ("Verdana", 15)

class app(tk.Tk):
     

    def __init__(self, *args, **kwargs):
         
        tk.Tk.__init__(self, *args, **kwargs)
         
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  

        self.frames = {} 
  
        for F in (StartPage, Page1, Page2):
  
            frame = F(container, self)

            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Startpage", font = LARGEFONT)
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Page 1",
        command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Page 2",
        command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)




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