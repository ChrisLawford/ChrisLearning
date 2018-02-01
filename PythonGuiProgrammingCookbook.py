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
from tkinter import Spinbox
from time import sleep

class ToolTip(object):
    def __init__(self,widget):
        self.widget = widget
        self.tip_window = None

    def show_tip(self, tip_text):
        "Display text in a tooltip window"
        if self.tip_window or not tip_text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 25                  # calculate to display tooltip
        y = y + cy + self.widget.winfo_rooty() + 25             # calculate to display tooltip
        self.tip_window = tw = tk.Toplevel(self.widget)         # below and to the right
        tw.wm_overrideredirect(True)                            # remove all Window Manager (wm) decorations
#        tw.wm_overrideredirect(False)                           # uncomment to see the effect
        tw.wm_geometry("+%d+%d" % (x, y))                       # create window size
        
        label = tk.Label(tw, text=tip_text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma","8", "normal"))
        label.pack(ipadx=1)
    def hide_tip(self):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()

#==============================================================================
def create_ToolTip(widget,text):
    toolTip=ToolTip(widget)             # create instance of class
    def enter(event):
        toolTip.show_tip(text)
    def leave(event):
        toolTip.hide_tip()
    widget.bind('<Enter>', enter)       # bind mouse events
    widget.bind('<Leave>', leave)
    
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
    
# Spinbox callback
def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

# Adding a Spinbox widget
spin = Spinbox(mighty, from_=0, to=10, width=5, bd=8, command=_spin)
spin.grid(column=0,row=2)

# Adding a Spinbox widget
spin = Spinbox(mighty, values=(0, 50, 100), width=5, bd=20, command=_spin)
spin.grid(column=1,row=2)

# Using a scrolled Text control
scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=5, columnspan=3)

# Add a Tooltip
create_ToolTip(scr, 'This is a ScrolledText widget')

# Create a container to hold labels
buttons_frame = ttk.LabelFrame(mighty2, text='ProgressBar')
#buttons_frame.grid(column=0, row=7, padx=20, pady=40)
buttons_frame.grid(column=0, row=7)

#update Progressbar in callback loop
def run_progressbar():
    progress_bar['maximum'] = 100
    for i in range(101):
        sleep(0.05)
        progress_bar["value"] = i   # increment progressbar
        progress_bar.update()
    progress_bar["value"] = 0

def start_progressbar():
    progress_bar.start()

def stop_progressbar():
    progress_bar.stop()

def progressbar_stop_after(wait_ms=1000):
    win.after(wait_ms, progress_bar.stop)
    
# Place buttons into the container element
ttk.Button(buttons_frame, text="Run Progressbar",   command=run_progressbar    ).grid(column=0, row=0, sticky=tk.W)
ttk.Button(buttons_frame, text="Start Progressbar", command=start_progressbar  ).grid(column=0, row=1, sticky=tk.W)
ttk.Button(buttons_frame, text="Stop immediately",  command=stop_progressbar   ).grid(column=0, row=2, sticky=tk.W)
ttk.Button(buttons_frame, text="Stop after second", command=run_progressbar    ).grid(column=0, row=3, sticky=tk.W)

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

# Add a Progressbar to Tab 2
progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=286, mode='determinate')
progress_bar.grid(column=0, row=3, pady=2)


    

name_entered.focus()    # Place cursor into name Entry
#======================
# Start GUI
#======================
win.mainloop()
