from tkinter import *
from random import *

computerValue = {
    "0" : "Rock",
    "1" : "Paper",
    "2" : "Scissors"
}

def resetGame() :
    b1['state'] = "active"
    b2['state'] = "active"
    b3['state'] = "active"

    l1.config(text='Player              ') # 14 spaces
    l3.config(text='Computer')
    l4.config(text='')

def buttonDisable() :
    b1['state'] = "disable"
    b2['state'] = "disable"
    b3['state'] = "disable"

def isRock() :
    cv = computerValue[str(randint(0, 2))]

    if cv == 'Rock' :
        result = 'Match Draw'
    elif cv == 'Paper' :
        result = 'Computer Win'
    else :
        result = 'Player Win'

    l1.config(text='Rock            ') # 12 spaces
    l3.config(text=cv)
    l4.config(text=result)

    buttonDisable()

def isPaper() :
    cv = computerValue[str(randint(0, 2))]

    if cv == 'Rock' :
        result = 'Player Win'
    elif cv == 'Paper' :
        result = 'Match Draw'
    else :
        result = 'Computer Win'

    l1.config(text='Paper           ') # 11 spaces
    l3.config(text=cv)
    l4.config(text=result)

    buttonDisable()

def isScissors() :
    cv = computerValue[str(randint(0, 2))]

    if cv == 'Rock' :
        result = 'Computer Win'
    elif cv == 'Paper' :
        result = 'Player Win'
    else :
        result = 'Match Draw'

    l1.config(text='Scissors         ') # 9 spaces
    l3.config(text=cv)
    l4.config(text=result)

    buttonDisable()

# Main program
root = Tk()

root.title('RPS Game')
root.geometry('330x300')

Label(root, text='Rock Paper Scissors', font="normal 20 bold", fg='blue').pack(pady=20)

frame1 = Frame(root)
frame1.pack()

l1 = Label(frame1, text='Player              ', font=10)
l2 = Label(frame1, text='vs              ', font="normal 10 bold")
l3 = Label(frame1, text='Computer', font=10)

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

l4 = Label(root, text='', font="normal 20 bold", bg='white', width=15, borderwidth=2, relief='solid')

l4.pack(pady=20)

frame2 = Frame(root)
frame2.pack()

b1 = Button(frame2, text='Rock', font=10, width=7, command=isRock)
b2 = Button(frame2, text='Paper', font=10, width=7, command=isPaper)
b3 = Button(frame2, text='Scissors', font=10, width=7, command=isScissors)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

Button(root, text='Reset Game', font=10, fg='Red', bg='black', command=resetGame).pack(pady=20)

root.mainloop()