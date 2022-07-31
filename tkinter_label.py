import tkinter as tk


#create an instance
parent = tk.Tk()


#create title
parent.title("How to give label in tkinter")

#create Label
label = tk.Label(parent, text="This is a Label" )
label.grid(column=0, row=0)

parent.mainloop()