# ToDo List

from tkinter import *
from tkinter import messagebox

tasks_list = []
counter = 1

def inputError() :
    if enterTaskField.get() == '' :
        messagebox.showerror('Input Error')

        return 0
    else :
        return 1

def clear_taskNumberField() :
    taskNumberField.delete(0.0, END)

def clear_taskField() :
    enterTaskField.delete(0, END)

def insertTask() :
    global counter

    if inputError() == 0 :
        return
    
    content = enterTaskField.get() + '\n'
    tasks_list.append(content)
    textArea.insert('end -1 chars', '['+str(counter)+']'+content)
    counter += 1

    clear_taskField()

def deleteTask() :
    global counter

    if len(tasks_list) == 0 :
        messagebox.showerror("No task")

        return
    
    number = taskNumberField.get(1.0, END)

    if number == '\n' :
        messagebox.showerror("Input Error")

        return
    else :
        task_no = int(number)

    clear_taskNumberField()

    tasks_list.pop(task_no-1)
    counter -= 1

    textArea.delete(1.0, END)
    for i in range(len(tasks_list)) :
        textArea.insert('end -1 chars', '['+str(i+1)+']'+tasks_list[i])

if __name__ == "__main__" :
    root = Tk()

    root.configure(background='light green')
    root.title("ToDo App")
    root.geometry("250x300")

    enterTask = Label(root, text='Enter Your Task', bg='light green')
    enterTaskField = Entry(root)
    submit = Button(root, text='Submit', fg='black', bg='red', command=insertTask)
    textArea = Text(root, height=5, width=25, font='lucida 13')
    taskNumber = Label(root, text='Delete by Task Number', bg='blue')
    taskNumberField = Text(root, height=1, width=2, font='luida 13')
    delete = Button(root, text='Delete', fg='black', bg='red', command=deleteTask)
    exit = Button(root, text='Exit', fg='black', bg='red', command=exit)

    enterTask.grid(row=0, column=2)
    enterTaskField.grid(row=1, column=2, ipadx=50)
    submit.grid(row=2, column=2)
    textArea.grid(row=3, column=2, padx=10, sticky=W)
    taskNumber.grid(row=4, column=2, pady=5)
    taskNumberField.grid(row=5, column=2)
    delete.grid(row=6, column=2)
    exit.grid(row=7, column=2)

    root.mainloop()
