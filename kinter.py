import tkinter as tk
root = tk.Tk()
root.geometry("400x240")
w = tk.Listbox(root)

def getTextInput():
    w.insert(0, "hello world")
    w.pack()

btnRead=tk.Button(root, height=1, width=10, text="Read",
                    command=getTextInput)

btnRead.pack()

root.mainloop()