import tkinter
from tkinter import Label, Button

def my_function():
    my_label.configure(text="خداحافظ")

root = tkinter.Tk()
root.title("my app")
root.geometry("400x300")
root.resizable(False, False)

my_label = Label(root, text="سلام")
my_label.place(x= 100, y=100)

my_button = Button(root, text="کلیک کن", command=my_function)
my_button.place(x=100,y=200)
root.mainloop()