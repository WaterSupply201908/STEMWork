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

        self.result_string = ctk.StringVar(value='0')
        self.formula_string = ctk.StringVar(value='test')

        self.create_widgets()

        self.mainloop()

    def create_widgets(self) :
        main_font = ctk.CTkFont(family=FONT, size=NORMAL_FONT_SIZE)
        result_font = ctk.CTkFont(family=FONT, size=OUTPUT_FONT_SIZE)

        OutputLabel(self, 0, 'SE', main_font, self.formula_string)
        OutputLabel(self, 1, 'E', result_font, self.result_string)

class OutputLabel(ctk.CTkLabel) :
    def __init__(self, parent, row, anchor, font, string_var) :
        super().__init__(master=parent, font=font, textvariable=string_var)
        self.grid(column=0, columnspan=4, row=row, sticky=anchor, padx=10)

# Main program
Calculator(darkdetect.isDark())
