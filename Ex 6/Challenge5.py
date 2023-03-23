# Exercise 6 Challenge 5
# Author: Paul Takemoto

import tkinter as tk  # tkinter module
from tkinter import messagebox  # imports messagebox display

win = tk.Tk()  # creates window interface
win.geometry("300x250")  # dimensions in pixels
win.title("Customer Information")

lblLastName = tk.Label(win, text='Enter last name: ').grid(column=0, row=0)
lblFirstName = tk.Label(win, text='Enter first name: ').grid(column=0, row=1)
# Adds labels for street address, city, state, zipcode
lblStreetAddress = tk.Label(win, text='Enter street address: ').grid(column=0, row=2)
lblCity = tk.Label(win, text='Enter city: ').grid(column=0, row=3)
lblState = tk.Label(win, text='Enter state: ').grid(column=0, row=4)
lblZipcode = tk.Label(win, text='Enter zipcode: ').grid(column=0, row=5)

def write():
    text_file = open('Customers.txt', 'a')
    content1 = text_file.write('\nConfirmation: ' + str(LN.get()) + ', ' + str(FN.get()))
    # Adds street address, city, state, and zipcode to file along w/ name
    content2 = text_file.write('\n' + str(SA.get()))
    content3 = text_file.write('\n' + str(CT.get()) + ', ' + str(ST.get()) + ' ' + str(ZP.get()))
    text_file.close()
    messagebox.showinfo('Information', 'Data recorded.')

def quit():
    messagebox.showinfo('Information', 'Thank you.')
    win.destroy()  # closes interface

def submit():
    # Added street address, city, state, and zipcode to display
    messagebox.showinfo('Information', 'Entered: ' + LN.get() + ', ' + FN.get() + '\n' +
                        SA.get() + '\n' + CT.get() + ', ' + ST.get() + ' ' + ZP.get())  # displays info

# LN = lastname, FN = firstname, SA = street address, CT = city, ST = state, ZP = zipcode
LN = tk.StringVar()
txtLastName = tk.Entry(win, width=12, textvariable=LN).grid(column=1, row=0)
FN = tk.StringVar()
txtFirstName = tk.Entry(win, width=12, textvariable=FN).grid(column=1, row=1)
SA = tk.StringVar()
txtStreetAddress = tk.Entry(win, width=12, textvariable=SA).grid(column=1, row=2)
CT = tk.StringVar()
txtCity = tk.Entry(win, width=12, textvariable=CT).grid(column=1, row=3)
ST = tk.StringVar()
txtState = tk.Entry(win, width=12, textvariable=ST).grid(column=1, row=4)
ZP = tk.StringVar()
txtZipcode = tk.Entry(win, width=12, textvariable=ZP).grid(column=1, row=5)

btnSubmit = tk.Button(win, text='Submit', command=submit).grid(column=0, row=6)
btnQuit = tk.Button(win, text='Quit', command=quit).grid(column=1, row=6)
btnWrite = tk.Button(win, text='Transfer', command=write).grid(column=2, row=6)

win.mainloop()
