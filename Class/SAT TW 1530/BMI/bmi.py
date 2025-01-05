# BMI : Body Mass Index
# bmi = weight (kg) / (height (m) * height (m))

import customtkinter as ctk

class App(ctk.CTk) :
  def __init__(self) :
    super().__init__(fg_color='green')

    self.title('BMI')
    self.geometry('400x400')
    self.resizable(False, False)

    self.columnconfigure(0, weight=1)
    self.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')  
    
    ResultText(self)
    WeightInput(self)
  
    self.mainloop()

class ResultText(ctk.CTkLabel) :
  def __init__(self, parent) :
    font = ctk.CTkFont(family='Calibri', size=150, weight='bold')
    super().__init__(master=parent, text='22.5', font=font, text_color='white')

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
    label = ctk.CTkLabel(self, text='70kg', text_color='black', font=font)

    label.grid(row=0, column=2)
    '''pg 18'''
  
if __name__ == '__main__' :
  App()
