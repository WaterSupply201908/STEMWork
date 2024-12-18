import customtkinter as ctk
import darkdetect
from Setting import *

class Calculator(ctk.CTk) :
    def __init__(self, is_dark) :
        super().__init__(fg_color=('White', 'Black'))

        if is_dark :
            ctk.set_appearance_mode('dark')
        else :
            ctk.set_appearance_mode('light')

        self.geometry('400x700')
        self.resizable(False, False)
        self.title('Calculator')

        self.rowconfigure(list(range(MAIN_ROWS)), weight=1, uniform='a')
        self.columnconfigure(list(range(MAIN_COLUMNS)), weight=1, uniform='a')

        self.create_widgets()
        
        self.mainloop()

    def create_widgets(self) :
        OutputLabel(self, 0)
        OutputLabel(self, 1)

class OutputLabel(ctk.CTkLabel) :
    def __init__(self, parent, row) :
        super().__init__(master=parent, text='123')
        self.grid(column=0, columnspan=4, row=row)

# Main program
Calculator(darkdetect.isDark())
