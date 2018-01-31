# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:52:24 2018

@author: clawford
"""
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI")

# Adding a Label that will get modified
a_label = ttk.Label(win, text="A Label")
a_label.grid(column=0, row=0)

# Modified Button Click Function
def click_me():
    action.configure(text="Hello " + name.get())
    
# Changing our Label
ttk.Label(win, text="Enter a name:").grid(column=0,row=0)

# Adding a Text box Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable = name)
name_entered.grid(column=0,row=1)

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=1, row=1)
action.configure(state='disabled')

name_entered.focus()    # Place cursor into name Entry

#======================
# Start GUI
#======================
win.mainloop()
