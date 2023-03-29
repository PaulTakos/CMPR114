# Exercise 7b Challenge 2
# Paul Takemoto

from tkinter import *

root = Tk()
root.geometry('180x200')

listbox = Listbox(root, width=40, height=10, selectmode=MULTIPLE)
# Adds listboxes of food items
listbox.insert(1, 'Sandwich')
listbox.insert(2, 'Burger')
listbox.insert(3, 'Pizza')
listbox.insert(4, 'French Fries')
listbox.insert(5, 'Hot Dogs')
listbox.insert(6, 'Cheeseburger')

def selected_item():
    for i in listbox.curselection():
        print(listbox.get(i))

btn = Button(root, text='Print Selected', command=selected_item)
btn.pack(side='bottom')
listbox.pack()

root.mainloop()
