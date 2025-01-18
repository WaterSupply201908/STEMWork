# BMI : Body Mass Index
# bmi = weight (kg) / (height (m) * height (m))

import customtkinter as ctk


class App(ctk.CTk):

  def __init__(self):
    super().__init__(fg_color='green')

    self.title('BMI')
    self.geometry('400x400')
    self.resizable(False, False)

    self.columnconfigure(0, weight=1)
    self.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')

    self.height_int = ctk.IntVar(value=170)
    self.weight_float = ctk.DoubleVar(value=70.0)
    self.bmi_string = ctk.StringVar()
    self.update_bmi()

    self.height_int.trace('w', self.update_bmi)
    self.weight_float.trace('w', self.update_bmi)

    ResultText(self, self.bmi_string)
    WeightInput(self, self.weight_float)
    HeightInput(self, self.height_int)
    UnitSwitcher(self)

    self.mainloop()

  def update_bmi(self, *args):
    height_m = self.height_int.get() / 100
    weight_kg = self.weight_float.get()
    bmi_result = round(weight_kg / (height_m * height_m), 2)
    self.bmi_string.set(str(bmi_result))


class ResultText(ctk.CTkLabel):

  def __init__(self, parent, bmi_string):
    font = ctk.CTkFont(family='Calibri', size=150, weight='bold')
    super().__init__(master=parent,
                     text='22.5',
                     font=font,
                     text_color='white',
                     textvariable=bmi_string)

    self.grid(column=0, row=0, rowspan=2, sticky='nsew')


class WeightInput(ctk.CTkFrame):

  def __init__(self, parent, weight_float):
    super().__init__(master=parent, fg_color='White')

    self.grid(column=0, row=2, sticky='nsew', padx=10, pady=10)

    self.weight_float = weight_float
    self.output_string = ctk.StringVar()

    self.rowconfigure(0, weight=1, uniform='b')
    self.columnconfigure(0, weight=2, uniform='b')
    self.columnconfigure(1, weight=1, uniform='b')
    self.columnconfigure(2, weight=3, uniform='b')
    self.columnconfigure(3, weight=1, uniform='b')
    self.columnconfigure(4, weight=2, uniform='b')

    font = ctk.CTkFont(family='Calibri', size=26)
    label = ctk.CTkLabel(self, text='70kg', text_color='black', font=font)
    label.grid(row=0, column=2)

    minus_button = ctk.CTkButton(self,
                                 command=lambda: self.update_weight(
                                     ('minus', 'large')),
                                 text='-',
                                 font=font,
                                 text_color='black',
                                 fg_color='light gray',
                                 hover_color='gray')
    minus_button.grid(row=0, column=0, sticky='ns', padx=8, pady=8)

    plus_button = ctk.CTkButton(self,
                                command=lambda: self.update_weight(
                                    ('plus', 'large')),
                                text='+',
                                font=font,
                                text_color='black',
                                fg_color='light gray',
                                hover_color='gray')
    plus_button.grid(row=0, column=4, sticky='ns', padx=8, pady=8)

    small_plus_button = ctk.CTkButton(self,
                                      command=lambda: self.update_weight(
                                          ('plus', 'small')),
                                      text='+',
                                      font=font,
                                      text_color='black',
                                      fg_color='light gray',
                                      hover_color='gray')
    small_plus_button.grid(row=0, column=3, padx=4, pady=4)

    small_minus_button = ctk.CTkButton(self,
                                       command=lambda: self.update_weight(
                                           ('minus', 'small')),
                                       text='-',
                                       font=font,
                                       text_color='black',
                                       fg_color='light gray',
                                       hover_color='gray')
    small_minus_button.grid(row=0, column=1, padx=4, pady=4)

  def update_weight(self, info=None):
    amount = 0

    if info[1] == 'large':
      amount = 1
    else:
      amount = 0.1

    if info[0] == 'plus':
      self.weight_float.set(self.weight_float.get() + amount)
    else:
      self.weight_float.set(self.weight_float.get() - amount)


class HeightInput(ctk.CTkFrame):

  def __init__(self, parent, height_int):
    super().__init__(master=parent, fg_color='White')

    self.grid(column=0, row=3, sticky='nsew', padx=10, pady=10)

    slider = ctk.CTkSlider(master=self,
                           button_color='green',
                           button_hover_color='gray',
                           progress_color='green',
                           fg_color='light gray',
                           variable=height_int,
                           from_=100,
                           to=250)
    slider.pack(side='left', fill='x', expand=True, padx=10, pady=10)

    self.output_string = ctk.StringVar()
    
    output_text = ctk.CTkLabel(self,
                               textvariable=self.output_string,
                               text_color='black',
                               font=ctk.CTkFont(family='Calibri', size=26))
    output_text.pack(side='left', padx=20)


class UnitSwitcher(ctk.CTkLabel):

  def __init__(self, parent):
    super().__init__(master=parent,
                     text='metric',
                     text_color='dark green',
                     font=ctk.CTkFont(family='Calibri', size=18))
    self.place(relx=0.98, rely=0.01, anchor='ne')


if __name__ == '__main__':
  App()
