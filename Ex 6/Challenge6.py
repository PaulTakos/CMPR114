# Exercise 6 Challenge 6
# Author: Paul Takemoto

import tkinter as tk  # tkinter module
from tkinter import messagebox  # imports messagebox display

win = tk.Tk()  # creates window interface
win.geometry("300x250")  # dimensions in pixels
win.title("Adder")

lblNum1 = tk.Label(win, text='Enter 1st number: ').grid(column=0, row=0)
lblNum2 = tk.Label(win, text='Enter 2nd number: ').grid(column=0, row=1)
lblNum3 = tk.Label(win, text='Enter 3rd number: ').grid(column=0, row=2)
lblTotal = tk.Label(win, text='Total: ').grid(column=0, row=3)
lblAvg = tk.Label(win, text='Average: ').grid(column=0, row=4)

def write():
    text_file = open('Sum.txt', 'w')
    line1 = text_file.write('\nThe three numbers are ' + str(N1.get()) + ', ' + str(N2.get()) + ', and '
                            + str(N3.get()))
    line2 = text_file.write('\nThe total is ' + str(TTL.get()))
    line3 = text_file.write('\nThe average is ' + str(AVG.get()))

    text_file.close()
    messagebox.showinfo('Information', 'Data recorded.')

def quit():
    messagebox.showinfo('Information', 'Thank you.')
    win.destroy()  # closes interface

def add():
    num1 = float(N1.get())
    num2 = float(N2.get())
    num3 = float(N3.get())

    total = num1 + num2 + num3
    average = total / 3

    TTL.set(str(total))
    AVG.set(str(average))

N1 = tk.StringVar()
txtNum1 = tk.Entry(win, width=12, textvariable=N1).grid(column=1, row=0)
N2 = tk.StringVar()
txtNum2 = tk.Entry(win, width=12, textvariable=N2).grid(column=1, row=1)
N3 = tk.StringVar()
txtNum3 = tk.Entry(win, width=12, textvariable=N3).grid(column=1, row=2)


TTL = tk.StringVar()
txtTotal = tk.Label(win, textvariable=TTL).grid(column=1, row=3)
AVG = tk.StringVar()
txtAvg = tk.Label(win, textvariable=AVG).grid(column=1, row=4)

btnAdd = tk.Button(win, text='Calculate', command=add).grid(column=0, row=6)
btnQuit = tk.Button(win, text='Quit', command=quit).grid(column=1, row=6)
btnWrite = tk.Button(win, text='Transfer', command=write).grid(column=2, row=6)

win.mainloop()
