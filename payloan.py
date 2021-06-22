import tkinter as tk

calc = tk.Tk()
calc.title("Calculator")
calc.geometry('200x200')

def nu1():
    screen.config(text='1')

numbers = '0'

screen = tk.Label(calc, text=numbers)
screen.grid(row=0, column=0)

no1 = tk.Button(calc, text='1', command=nu1)
no1.grid(row=0, column=2)

calc.mainloop()