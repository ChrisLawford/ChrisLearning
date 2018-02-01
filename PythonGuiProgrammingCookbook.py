# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 12:15:48 2018
@author: clawford
"""
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg

win = tk.Tk()                           # Create instance 
win.title("Python GUI")                 # Add a title
tabControl = ttk.Notebook(win)          # Create Tab Control
tab1 = ttk.Frame(tabControl)            # Create a tab
tabControl.add(tab1, text='Tab 1')      # Add the tab
tab2 = ttk.Frame(tabControl)            # Create a tab
tabControl.add(tab2, text='Tab 2')      # Add the tab

tabControl.pack(expand=1, fill="both")  # Pack to make visible

# We are creating a container frame to hold all other widgets
mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
mighty.grid(column=0, row=0, padx=8, pady=4)

# We are creating a container frame to hold all other widgets
mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
mighty2.grid(column=0, row=0, padx=8, pady=4)


# Modify adding a using mighty as the parent instead of win
a_label = ttk.Label(mighty, text="Enter a name:")
a_label.grid(column=0, row=0, sticky='W')

ttk.Label(mighty, text='Choose a number:').grid(column=1, row=0)

# Modified Button Click Function
def click_me():
    action.configure(text="Hello " + name.get() + ' ' + number_chosen.get())
    
# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky='W')

# Adding a Button
action = ttk.Button(mighty, text="Click Me!", command=click_me)
action.grid(column=2, row=1)

# Creating three checkbuttons
ttk.Label(mighty, text='Choose a number:').grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty2, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty2, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty2, text="Enabled", variable=chVarEn)
check3.deselect()
check3.grid(column=2, row=4, sticky=tk.W)

# First, we change our Radiobutton global variables into a list
colors = ["Blue", "Gold", "Red"]

# We have also changed the callback function to tbe zero-based, using the list
# instead of module-level global variables
# Radiobutton Callback
def radCall():
    radSel = radVar.get()
    if   radSel == 0: mighty2.configure(text=colors[0]) # now zero-based
    elif radSel == 1: mighty2.configure(text=colors[1]) # and using list
    elif radSel == 2: mighty2.configure(text=colors[2])


# Create three Radiobuttons using one variable
radVar = tk.IntVar()

# Next we are selecting a non-existing index values for radVar
radVar.set(99)

for col in range(3):
    curRad = tk.Radiobutton(mighty2, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W) 

# Using a scrolled Text control
scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=5, columnspan=3)

# Create a container to hold labels
buttons_frame = ttk.LabelFrame(mighty2, text=' Labels in a Frame ')
#buttons_frame.grid(column=0, row=7, padx=20, pady=40)
buttons_frame.grid(column=0, row=7)

# Place labels into the container element
ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)

#Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit()

#Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# Create menu and add menu items
file_menu = Menu(menu_bar, tearoff=0)          # create File menu
file_menu.add_command(label="New")  # add File menu item
file_menu.add_separator()           # add separator item
file_menu.add_command(label="Exit", command=_quit)  # add exit menu item
menu_bar.add_cascade(label="File", menu=file_menu) #add File menu to menu bar and give it a label

def _msgBox():
#    msg.showinfo('Python Message Info Box', 'A Python GUI created using tkinter: \nThe year is 2017. ')
#    msg.showwarning('Python Message Warning Box', 'A Python GUI created using tkinter: \nThere might be a bug in this code. ')
#    msg.showerror('Python Message Error Box', 'A Python GUI created using tkinter: \nError: Houston ~ we DO have a serious PROBLEM! ')
    answer = msg.askyesnocancel('Python Message Multi Choice Box','Are you sure you really want to do this?')    
    print(answer)

# Add another Menu to the Manu Bar and an item
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=_msgBox)   # display messagebox when clicked
menu_bar.add_cascade(label="Help", menu=help_menu)

name_entered.focus()    # Place cursor into name Entry
#======================
# Start GUI
#======================
win.mainloop()
