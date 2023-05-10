# Ex 11 Project 5
# Paul Takemoto

import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Widgets for top frame
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter a distance in kilometers: ')
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)
        # Pack top frame widgets
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        # Button widgets for bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        # Pack bottom frame widgets
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())

        # Converts km to mi
        miles = kilo * 0.6214

        tkinter.messagebox.showinfo('Results', str(kilo) + ' km is equal to ' + str(miles) + ' miles.')

if __name__ == '__main__':
    kilo_conv = KiloConverterGUI()
