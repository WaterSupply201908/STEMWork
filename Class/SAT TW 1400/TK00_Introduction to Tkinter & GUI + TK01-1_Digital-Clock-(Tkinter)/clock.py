from customtkinter import *
from time import strftime

root = CTk()
root.title("Digital Clock")

def time() :
    string = strftime('%H:%M:%S %p')
    label.configure(text=string)
    label.after(1000, time)

label = CTkLabel(root, font=('calibri', 40, 'bold'), fg_color='purple', text_color='white')
label.pack(anchor='center')

time()

root.mainloop()
