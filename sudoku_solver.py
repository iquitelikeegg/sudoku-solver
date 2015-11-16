"""Sudoku solver"""

from Tkinter import *

class Application:

    def createWidgets(self):
        self.wrapper = Frame(self.frame, bg="grey")
        self.wrapper.pack(fill=BOTH, expand=1, ipadx=50, ipady=50)

        self.container = Frame(self.wrapper, width=650, height=650, bg="white")
        self.container.pack()

    def __init__(self, master):

        self.frame = Frame(master)
        self.frame.pack(fill=BOTH, expand=1)
        self.createWidgets()


root = Tk()

app = Application(root)

root.mainloop()
root.destroy()
