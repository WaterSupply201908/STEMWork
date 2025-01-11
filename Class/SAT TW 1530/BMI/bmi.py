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

    ResultText(self)
    WeightInput(self)
    HeightInput(self)
    UnitSwitcher(self)

    self.mainloop()


class ResultText(ctk.CTkLabel):

  def __init__(self, parent):
    font = ctk.CTkFont(family='Calibri', size=150, weight='bold')
    super().__init__(master=parent, text='22.5', font=font, text_color='white')

    self.grid(column=0, row=0, rowspan=2, sticky='nsew')


class WeightInput(ctk.CTkFrame):

  def __init__(self, parent):
    super().__init__(master=parent, fg_color='White')

    self.grid(column=0, row=2, sticky='nsew', padx=10, pady=10)

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
                                 text='-',
                                 font=font,
                                 text_color='black',
                                 fg_color='light gray',
                                 hover_color='gray')
    minus_button.grid(row=0, column=0, sticky='ns', padx=8, pady=8)

    plus_button = ctk.CTkButton(self,
                                text='+',
                                font=font,
                                text_color='black',
                                fg_color='light gray',
                                hover_color='gray')
    plus_button.grid(row=0, column=4, sticky='ns', padx=8, pady=8)

    small_plus_button = ctk.CTkButton(self,
                                      text='+',
                                      font=font,
                                      text_color='black',
                                      fg_color='light gray',
                                      hover_color='gray')
    small_plus_button.grid(row=0, column=3, padx=4, pady=4)

    small_minus_button = ctk.CTkButton(self,
                                       text='-',
                                       font=font,
                                       text_color='black',
                                       fg_color='light gray',
                                       hover_color='gray')
    small_minus_button.grid(row=0, column=1, padx=4, pady=4)


class HeightInput(ctk.CTkFrame):

  def __init__(self, parent):
    super().__init__(master=parent, fg_color='White')

    self.grid(column=0, row=3, sticky='nsew', padx=10, pady=10)

    slider = ctk.CTkSlider(master=self,
                           button_color='green',
                           button_hover_color='gray',
                           progress_color='green',
                           fg_color='light gray')
    slider.pack(side='left', fill='x', expand=True, padx=10, pady=10)

    output_text = ctk.CTkLabel(self, text='1.70', text_color='black',
                               font=ctk.CTkFont(family='Calibri', size=26))
    output_text.pack(side='left', padx=20)

class UnitSwitcher(ctk.CTkLabel) :
  def __init__(self, parent) :
    super().__init__(master=parent, text='metric')
    self.place(relx=0.98, rely=0.01, anchor='ne')

if __name__ == '__main__':
  App()
