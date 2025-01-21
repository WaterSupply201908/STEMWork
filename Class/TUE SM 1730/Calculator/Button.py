from customtkinter import CTkButton
from Setting import *

class Button(CTkButton):
    def __init__(self, parent, text, func, col, row, font, span=1, color = 'dark-gray'):
        super().__init__(
            master = parent,
            command = func,
            text = text,
            corner_radius = STYLING['corner-radius'],
            font = font,
            fg_color = COLORS[color]['fg'],
            hover_color = COLORS[color]['hover'],
            text_color = COLORS[color]['text']
        )
        self.grid(column = col, columnspan=span, row = row, sticky = 'NSEW',
                  padx = STYLING['gap'], pady = STYLING['gap'])

class ImageButton(CTkButton) :
    def __init__(self, parent, func, col, row, image, text = '', color = 'dark-gray'):
        super().__init__(
            master = parent,
            command = func,
            text = text,
            corner_radius = STYLING['corner-radius'],
            image = image,
            fg_color = COLORS[color]['fg'],
            hover_color = COLORS[color]['hover'],
            text_color = COLORS[color]['text']
        )
        self.grid(column = col, row = row, sticky = 'NSEW',
                  padx = STYLING['gap'], pady = STYLING['gap'])
        
class NumButton(Button) :
    def __init__(self, parent, text, func, col, row, font, span, color='light-gray') :
        super().__init__(
            parent=parent,
            func=lambda:func(text),
            text=text,
            col=col,
            row=row,
            font=font,
            color=color,
            span=span
        )

class MathButton(Button) :
    def __init__(self, parent, text, operator, func, col, row, font, color='orange') :
        super().__init__(
            parent=parent,
            func=lambda:func(operator),
            text=text,
            col=col,
            row=row,
            font=font,
            color=color
        )

class MathImageButton(ImageButton) :
    def __init__(self, parent, operator, func, col, row, image, color='orange') :
        super().__init__(
            parent=parent,
            func=lambda:func(operator),
            col=col,
            row=row,
            image=image,
            color=color
        )
