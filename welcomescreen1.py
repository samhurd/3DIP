from tkinter import *

root =Tk()
root.title('General Revision Quiz')
root.geometry('960x720')
bottomframe = Frame(root, bg = "blue")
bottomframe.pack(side = BOTTOM)



label = Label (bottomframe, text = "Bottom Frame", height = "10", width = "960").pack()



label = Label (root, 
    text = "Hello World",
    fg = "#ADD8E6",
    bg = "#FFD580",
    height = "10",
    width = "960",
    font = "Helvetica 16 bold italic").pack()









button = Button (root, text = "Test Button")
button.pack(padx = 5, pady = 5)

root.mainloop()