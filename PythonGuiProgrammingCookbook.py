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
import GUI_tabbed as tt
from threading import Thread

GLOBAL_CONST = 42



class OOP():
    def method_in_a_thread(self, num_of_loops=10):
        print('Hi, how are you?')
        for idx in range(num_of_loops):
            sleep(1)
            self.scr.insert(tk.INSERT, str(idx) +'\n')
        sleep(1)
        print('method_in_a_thread():', self.run_thread.isAlive())
        
    def __init__(self):
        # Create instance
        self.win = tk.Tk()                  # Create instance 
        
        #tt.create_ToolTip(self.win, 'Hello GUI')
        
        self.win.title("Python GUI")        # Add a title
        self.create_widgets()
    
    # Button callback
    def click_me(self):
        self.action.configure(text="Hello " + self.name.get() + ' ' + self.number_chosen.get())
        self.create_thread()
    
    # We have also changed the callback function to tbe zero-based, using the list
    # instead of module-level global variables
    # Radiobutton Callback
    def radCall(self):
        radSel = self.radVar.get()
        if   radSel == 0: self.mighty2.configure(text='Blue') # now zero-based
        elif radSel == 1: self.mighty2.configure(text='Red') # and using list
        elif radSel == 2: self.mighty2.configure(text='Green')    
    
    # Spinbox callback
    def _spin(self):
        value = self.spin.get()
        print(value)
        self.scr.insert(tk.INSERT, value + '\n')   
    
    #update Progressbar in callback loop
    def run_progressbar(self):
        self.progress_bar['maximum'] = 100
        for i in range(101):
            sleep(0.05)
            self.progress_bar["value"] = i   # increment progressbar
            self.progress_bar.update()       # have to call update() in loop
            self.progress_bar["value"] = 0       #reset/clear progressbar   
            
    def start_progressbar(self):
        self.progress_bar.start()
                        
    def stop_progressbar(self):
        self.progress_bar.stop()
                        
    def progressbar_stop_after(self, wait_ms=1000):
        self.win.after(wait_ms, self.progress_bar.stop)
    
    #Exit GUI cleanly
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()
    
    def _msgBox(self):
        #    msg.showinfo('Python Message Info Box', 'A Python GUI created using tkinter: \nThe year is 2017. ')
        #    msg.showwarning('Python Message Warning Box', 'A Python GUI created using tkinter: \nThere might be a bug in this code. ')
        #    msg.showerror('Python Message Error Box', 'A Python GUI created using tkinter: \nError: Houston ~ we DO have a serious PROBLEM! ')
        answer = msg.askyesnocancel('Python Message Multi Choice Box','Are you sure you really want to do this?')    
        print(answer)

    def usingGlobal(self):
        global GLOBAL_CONST
        print(GLOBAL_CONST)
        GLOBAL_CONST = 777
        print(GLOBAL_CONST)
        
    # Running mehtods in Threads
    def create_thread(self):
        self.run_thread = Thread(target=self.method_in_a_thread, args=[8])
        self.run_thread.setDaemon(True)
        self.run_thread.start()
        print(self.run_thread)
        print('createThread():',self.run_thread.isAlive())
        
