from calendar import weekday
import os
import sys
import json
import tkinter as tk
from tkinter import *
from tkinter import font as tkfont
from tkinter import messagebox


class MainFrame(tk.Tk):


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.headingfont = tkfont.Font(family = "Verdana", size = 12, weight = "bold", slant = "roman")
        self.titlefont = tkfont.Font(family = "Verdana", size = 20, weight = "bold", slant = "roman")
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


        label = tk.Label(self, text = "Welcome to the quiz \n", font = controller.headingfont)
        label.pack()

        label = tk.Label(self, text = "Select a quiz below to start: \n", font = controller.headingfont)
        label.pack()

        mathbtn = tk.Button(self, text = "Maths", command= lambda *args: [controller.up_frame("QuizPage"), subject_select(1), print(subject)])
        mathbtn.pack()

        phybtn = tk.Button(self, text = "Physics", command= lambda *args: [controller.up_frame("QuizPage"), subject_select(2), print(subject)])
        phybtn.pack()

        engbtn = tk.Button(self, text = "Maths", command= lambda *args: [controller.up_frame("QuizPage"), subject_select(3), print(subject)])
        engbtn.pack()

        sosbtn = tk.Button(self, text = "Social Studies", command= lambda *args: [controller.up_frame("QuizPage"), subject_select(4), print(subject)])
        sosbtn.pack()        




class QuizPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.q_no=0
         
        self.correct=0
        self.display_title()
        self.display_question()
        self.opt_selected=tk.IntVar()
        
        self.opts=self.radio_buttons()
        self.display_options()

        self.buttons()
         
        self.data_size=len(question)

        quit_button = tk.Button(self, text="Quit", command= lambda: controller.up_frame("MainMenu"),
        width=5,bg="black", fg="black",font=("ariel",16," bold"))
         
        
        quit_button.pack()
         
        

    def check_ans(self, q_no):
         
        
        if self.opt_selected.get() == answer[q_no]:
            
            return True   


    def next_btn(self):
         
        
        if self.check_ans(self.q_no):
             
            
            self.correct += 1
         
        
        self.q_no += 1
         
        # if all questions have been answered, the program will end
        if self.q_no==self.data_size:
             
            
            self.display_result()
             
            
            MainFrame.up_frame("MainMenu")
        else:
            
            self.display_question()
            self.display_options()
 

    def display_result(self):
         
        
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
         
        
        scorepercentage = int(self.correct / self.data_size * 100)
        result = f"Score: {scorepercentage}%"
         
        
        messagebox.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    def buttons(self):
        next_button = tk.Button(self, text="Next",command=self.next_btn,
        width=10,bg="blue",fg="black",font=("ariel",16,"bold"))
         
        
        next_button.pack()
         



    def display_options(self):
        val=0
         
        
        self.opt_selected.set(0)
         
        
        
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1

    def display_question(self):

        q_no = tk.Label(self, text=question[self.q_no], width=60,
        font=( 'verdana' ,18, 'bold' ))
         
        
        q_no.place(x=5, y=20)

    def display_title(self):
         
        
        title = tk.Label(self, text="Revision Quiz",
        width=74, bg="white",fg="black", font=("verdana", 20, "bold"))
         
        
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

        label = tk.Label(self, text = "This is the login page \n", font = controller.headingfont)
        label.pack()

        bou = tk.Button(self, text = "Enter quiz", command= lambda: controller.up_frame("MainMenu"))
        bou.pack()



class WelcomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text = "\n Welcome to the Quiz! \n", font = controller.titlefont)
        label.pack()

        self.after(300, lambda: controller.up_frame("LoginPage"))  










def subject_select(value):
    global subject
    subject = value



with open (os.path.join(sys.path[0], 'quizquestions.json'), "r") as f:
    data = json.load(f)


question = (data['mathsquestions'])
options = (data['mathsoptions'])
answer = (data['mathsanswers'])


phyquestion = (data['phyquestions'])
phyoptions = (data['phyoptions'])
phyanswer = (data['phyanswers'])


# question = (data['question'])
# options = (data['options'])
# answer = (data['answer'])  

# question = (data['question'])
# options = (data['options'])
# answer = (data['answer'])  

subject = 1








variable = 0






gui = MainFrame()

gui.mainloop()
gui.title = "BDSC QUIZ"

# Make initial window that appears before all of this, to choose the subject, there is not really another way??


# TRy to find a way to return to the main menu after the quiz is done