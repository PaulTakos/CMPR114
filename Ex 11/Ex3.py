# Ex 11 Project 3
# Paul Takemoto

import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        # self.main_window.geometry('300x100')

        self.label1 = tkinter.Label(self.main_window, text='Hello world!', borderwidth=1, relief='solid')
        self.label2 = tkinter.Label(self.main_window, text='This is my GUI program.', borderwidth=2, relief='solid')
        self.label3 = tkinter.Label(self.main_window, text='You can do this.', borderwidth=1, relief='solid')
        self.label4 = tkinter.Label(self.main_window, text='This is great!', borderwidth=2, relief='solid')

        self.label1.pack(ipadx=20, ipady=20)
        self.label2.pack(ipadx=20, ipady=20)
        self.label3.pack(ipadx=20, ipady=20)
        self.label4.pack(ipadx=20, ipady=20)

        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()
