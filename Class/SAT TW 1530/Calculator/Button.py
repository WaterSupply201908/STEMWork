from customtkinter import CTkButton
from Setting import *

class Button(CTkButton) :
  def __init__(self, parent, text, col, row) :
    super().__init__(master=parent, text=text)
    self.grid(column=col, row=row, sticky='NSEW')
