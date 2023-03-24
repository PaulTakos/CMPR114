# HW 6 Project 2
# Author: Paul Takemoto

import tkinter as tk  # tkinter module
from tkinter import messagebox  # imports messagebox display

win = tk.Tk()  # creates window interface
win.geometry("300x100")  # dimensions in pixels
win.title("Sum calculation")

def run():
    total = 0.0
    num_file = open('numbers.txt', 'r')
    line = num_file.readline().rstrip()
    while line != '':
        total += float(line)
        line = num_file.readline().rstrip()
    TTL.set(str(total))
    num_file.close()

def quit():
    messagebox.showinfo('Information', 'Thank you.')
    win.destroy()

lbl1 = tk.Label(win, text='Total from file: ').grid(column=0, row=0)

TTL = tk.StringVar()
txtTotal = tk.Label(win, textvariable=TTL).grid(column=1, row=0)

run_button = tk.Button(win, text='Run', command=run).grid(column=0, row=2)
quit_button = tk.Button(win, text='Quit', command=quit).grid(column=1, row=2)

win.mainloop()
