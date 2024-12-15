# BMI : weight / (height^2)

import customtkinter as ctk

class App(ctk.CTk) :
    def __init__(self) :
        super().__init__(fg_color='Green')

        self.title('BMI')
        self.geometry('400x400')
        self.resizable(False, False)

        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')

        self.weight_float = ctk.DoubleVar(value=70)
        self.height_int = ctk.IntVar(value=180)
        self.bmi_string = ctk.StringVar()
        self.updateBMI()

        ResultText(self)
        WeightInput(self)
        HeightInput(self)
        UnitSwitcher(self)

        self.mainloop()

    def updateBMI(self) :
        pass

class ResultText(ctk.CTkLabel) :
    def __init__(self, parent) :
        font = ctk.CTkFont(family='Calibri', size=150, weight='bold')
        super().__init__(master=parent, text=22.5, font=font, text_color='White')

        self.grid(column=0, row=0, rowspan=2, sticky='nsew')

class WeightInput(ctk.CTkFrame) :
    def __init__(self, parent) :
        super().__init__(master=parent, fg_color='White')

        self.grid(column=0, row=2, sticky='nsew', padx=10, pady=10)

        self.rowconfigure(0, weight=1, uniform='b')
        self.columnconfigure(0, weight=2, uniform='b')
        self.columnconfigure(1, weight=1, uniform='b')
        self.columnconfigure(2, weight=3, uniform='b')
        self.columnconfigure(3, weight=1, uniform='b')
        self.columnconfigure(4, weight=2, uniform='b')

        font = ctk.CTkFont(family='Calibri', size=26)
        label = ctk.CTkLabel(self, text='70kg', text_color='Black', font=font)
        label.grid(row=0, column=2)

        minusButton = ctk.CTkButton(self, text='-', font=font, text_color='Black',
                                    fg_color='Light Gray', hover_color='Gray')
        minusButton.grid(row=0, column=0, sticky='ns', padx=8, pady=8)

        plusButton = ctk.CTkButton(self, text='+', font=font, text_color='Black',
                                    fg_color='Light Gray', hover_color='Gray')
        plusButton.grid(row=0, column=4, sticky='ns', padx=8, pady=8)

        smallPlusButton = ctk.CTkButton(self, text='+', font=font, text_color='Black',
                                    fg_color='Light Gray', hover_color='Gray')
        smallPlusButton.grid(row=0, column=3, padx=4, pady=4)

        smallMinusButton = ctk.CTkButton(self, text='-', font=font, text_color='Black',
                                    fg_color='Light Gray', hover_color='Gray')
        smallMinusButton.grid(row=0, column=1, padx=4, pady=4)

class HeightInput(ctk.CTkFrame) :
    def __init__(self, parent) :
        super().__init__(master=parent, fg_color='White')

        self.grid(column=0, row=3, sticky='nsew', padx=10, pady=10)

        slider = ctk.CTkSlider(master=self, 
                               button_color='Green', button_hover_color='Gray',
                               progress_color='Green', fg_color='Light Gray')
        slider.pack(side='left', fill='x', expand=True, padx=10, pady=10)

        outputText = ctk.CTkLabel(self, text='1.80', text_color='Black',
                                  font=ctk.CTkFont(family='Calibri', size=26))
        outputText.pack(side='left', padx=20)

class UnitSwitcher(ctk.CTkLabel) :
    def __init__(self, parent) :
        super().__init__(master=parent, text='metric',
                         text_color='Dark Green',
                         font=ctk.CTkFont(family='Calibri', size=18))

        self.place(relx=0.98, rely=0.01, anchor='ne')

# Main program
if __name__ == '__main__' :
    App()
