#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:18:03 2020

@author: cpsc
"""

import tkinter as tk

win = tk.Tk()

img = tk.PhotoImage(file='Old Guy.png')
w = img.width()
h = img.height()

cav = tk.Canvas(win, width= 500, height=h+150, bg ='yellow')
cav.pack(side=tk.TOP)

# put text
cav.create_text(20, 10, text='This is a Test String.', fill='red', anchor='nw')

# create a line
cav.create_line(30, 30, 40, 60, fill='blue')

# create image 
cav.create_image(100, 50, image=img, anchor='nw')

win.mainloop()
