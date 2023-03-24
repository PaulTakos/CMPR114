# HW 6 Project 2
# Author: Paul Takemoto

import tkinter as tk  # tkinter module
from tkinter import messagebox  # imports messagebox display

# This program reads numbers from a file and displays the sum on the GUI.
# GUI: User clicks 'Run' button and numbers from file will be added, or user clicks 'Quit' to end

win = tk.Tk()  # creates window interface
win.geometry("300x100")  # dimensions in pixels
win.title("Sum calculation")

#
def run():
    total = 0.0
    num_file = open('numbers.txt', 'r')  # Opens a file for reading

    # Uses a while loop to read each line from file, cast each one to float, and add to total
    line = num_file.readline().rstrip()
    while line != '':
        total += float(line)
        line = num_file.readline().rstrip()

    TTL.set(str(total))  # Sets total to be displayed on GUI
    num_file.close()

def quit():
    messagebox.showinfo('Information', 'Thank you.')
    win.destroy()  # Closes interface

lbl1 = tk.Label(win, text='Total from file: ').grid(column=0, row=0)  # Label widget for total

# Widget that displays the sum on GUI
TTL = tk.StringVar()
txtTotal = tk.Label(win, textvariable=TTL).grid(column=1, row=0)

# GUI buttons to run (add numbers from file) and quit GUI
run_button = tk.Button(win, text='Run', command=run).grid(column=0, row=2)
quit_button = tk.Button(win, text='Quit', command=quit).grid(column=1, row=2)

win.mainloop()
