import tkinter as tk

from tkinter import font as tkfont


class MainFrame(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.titlefont = tkfont.Font(family = "Verdana", size = 12, weight = "bold", slant = "roman")


        container = tk.Frame()
        container.grid(row=0, column=0, sticky='nsew')

        #id of the user, will be used later in login page
        self.id =tk.StringVar()
        self.id.set("John Appleseed")

        self.listing = {}
        for p in (WelcomePage, PageOne):
            page_name = p.__name__
            frame = p(parent = container, controller = self)
            frame.grid(row=0, column=0, sticky='nsew')
            self.listing[page_name] = frame

    def up_frame(self, page_name):
        page = self.listing[page_name]
        page.tkraise()

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id

        label = tk.Label(self, text = "Welcome page test \n" + controller.id.get(),
        font = controller.titlefont)
        label.pack()

        bou = tk.Button(self, text = "To page 1", command= lambda: controller.up_frame("PageOne"))
        bou.pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id

        label = tk.Label(self, text = "Page One test \n" + controller.id.get(),
        font = controller.titlefont)
        label.pack()

        bou = tk.Button(self, text = "To Main Menu", command= lambda: controller.up_frame("WelcomePage"))
        bou.pack()


if __name__ == '__main__':
    app = MainFrame()
    app.mainloop()