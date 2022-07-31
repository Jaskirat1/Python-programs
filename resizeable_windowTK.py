import tkinter as tk

#create an instance
parent = tk.Tk()
#create title
parent.title("Resizeable Window")
#create LAbel
lab = tk.Label(parent, text="How to disable resizing the GUI")
lab = lab.grid(column=0, row=0)

parent.resizable(0,0)

parent.mainloop()

