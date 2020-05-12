#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:06:59 2020

@author: cpsc
"""

import tkinter as tk
import tkinter.ttk as ttk

def getVal():
    global entry
    global lbl1
    global var
    print('+++ Value Entered By User: ', entry.get())
    print('=== Option Selected By User: ', var.get())
    val = entry.get()
    val1 = var.get()
    lbl1.config(text = val + ' : ' + val1)
    
win = tk.Tk()

lbl = tk.Label(win, text='Please Enter Name:')
lbl.pack(side=tk.TOP, anchor='w') 

entry = tk.Entry(win)
entry.pack(side=tk.TOP, fill=tk.X)

button = tk.Button(win, text='SUBMIT', command = getVal)
button.pack(side=tk.TOP, anchor='e')

lbl1 = tk.Label(win)
lbl1.config(text='Hello.')
lbl1.pack(side=tk.TOP)


data = ['O1', 'O2', 'O3']
var = tk.StringVar()
combobox = ttk.Combobox(win, values=data, textvariable = var)
combobox.pack(side=tk.TOP)

win.mainloop()


