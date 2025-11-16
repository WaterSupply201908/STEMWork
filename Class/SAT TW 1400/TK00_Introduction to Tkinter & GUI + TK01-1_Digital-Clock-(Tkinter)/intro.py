from customtkinter import *

app = CTk()
app.geometry("500x400")

def click_event() :
    print("You Clicked ME!!!")

def select_event(choice) :
    print(f'You selected {choice}')

#btn = CTkButton(master=app, text='Click Me', fg_color='pink', hover_color='red', corner_radius=32, command=click_event)
#btn.place(relx=0.5, rely=0.5, anchor='center')

#label = CTkLabel(master=app, text='Some Random Text..', font=('Roboto Mono', 20), text_color='black')
#label.place(relx=0.5, rely=0.5, anchor='center')

#combobox = CTkComboBox(master=app, values=['option 1', 'option 2', 'option 3'], fg_color='lightblue', dropdown_fg_color='blue', border_color='red', command=select_event)
#combobox.place(relx=0.5, rely=0.5, anchor='center')

#checkbox = CTkCheckBox(master=app, text='option', fg_color='lightgreen', checkbox_height=30, checkbox_width=30, corner_radius=36)
#checkbox.place(relx=0.5, rely=0.5, anchor='center')

#switch = CTkSwitch(master=app, text='option')
#switch.place(relx=0.5, rely=0.5, anchor='center')

#slider = CTkSlider(master=app, from_=0, to=100, number_of_steps=8, button_color='orange', progress_color='green')
#slider.place(relx=0.5, rely=0.5, anchor='center')

frame = CTkFrame(master=app, fg_color='brown', border_color='yellow', border_width=2)
frame.pack(expand=True)

label = CTkLabel(master=frame, text='This a frame')
entry = CTkEntry(master=frame, placeholder_text='Type something...')
btn = CTkButton(master=frame, text='Submit')

label.pack(anchor='s', expand=True, padx=30, pady=10)
entry.pack(anchor='s', expand=True, padx=30, pady=10)
btn.pack(anchor='n', expand=True, padx=20, pady=30)

app.mainloop()