###############################################################################
    
    def create_widgets(self):
        tabControl = ttk.Notebook(self.win)     # Create Tab Control
        tab1 = ttk.Frame(tabControl)            # Create a tab
        tabControl.add(tab1, text='Tab 1')      # Add the tab
        tab2 = ttk.Frame(tabControl)            # Create a tab
        tabControl.add(tab2, text='Tab 2')      # Add the tab
        tab3 = ttk.Frame(tabControl)            # Create a tab
        tabControl.add(tab3, text='Tab 3')      # Add the tab
        tabControl.pack(expand=1, fill="both")  # Pack to make visible
    
        # We are creating a container frame to hold all other widgets
        mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
        mighty.grid(column=0, row=0, padx=8, pady=4)
    
        # We are creating a container frame to hold all other widgets
        self.mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
        self.mighty2.grid(column=0, row=0, padx=8, pady=4)
    
    
        # Modify adding a using mighty as the parent instead of win
        a_label = ttk.Label(mighty, text="Enter a name:")
        a_label.grid(column=0, row=0, sticky='W')
        
        ttk.Label(mighty, text='Choose a number:').grid(column=1, row=0)
        
        # Adding a Textbox Entry widget
        self.name = tk.StringVar()
        self.name_entered = ttk.Entry(mighty, width=24, textvariable=self.name)
        self.name_entered.grid(column=0, row=1, sticky='W')
            
        # Adding a Button
        self.action = ttk.Button(mighty, text="Click Me!", command=self.click_me)
        self.action.grid(column=2, row=1)
        
        # Creating three checkbuttons
        ttk.Label(mighty, text='Choose a number:').grid(column=1, row=0)
        number = tk.StringVar()
        self.number_chosen = ttk.Combobox(mighty, width=14, textvariable=number, state='readonly')
        self.number_chosen['values'] = (1, 2, 4, 42, 100)
        self.number_chosen.grid(column=1, row=1)
        self.number_chosen.current(0)
            
        chVarDis = tk.IntVar()
        check1 = tk.Checkbutton(self.mighty2, text="Disabled", variable=chVarDis, state='disabled')
        check1.select()
        check1.grid(column=0, row=4, sticky=tk.W)
            
        chVarUn = tk.IntVar()
        check2 = tk.Checkbutton(self.mighty2, text="UnChecked", variable=chVarUn)
        check2.deselect()
        check2.grid(column=1, row=4, sticky=tk.W)
        
        chVarEn = tk.IntVar()
        check3 = tk.Checkbutton(self.mighty2, text="Enabled", variable=chVarEn)
        check3.deselect()
        check3.grid(column=2, row=4, sticky=tk.W)
        
        # First, we change our Radiobutton global variables into a list
        colors = ["Blue", "Gold", "Red"]
        

        # Create three Radiobuttons using one variable
        self.radVar = tk.IntVar()
                
        # Next we are selecting a non-existing index values for radVar
        self.radVar.set(99)
                
        for col in range(3):
            curRad = tk.Radiobutton(self.mighty2, text=colors[col], variable=self.radVar, value=col, command=self.radCall)
            curRad.grid(column=col, row=6, sticky=tk.W) 
            tt.create_ToolTip(curRad, 'This is a radio button')
            
        # Adding a Spinbox widget
        self.spin = Spinbox(mighty, from_=0, to=10, width=5, bd=8, command=self._spin)
        self.spin.grid(column=0,row=2, sticky = 'W')

        # Adding a Spinbox widget
        #self.spin = Spinbox(mighty, values=(0, 50, 100), width=5, bd=20, command=self._spin)
        #self.spin.grid(column=1,row=2)
        
        # Using a scrolled Text control
        scrol_w = 40
        scrol_h = 10
        self.scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scr.grid(column=0, row=3, columnspan=3)
        
        # Add a Tooltip
        tt.create_ToolTip(self.scr, 'This is a ScrolledText widget')
        
        # Create a container to hold labels
        buttons_frame = ttk.LabelFrame(self.mighty2, text='ProgressBar')
        #buttons_frame.grid(column=0, row=7, padx=20, pady=40)
        buttons_frame.grid(column=0, row=7)
            
        # Place buttons into the container element
        ttk.Button(buttons_frame, text="Run Progressbar",   command=self.run_progressbar    ).grid(column=0, row=0, sticky=tk.W)
        ttk.Button(buttons_frame, text="Start Progressbar", command=self.start_progressbar  ).grid(column=0, row=1, sticky=tk.W)
        ttk.Button(buttons_frame, text="Stop immediately",  command=self.stop_progressbar   ).grid(column=0, row=2, sticky=tk.W)
        ttk.Button(buttons_frame, text="Stop after second", command=self.run_progressbar    ).grid(column=0, row=3, sticky=tk.W)
                            
        for child in buttons_frame.winfo_children():
            child.grid_configure(padx=8, pady=4)
        
        #Creating a Menu Bar
        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)

        # Create menu and add menu items
        file_menu = Menu(menu_bar, tearoff=0)          # create File menu
        file_menu.add_command(label="New")  # add File menu item
        file_menu.add_separator()           # add separator item
        file_menu.add_command(label="Exit", command=self._quit)  # add exit menu item
        menu_bar.add_cascade(label="File", menu=file_menu) #add File menu to menu bar and give it a label
    
     
        # Add another Menu to the Manu Bar and an item
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self._msgBox)   # display messagebox when clicked
        menu_bar.add_cascade(label="Help", menu=help_menu)
        
        # Add a Progressbar to Tab 2
        self.progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=286, mode='determinate')
        self.progress_bar.grid(column=0, row=3, pady=2)
        
        # Tab Control 3
        tab3_frame = tk.Frame(tab3, bg='blue')
        tab3_frame.pack()
        for orange_color in range(2):
            canvas = tk.Canvas(tab3_frame, width=150, height=80, highlightthickness=0, bg='orange')
            canvas.grid(row=orange_color, column=orange_color)
            
        # get data from a widget
        strData = self.spin.get()
        print("Spinbox value: " + strData)
                
        self.usingGlobal()
        
        # Add Tooltips -----------------------------------------------------
        # Add a Tooltip to the Spinbox
        tt.create_ToolTip(self.spin, 'This is a Spinbox control')   
                
        # Add Tooltips to more widgets
        tt.create_ToolTip(self.name_entered, 'This is an Entry control')  
        tt.create_ToolTip(self.action, 'This is a Button control')                      
        tt.create_ToolTip(self.scr, 'This is a ScrolledText control')

        self.name_entered.focus()    # Place cursor into name Entry
#======================
# Start GUI
#======================
oop = OOP()

# Running methods in Threads
run_thread = Thread(target = oop.method_in_a_thread)
oop.win.mainloop()

