import customtkinter as ctk
import darkdetect

class Calculator(ctk.CTk) :
    def __init__(self, is_dark) :
        super().__init__()

        if is_dark :
            ctk.set_appearance_mode('dark')
        else :
            ctk.set_appearance_mode('light')

        self.mainloop()

# Main program
Calculator(darkdetect.isDark())