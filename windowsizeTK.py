from cProfile import label
import tkinter as tk

#create an instance

parent = tk.Tk()

#create title
parent.title("How to set default window size ")

#create label
lab = tk.Label(parent, text=" This can done by using geometry function  as by setting the value for as(600x300)", font="Georgia 10")
lab = lab.grid(column=0,row=0)

parent.geometry('600x300')
parent.mainloop()
