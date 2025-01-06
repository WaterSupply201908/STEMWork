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

        self.metric_bool = ctk.BooleanVar(value=True)
        self.weight_float = ctk.DoubleVar(value=65)
        self.height_int = ctk.IntVar(value=170)
        self.bmi_string = ctk.StringVar()
        self.updateBMI()

        self.weight_float.trace('w', self.updateBMI)
        self.height_int.trace('w', self.updateBMI)
        self.metric_bool.trace('w', self.change_units)

        ResultText(self, self.bmi_string)
        self.weight_input = WeightInput(self, self.weight_float, self.metric_bool)
        self.height_input = HeightInput(self, self.height_int, self.metric_bool)
        UnitSwitcher(self, self.metric_bool)

        self.mainloop()

    def updateBMI(self, *args) :
        weight_kg = self.weight_float.get()
        height_m = self.height_int.get() / 100
        bmi_result = round(weight_kg / height_m ** 2, 2)
        self.bmi_string.set(bmi_result)

    def change_units(self, *args) :
        self.height_input.update_text(self.height_int.get())
        self.weight_input.update_weight()

class ResultText(ctk.CTkLabel) :
    def __init__(self, parent, bmi_string) :
        font = ctk.CTkFont(family='Calibri', size=150, weight='bold')
        super().__init__(master=parent, text='22.5', font=font, text_color='White', textvariable=bmi_string)

        self.grid(column=0, row=0, rowspan=2, sticky='nsew')

class WeightInput(ctk.CTkFrame) :
    def __init__(self, parent, weight_float, metric_bool) :
        super().__init__(master=parent, fg_color='White')

        self.grid(column=0, row=2, sticky='nsew', padx=10, pady=10)

        self.weight_float = weight_float
        self.metric_bool = metric_bool
        self.output_string = ctk.StringVar()
        self.update_weight()

        self.rowconfigure(0, weight=1, uniform='b')
        self.columnconfigure(0, weight=2, uniform='b')
        self.columnconfigure(1, weight=1, uniform='b')
        self.columnconfigure(2, weight=3, uniform='b')
        self.columnconfigure(3, weight=1, uniform='b')
        self.columnconfigure(4, weight=2, uniform='b')

        font = ctk.CTkFont(family='Calibri', size = 26)
        label = ctk.CTkLabel(self, textvariable=self.output_string, text='70kg', text_color='Black', font=font)
        label.grid(row=0, column=2)

        minusButton = ctk.CTkButton(self, command=lambda:self.update_weight(('minus', 'large')),
                                    text='-', font=font, text_color='Black',
                                    fg_color='Light Gray', hover_color='Gray')
        minusButton.grid(row=0, column=0, sticky='ns', padx=8, pady=8)

        plusButton = ctk.CTkButton(self, command=lambda:self.update_weight(('plus', 'large')),
                                    text='+', font=font, text_color='Black',
                                    fg_color='Light Gray', hover_color='Gray')
        plusButton.grid(row=0, column=4, sticky='ns', padx=8, pady=8)

        smallPlusButton = ctk.CTkButton(self, command=lambda:self.update_weight(('plus', 'small')),
                                    text='+', font=font, text_color='Black',
                                    fg_color='Light Gray', hover_color='Gray')
        smallPlusButton.grid(row=0, column=3, padx=4, pady=4)

        smallMinusButton = ctk.CTkButton(self, command=lambda:self.update_weight(('minus', 'small')),
                                    text='-', font=font, text_color='Black',
                                    fg_color='Light Gray', hover_color='Gray')
        smallMinusButton.grid(row=0, column=1, padx=4, pady=4)

    def update_weight(self, info=None) :
        if info :
            amount = 0

            if self.metric_bool.get() :
                if info[1] == 'large' :
                    amount = 1
                else :
                    amount = 0.1
            else :
                if info[1] == 'large' :
                    amount = 0.453592
                else :
                    amount = 0.453592 / 16

            if info[0] == 'plus' :
                self.weight_float.set(self.weight_float.get() + amount)
            else :
                self.weight_float.set(self.weight_float.get() - amount)

        if self.metric_bool.get() :
            self.output_string.set(f'{round(self.weight_float.get(), 1)}kg')
        else :
            raw = self.weight_float.get() * 2.20462 * 16
            pounds, ounces = divmod(raw, 16)
            self.output_string.set(f'{int(pounds)}lb {int(ounces)}oz')

class HeightInput(ctk.CTkFrame) :
    def __init__(self, parent, height_int, metric_bool) :
        super().__init__(master=parent, fg_color='White')

        self.grid(column=0, row=3, sticky='nsew', padx=10, pady=10)

        self.metric_bool = metric_bool

        slider = ctk.CTkSlider(master=self,
                               command=self.update_text,
                               button_color='Green',
                               button_hover_color='Gray',
                               progress_color='Green',
                               fg_color='Light Gray',
                               variable=height_int,
                               from_=100,
                               to=250)
        slider.pack(side='left', fill='x', expand=True, padx=10, pady=10)

        self.output_string = ctk.StringVar()
        self.update_text(height_int.get())

        outputText = ctk.CTkLabel(self, textvariable=self.output_string, text_color='Black',
                                  font=ctk.CTkFont(family='Calibri', size=26))
        outputText.pack(side='left', padx=20)

    def update_text(self, amount) :
        if self.metric_bool.get() :
            text_string = str(int(amount))
            m = text_string[0]
            cm = text_string[1:]
            self.output_string.set(f'{m}.{cm}m')
        else :
            feet, inches = divmod(amount / 2.54, 12)
            self.output_string.set(f'{int(feet)}\'{int(inches)}\"')

class UnitSwitcher(ctk.CTkLabel) :
    def __init__(self, parent, metric_bool) :
        super().__init__(master=parent, text='Metric',
                         text_color='Dark Green',
                         font=ctk.CTkFont(family='Calibri', size=18))

        self.place(relx=0.98, rely=0.01, anchor='ne')

        self.metric_bool = metric_bool
        self.bind('<Button>', self.change_units)

    def change_units(self, event) :
        self.metric_bool.set(not self.metric_bool.get())

        if self.metric_bool.get() :
            self.configure(text='Metric')
        else :
            self.configure(text='Imperial')

# Main program
if __name__ == '__main__' :
    App()
