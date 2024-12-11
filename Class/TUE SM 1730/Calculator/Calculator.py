import customtkinter as ctk
import darkdetect

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

        self.rowconfigure()

        self.mainloop()

# Main program
Calculator(darkdetect.isDark())
