# Ex 11 Project 6
# Paul Takemoto

import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Widgets for top frame
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter a distance in kilometers: ')
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)
        # Pack top frame widgets
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        # Widgets for middle frame
        self.descr_label = tkinter.Label(self.mid_frame, text='Converted to miles: ')
        # StringVar to associate with output
        self.value = tkinter.StringVar()  # StringVar to associate with output
        self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.value)  # Label associated with StringVar
        # Pack middle frame widgets
        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')

        # Button widgets for bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        # Pack bottom frame widgets
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = kilo * 0.6214  # Converts km to mi

        self.value.set(str(miles))  # Converts value to string and stores in StringVar

if __name__ == '__main__':
    kilo_conv = KiloConverterGUI()
