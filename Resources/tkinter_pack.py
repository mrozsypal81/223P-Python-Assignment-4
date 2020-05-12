#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:56:39 2020

@author: cpsc
"""

import tkinter as tk

win = tk.Tk()


lbl = tk.Label(win, text='Label 1', bg='yellow', fg='red')
lbl.pack(side=tk.LEFT)

lbl = tk.Label(win, text='Label 2', bg='orange', fg='blue')
lbl.pack(side=tk.LEFT)

lbl = tk.Label(win, text='Label 3', bg='yellow', fg='red')
lbl.pack(side=tk.TOP)

lbl = tk.Label(win, text='Label 4', bg='orange', fg='blue')
lbl.pack(side=tk.TOP)

lbl = tk.Label(win, text='Label 5', bg='orange', fg='blue')
lbl.pack(side=tk.LEFT)

'''
lbl = tk.Label(win, text='Label 1', bg='yellow', fg='red')
lbl.pack(side=tk.LEFT, expand=tk.TRUE, fill=tk.BOTH)

lbl = tk.Label(win, text='Label 2', bg='orange', fg='blue')
lbl.pack(side=tk.LEFT, anchor='nw')
'''
'''
lbl = tk.Label(win, text='Label 3', bg='yellow', fg='blue')
lbl.pack(side=tk.TOP)

lbl = tk.Label(win, text='Label 4', bg='orange', fg='blue')
lbl.pack(side=tk.BOTTOM)
'''
win.mainloop()
