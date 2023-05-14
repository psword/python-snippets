# -*- coding: utf-8 -*-
"""
Spyder Editor ~ VS Code Editor

This is a temporary script file.
"""

import tkinter
import tkinter.messagebox
from tkinter import Tk
from tkinter import Button

win=Tk() #creating the main window and storing the window object in 'win'
win.title('Welcome') #setting title of the window
win.geometry('640x480') #setting the size of the window

def func():#function of the button
    tkinter.messagebox.showinfo("This is just a test message box")
    
btn=Button(win,text="Click Me", width=10,height=5,command=func)
btn.place(x=270,y=180)


win.mainloop() #running the loop that works as a trigger