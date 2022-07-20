import os
import sys
import json
import tkinter as tk
from tkinter import *
from tkinter import font as tkfont

class MainFrame(tk.Tk):


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.titlefont = tkfont.Font(family = "Verdana", size = 12, weight = "bold", slant = "roman")

        container = tk.Frame()
        container.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)




        self.listing = {}

        for p in (MainMenu, QuizPage, LoginPage, WelcomeScreen):
            page_name = p.__name__
            frame = p(parent = container, controller = self)
            frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
            self.listing[page_name] = frame

    def up_frame(self, page_name):
        page = self.listing[page_name]
        page.tkraise()
        # for testing
        if page_name != "MainMenu":
            print("Raised {} page".format(page_name))

        elif page_name == "MainMenu":
            print("Returned to {}".format(page_name))
    



class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        label = tk.Label(self, text = "Welcome to the quiz \n", font = controller.titlefont)
        label.pack()

        label = tk.Label(self, text = "Select a quiz below to start: \n", font = controller.titlefont)
        label.pack()

        mathbtn = tk.Button(self, text = "Maths", command= lambda *args : [controller.up_frame("QuizPage"), controller.subject_select(1)])
        mathbtn.pack()

        engbtn = tk.Button(self, text = "English", command= lambda: controller.up_frame("QuizPage"))
        engbtn.pack()

        phybtn = tk.Button(self, text = "Physics", command= lambda: controller.up_frame("QuizPage"))
        phybtn.pack()

        sosbtn = tk.Button(self, text = "Social Studies", command= lambda: controller.up_frame("QuizPage"))
        sosbtn.pack()        





class QuizPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.q_no=0
         
        self.display_title()
        self.display_question()
        self.opt_selected=tk.IntVar()
        
        self.opts=self.radio_buttons()
        self.display_options()
         
        
        self.buttons()
         
        
        self.data_size=len(question)
         
        
        self.correct=0

    def exit(self):
        gui.quit()

    def check_ans(self, q_no):
         
        
        if self.opt_selected.get() == answer[q_no]:
            
            return True   


    def next_btn(self):
         
        
        if self.check_ans(self.q_no):
             
            
            self.correct += 1
         
        
        self.q_no += 1
         
        # if all questions have been answered, the program will end
        if self.q_no==self.data_size:
             
            
            # self.display_result()
             
            
            self.exit()
        else:
            
            self.display_question()
            self.display_options()
 

    def buttons(self):
        next_button = tk.Button(self, text="Next",command=self.next_btn,
        width=10,bg="blue",fg="black",font=("ariel",16,"bold"))
         
        
        next_button.pack()
         

        quit_button = tk.Button(self, text="Quit", command=self.exit,
        width=5,bg="black", fg="black",font=("ariel",16," bold"))
         
        
        quit_button.pack()

    def display_options(self):
        val=0
         
        
        self.opt_selected.set(0)
         
        
        
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1

    def display_question(self):

        q_no = tk.Label(self, text=question[self.q_no], width=60,
        font=( 'ariel' ,16, 'bold' ))
         
        
        q_no.place(x=5, y=20)

    def display_title(self):
         
        
        title = tk.Label(self, text="Revision Quiz",
        width=74, bg="white",fg="black", font=("ariel", 20, "bold"))
         
        
        title.pack()

    def radio_buttons(self):
         
        
        q_list = []
         
        
        y_pos = 150
         
        
        while len(q_list) < 4:
             
            
            radio_btn = tk.Radiobutton(self,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("ariel",14), pady=10, padx=10)
             
            
            q_list.append(radio_btn)
             
            
            radio_btn.pack(anchor=W)
             
            
            y_pos += 40
         
        
        return q_list
 

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text = "This is the login page \n", font = controller.titlefont)
        label.pack()

        bou = tk.Button(self, text = "Enter quiz", command= lambda: controller.up_frame("MainMenu"))
        bou.pack()



class WelcomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text = "Press button to enter quiz \n", font = controller.titlefont)
        label.pack()

        bou = tk.Button(self, text = "Enter quiz", command= lambda: controller.up_frame("LoginPage"))
        bou.pack()




with open (os.path.join(sys.path[0], 'questionsbackup.json'), "r") as f:
    data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data['answer'])


gui = MainFrame()
gui.mainloop()


