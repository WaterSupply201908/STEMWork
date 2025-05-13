import tkinter as tk
import random

COLOURS = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
TOTAL = 30
timeleft = TOTAL

def countdown() :
    global timeleft

    if timeleft > 0 :
        timeleft -= 1

        timeLabel.config(text='Time left: '+str(timeleft))
        timeLabel.after(1000, countdown)

def nextColour() :
    global score, timeleft

    if timeleft > 0 :
        e.focus_set()

        if e.get().lower() == COLOURS[1].lower() :
            score += 1

        e.delete(0, tk.END)
        random.shuffle(COLOURS)
        label.config(fg=str(COLOURS[1]), text=str(COLOURS[0]))
        scoreLabel.config(text='Score: '+str(score))

def startGame(event) :
    if timeleft == TOTAL :
        countdown()

    nextColour()

# Main program
root = tk.Tk()
root.geometry('375x200')
root.title('Color Game')

instructionLabel = tk.Label(root, text='Type in the colour of the words, and not word text!',
                            font=('Helveticas', 12))
instructionLabel.pack()

scoreLabel = tk.Label(root, text='Press Enter to Start', font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tk.Label(root, text='Time Left: '+str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

label = tk.Label(root, font=('Helvetica', 60))
label.pack()

e = tk.Entry(root)

root.bind('<Return>', startGame)
e.pack()
e.focus_set()

root.mainloop()
