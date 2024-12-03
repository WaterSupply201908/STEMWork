# BMI : Body Mass Index

import customtkinter as ctk

class App(ctk.CTk) :
    def __init__(self) :
        super().__init__(fg_color='Green')

        self.title('BMI')
        self.geometry('400x400')
        self.resizable(False, False)

        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')

        ResultText(self)

        self.mainloop()

class ResultText(ctk.CTkLabel) :
    def __init__(self, parent) :
        font = ctk.CTkFont(family='Calibri', size=150, weight='bold')
        super().__init__(master=parent, text='22.5', font=font)

        self.grid(column=0, row=0, rowspan=2, sticky='nsew')

# Main program
if __name__ == '__main__' :
    App()