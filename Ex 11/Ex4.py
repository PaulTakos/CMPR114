# Ex 11 Project 4
# Paul Takemoto

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.__main_window = tkinter.Tk()

        self.my_button = tkinter.Button(self.__main_window, text='Click me!', command=self.do_something)
        self.my_button1 = tkinter.Button(self.__main_window, text='Click me!', command=self.do_something1)
        self.my_button2 = tkinter.Button(self.__main_window, text='Click me!', command=self.do_something2)
        # Quit button
        self.quit_button = tkinter.Button(self.__main_window, text='Quit', command=self.__main_window.destroy)

        # Pack buttons
        self.my_button.pack()
        self.my_button1.pack()
        self.my_button2.pack()
        self.quit_button.pack()

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'Amazing!')

    def do_something1(self):
        tkinter.messagebox.showinfo('Response', 'You can do this!')

    def do_something2(self):
        tkinter.messagebox.showinfo('Response', 'Great!')

if __name__ == '__main__':
    my_gui = MyGUI()
