# BMI : Body Mass Index
# bmi = weight (kg) / (height (m) * height (m))

from customtkinter import *

app = CTk()
app.geometry("500x400")


def action():
  print('Clicked!!!')


btn = CTkButton(master=app, text='Clcik Me', command=action)
btn.place(relx=0.5, rely=0.5, anchor='center')

app.mainloop()
