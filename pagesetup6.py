import os
import sys
import json

from tkinter import *



class App():
    def __init__():
        mylabel = Label(text="")
        mylabel.pack()








gui = Tk() 

gui.geometry("960x720")


gui.title("Revision quiz")

with open (os.path.join(sys.path[0], 'questionsbackup.json'), "r") as f:
    data = json.load(f)

quiz = App()
 

gui.mainloop()
 
