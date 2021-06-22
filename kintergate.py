from tkinter import *

def userEntry(input):
    try:
        entryValue = int(input.get())
        return entryValue
    except ValueError:
        return None

def calculate():
    qts = userEntry(input)


root = Tk()
Label(root, text="Hola mundo").grid(row=0, column=0)
quarters = Entry(root)
quarters.grid(row=0, column=1)
output = quarters.get()
Label(root, text=output).grid(row=1, column=0)
quarters.bind("<Return>", on_change)
if __name__ == '__main__':
    root.mainloop()
import tkinter as tk


