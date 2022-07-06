from tkinter import *
from tkinter import Tk

window: Tk = Tk()
window.title("Calculator")
window.geometry("320x398")
frame = Frame(window)
frame.grid()
window.configure(bg='#011e42')
mainscreen = Entry(window, width=100, bg='white', font=('Georgia 20'))
mainscreen.grid(row=0, column=0, columnspan=37, sticky=E)

def cliked(num):
    screen_num = mainscreen.get() + str(num)
    mainscreen.delete(0, END)
    mainscreen.insert(0, str(screen_num))


def clr():
    mainscreen.delete(0, END)


def addition():
    first_num = mainscreen.get()
    global old_num
    old_num = int(first_num)
    global opretion
    opretion = "addition"
    mainscreen.delete(0, END)


def substraction():
    first_num = mainscreen.get()
    global old_num
    old_num = int(first_num)
    global opretion
    opretion = "substraction"
    mainscreen.delete(0, END)


def multiplication():
    first_num = mainscreen.get()
    global old_num
    old_num = int(first_num)
    global opretion
    opretion = "multiplication"
    mainscreen.delete(0, END)


def division():
    first_num = mainscreen.get()
    global old_num
    old_num = int(first_num)
    global opretion
    opretion = "division"
    mainscreen.delete(0, END)


def equals():
    if opretion == "addition":
        new_value = mainscreen.get()
        mainscreen.delete(0, END)
        result = int(old_num) + int(new_value)
        mainscreen.insert(0,result)
    if opretion == "substraction":
        new_value = mainscreen.get()
        mainscreen.delete(0, END)
        result = int(old_num) - int(new_value)
        mainscreen.insert(0,result)
    if opretion == "multiplication":
        new_value = mainscreen.get()
        mainscreen.delete(0, END)
        result = int(old_num) * int(new_value)
        mainscreen.insert(0,result)
    if opretion == "division":
        new_value = mainscreen.get()
        mainscreen.delete(0, END)
        result = int(old_num) / int(new_value)
        mainscreen.insert(0,result)

b7 = Button(window, text="7", height=2, width=8, command=lambda: cliked(7))
b7.grid(row=1, column=0, pady=10)
b8 = Button(window, text="8", height=2, width=8, command=lambda: cliked(8))
b8.grid(row=1, column=1)
b9 = Button(window, text="9", height=2, width=8, command=lambda: cliked(9))
b9.grid(row=1, column=2)
b4 = Button(window, text="4", height=2, width=8, command=lambda: cliked(4))
b4.grid(row=2, column=0, pady=10)
b5 = Button(window, text="5", height=2, width=8, command=lambda: cliked(5))
b5.grid(row=2, column=1)
b6 = Button(window, text="6", height=2, width=8, command=lambda: cliked(6))
b6.grid(row=2, column=2)
b1 = Button(window, text="1", height=2, width=8, command=lambda: cliked(1))
b1.grid(row=3, column=0, pady=10)
b2 = Button(window, text="2", height=2, width=8, command=lambda: cliked(2))
b2.grid(row=3, column=1)
b3 = Button(window, text="3", height=2, width=8, command=lambda: cliked(3))
b3.grid(row=3, column=2)
bdot = Button(window, text=".", height=2, width=8, command=lambda: cliked("."))
bdot.grid(row=4, column=0, pady=10)
b0 = Button(window, text="0", height=2, width=8, command=lambda: cliked(0))
b0.grid(row=4, column=1)
bequals = Button(window, text="=", height=2, width=8, command=equals)
bequals.grid(row=4, column=2)
bplus = Button(window, text="+", height=2, width=8, command=addition)
bplus.grid(row=5, column=0, pady=10)
bneg = Button(window, text="-", height=2, width=8, command=substraction)
bneg.grid(row=5, column=1)
bx = Button(window, text="X", height=2, width=8, command=multiplication)
bx.grid(row=5, column=2)
bdiv = Button(window, text="/", height=2, width=8, command=division)
bdiv.grid(row=6, column=0, pady=10)
bclr = Button(window, text="clr", height=2, width=8,bg="red", command=clr)
bclr.grid(row=6, column=1)
be = Button(window, text="", height=2, width=8)
be.grid(row=6, column=2)

window.mainloop()
