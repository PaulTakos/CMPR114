# Ex 11 Project 2
# Paul Takemoto

import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('300x100')

        self.label = tkinter.Label(self.main_window, text='Takemoto')
        self.label.pack()
        self.label = tkinter.Label(self.main_window, text='Paul')
        self.label.pack()
        self.label = tkinter.Label(self.main_window, text='23')
        self.label.pack()

        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()
