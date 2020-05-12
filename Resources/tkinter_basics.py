#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:02:55 2020

@author: cpsc
"""

import tkinter as tk

win= tk.Tk()

win.rowconfigure(0, weight=2)
win.columnconfigure(0, weight=1)
win.rowconfigure(1, weight=1)
win.columnconfigure(1, weight=2)

# grid
lbl = tk.Label(win, text='Label 1', bg='yellow', fg='red')
lbl.grid(row=0, column=0, sticky='news', columnspan=2, padx=5, pady=5)

lbl = tk.Label(win, text='Label 2', bg='orange', fg='blue')
lbl.grid(row=1, column=1, sticky='news')

win.mainloop()
