#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 19:28:51 2020

@author: cpsc
"""

import tkinter as tk

def newFunc():
    pass
    
win = tk.Tk()

win.title('Configuration Screen')
win.geometry('400x200')

menuBar = tk.Menu(win)
win.configure(menu=menuBar)
fileMenu = tk.Menu(menuBar)
menuBar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='New', command=newFunc)
fileMenu.add_command(label='Open')

win.configure(bg='yellow', bd=12, relief='sunken', cursor='spider')

img = tk.PhotoImage(file='Old Guy.png')

#lbl = tk.Label(win, text='Test Label')
#lbl.configure(bg='orange', fg='blue', font=('Times', 16, 'bold italic'), anchor='nw', bd=2, relief='raised', cursor='heart', width=16 ,height=4)

lbl = tk.Label(win)
lbl.configure(image=img)
lbl.pack(side=tk.TOP, fill=tk.X)

win.mainloop()
