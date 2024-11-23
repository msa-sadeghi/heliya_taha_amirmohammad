import tkinter
from tkinter import *

def my_function():
    my_label.configure(text=f"سلام {input_name.get()}")

root = tkinter.Tk()
root.title("my app")
root.geometry("400x300")
root.resizable(False, False)

# input_name = Entry(root)
# input_name.place(x=150, y = 200)

# my_label = Label(root, text="سلام", font=("arial", 32))
# my_label.place(x= 100, y=100)

# my_button = Button(root, text="کلیک کن", command=my_function, padx=30, pady=30)
# my_button.place(x=150,y=250)

t = Text(root, width=30)
t.place(x =50, y = 50)
t.insert(END, "sssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")


root.mainloop()