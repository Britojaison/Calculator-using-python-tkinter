from tkinter import *

window=Tk()
window.title("Calculator")
window.geometry("320x500")
window.configure(background="black")
mainscreen=Label(window,width=100,height=100)

mainscreen.grid(row=0,column=0)
window.mainloop()