import customtkinter as ctk
import darkdetect
from Setting import *
from Button import Button, ImageButton, NumButton
from PIL import Image

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

        Button(
            parent=self,
            text=OPERATORS['clear']['text'],
            func=self.clear,
            col=OPERATORS['clear']['col'],
            row=OPERATORS['clear']['row'],
            font=main_font
            )

        Button(
            parent=self,
            text=OPERATORS['percent']['text'],
            func=self.percent,
            col=OPERATORS['percent']['col'],
            row=OPERATORS['percent']['row'],
            font=main_font
            )

        invert_image = ctk.CTkImage(
            light_image=Image.open(OPERATORS['invert']['image path']['dark']),
            dark_image=Image.open(OPERATORS['invert']['image path']['light'])
        )

        ImageButton(
            parent=self,
            text='',
            func=self.invert,
            col=OPERATORS['invert']['col'],
            row=OPERATORS['invert']['row'],
            image=invert_image
            )
        
    def clear(self) :
        print('clear')

    def percent(self) :
        print('percent')

    def invert(self) :
        print('invert')

class OutputLabel(ctk.CTkLabel) :
    def __init__(self, parent, row, anchor, font, string_var) :
        super().__init__(master=parent, font=font, textvariable=string_var)
        self.grid(column=0, columnspan=4, row=row, sticky=anchor, padx=10)

# Main program
Calculator(darkdetect.isDark())
