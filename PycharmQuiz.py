# this is challenge by codewithharry and In this program we make a Pycharm start up when we open the pycharm we see the projract etc.
from tkinter import *

root = Tk()
# GUI logic here
# 1 argument is width ans 2 argument is Height
root.geometry("733x434")

# mini size

root.minsize(733,434)

# this is max size

root.maxsize(733,434)

# label
main = Label(text="Welcome to the Pycharm",font=20)
main.pack()
root.mainloop()