from tkinter import *
from tkinter import Tk

window: Tk = Tk()
window.title("Calculator")
window.geometry("320x522")
frame=Frame(window)
frame.grid()
window.configure(bg='#011e42')
mainscreen = Label(window, width=100, height=10, bg='grey')
mainscreen.grid(row=0, column=0,columnspan=12,sticky=W+E)

b7 = Button(window, text="7",height=2,width=8)
b7.grid(row=1,column=0,pady=10)
b8 = Button(window, text="8",height=2,width=8)
b8.grid(row=1,column=1)
b9 = Button(window, text="9",height=2,width=8)
b9.grid(row=1,column=2)
b4 = Button(window, text="4",height=2,width=8)
b4.grid(row=2,column=0,pady=10)
b5 = Button(window, text="5",height=2,width=8)
b5.grid(row=2,column=1)
b6 = Button(window, text="6",height=2,width=8)
b6.grid(row=2,column=2)
b1 = Button(window, text="1",height=2,width=8)
b1.grid(row=3,column=0,pady=10)
b2 = Button(window, text="2",height=2,width=8)
b2.grid(row=3,column=1)
b3 = Button(window, text="3",height=2,width=8)
b3.grid(row=3,column=2)
bdot = Button(window, text=".",height=2,width=8)
bdot.grid(row=4,column=0,pady=10)
b0 = Button(window, text="0",height=2,width=8)
b0.grid(row=4,column=1)
bequals = Button(window, text="=",height=2,width=8)
bequals.grid(row=4,column=2)
bplus = Button(window, text="+",height=2,width=8)
bplus.grid(row=5,column=0,pady=10)
bneg = Button(window, text="-",height=2,width=8)
bneg.grid(row=5,column=1)
bx = Button(window, text="X",height=2,width=8)
bx.grid(row=5,column=2)
bdiv = Button(window, text="/",height=2,width=8)
bdiv.grid(row=6,column=0,pady=10)
bclr = Button(window, text="clr",height=2,width=8)
bclr.grid(row=6,column=1)
be = Button(window, text="",height=2,width=8)
be.grid(row=6,column=2)
window.mainloop()
