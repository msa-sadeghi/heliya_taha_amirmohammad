# import tkinter
# from tkinter import Radiobutton, Label, StringVar, Tk

# root = Tk()

# selected_sport = StringVar(value="1")

# def my_function():
#     output.configure(text=selected_sport.get())


# r1 = Radiobutton(root, text="swim", value="swim", variable=selected_sport, command=my_function)
# r1.pack()
# r2 = Radiobutton(root, text="football", value="football", variable=selected_sport, command=my_function)
# r2.pack()

# output = Label(root, text="salaam")
# output.pack()
# root.mainloop()



# from tkinter import *

# root = Tk()

# menu = Menu(root)
# file_menu = Menu(menu, tearoff=0)
# file_menu.add_command(label="New")
# file_menu.add_command(label="Open")
# file_menu.add_separator()
# file_menu.add_command(label="Exit")
# menu.add_cascade(label="File", menu=file_menu)
# root.config(menu=menu)

# root.mainloop()


# from tkinter import *


# root = Tk()


# frame1 = Frame(root)
# frame1.pack()

# Label(frame1, text="username").pack(side=LEFT)
# Entry(frame1).pack(side=LEFT)

# frame2 = Frame(root)
# frame2.pack(pady=20)

# Label(frame2, text="password").pack(side=LEFT)
# Entry(frame2).pack(side=LEFT)

# Button(root, text="ورود").pack()

# root.mainloop()


w = open("my_file.txt", "a+")
w.write("\nsalaam4")
w.close()

# with open("test1.txt", "w") as w:
#     w.write("hi")

# w = open("my_file.txt", "r")
# print(w.read())
# w.close()

# with open("test1.txt", "r") as w:
#     print(w.read())
    
