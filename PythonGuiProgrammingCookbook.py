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
from tkinter import scrolledtext

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI")

# Adding a Label that will get modified
a_label = ttk.Label(win, text="A Label")
a_label.grid(column=0, row=0)

# Modified Button Click Function
def click_me():
    action.configure(text="Hello " + name.get() + ' ' + number_chosen.get())
    
# Changing our Label
ttk.Label(win, text="Enter a name:").grid(column=0,row=0)

# Adding a Text box Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable = name)
name_entered.grid(column=0,row=1)

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=2, row=1)

# Creating three checkbuttons
ttk.Label(win,text='Choose a number:').grid(column=1, row=0)
number =tk.StringVar()
number_chosen = ttk.Combobox(win,width = 12, textvariable = number, state = 'readonly')
number_chosen['values'] = (1, 2, 4, 43, 100)
number_chosen.grid(column= 1, row=1)
number_chosen.current(0)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text ="Disabled", variable = chVarDis, state= 'disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text ="Unchecked", variable = chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text ="Enabled", variable = chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

# First, we change our Radiobutton global variables into a list
colors = ["Blue", "Gold", "Red"]

# We have also changed the callback function to tbe zero-based, using the list
# instead of module-level global variables
# Radiobutton Callback
def radCall():
    radSel = radVar.get()
    if   radSel == 0: win.configure(background=colors[0]) # now zero-based
    elif radSel == 1: win.configure(background=colors[1]) # and using list
    elif radSel == 2: win.configure(background=colors[2])


# Create three Radiobuttons using one variable
radVar = tk.IntVar()

# Next we are selecting a non-existing index values for radVar
radVar.set(99)

for col in range(3):
    curRad = tk.Radiobutton(win, text = colors[col], variable = radVar, value = col, command = radCall)
    curRad.grid(column = col, row = 5, sticky = tk.W) 

# Using a scrolled Text control
scrol_w = 50
scrol_h = 3
scr = scrolledtext.ScrolledText(win, width = scrol_w, height = scrol_h, wrap = tk.WORD)
scr.grid(column = 0, columnspan =3)

# Create a container to gold labels
buttons_frame = ttk.LabelFrame(win, text=' Labels in a Frame ')
buttons_frame.grid(column = 0, row = 7, padx=20, pady=40)
#buttons_frame.grid(column = 1, row = 7)

# Place labels into the container element
ttk.Label(buttons_frame, text="Label1").grid(column = 0, row = 0, sticky= tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column = 1, row = 0, sticky= tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column = 2, row = 0, sticky= tk.W)


name_entered.focus()    # Place cursor into name Entry
#======================
# Start GUI
#======================
win.mainloop()
