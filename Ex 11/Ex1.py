# Ex 11 Project 1
# Paul Takemoto

import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title('My First GUI')
        self.main_window.geometry('300x100')

        tkinter.mainloop()

my_gui = MyGUI()
