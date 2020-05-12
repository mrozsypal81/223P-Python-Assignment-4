#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 20:02:34 2020

@author: cpsc
"""

import tkinter as tk

prev_x = None
prev_y = None
curr_x = None
curr_y = None

def init(event):
    '''
    print('+++ Event Name : ', event.type)
    print('+++ widget Name : ', event.widget.__class__.__name__)
    print(event.x, event.y)
    '''
    global prev_x
    global prev_y
    global curr_x
    global curr_y
    prev_x = event.x
    prev_y = event.y
    curr_x = event.x
    curr_y = event.y
    event.widget.focus_set()

def write(event):
    ch = event.char
    pass 
    
def draw(event):
    '''
    print('+++ Event Name : ', event.type)
    print('+++ widget Name : ', event.widget.__class__.__name__)
    print(event.x, event.y)
    '''
    global prev_x
    global prev_y
    global curr_x
    global curr_y
    curr_x = event.x
    curr_y = event.y
    w = event.widget
    w.create_line(prev_x, prev_y, curr_x, curr_y, fill='blue')
    prev_x = curr_x
    prev_y = curr_y
    # print(prev_x, prev_y, curr_x, curr_y)

def clear():
    cav.delete('all')

win = tk.Tk()

cav = tk.Canvas(win, width= 500, height=150, bg ='yellow')
cav.pack(side=tk.TOP)

but = tk.Button(win, text='CLEAR', command=clear)
but.pack(side=tk.TOP, anchor='e')

cav.bind('<Button-1>', init)
cav.bind('<B1-Motion>', draw)

cav.bind('<Key>', write)

win.mainloop()
