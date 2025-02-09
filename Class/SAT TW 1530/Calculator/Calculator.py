import customtkinter as ctk
import darkdetect
from Setting import *

class Calculator(ctk.CTk) :
  def __init__(self, is_dark) :
    super().__init__(fg_color=(WHITE, BLACK))

    ctk.set_appearance_mode(f'{"dark" if is_dark else "light"}')

    self.mainloop()

if __name__ == '__main__' :
  Calculator(darkdetect.isDark())
