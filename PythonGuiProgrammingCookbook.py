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

# Adding a Label
ttk.Label(win, text="A Label").grid(column=0, row=0) 

#======================
# Start GUI
#======================
win.mainloop()