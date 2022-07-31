import tkinter as tk

#create an instance
parent = tk.Tk()

#create a title

parent.title("How to edit labels")

#create label

label = tk.Label(parent, text="This is a new label", font=("Arial Bold", 20))
label = label.grid(column=0, row=0)

parent.mainloop()