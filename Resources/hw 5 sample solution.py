#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 06:31:09 2020

@author: cpsc
"""

import tkinter as tk

left_clicks = 0
right_clicks = 0
font_val = ('Times',14, 'bold italic')

def click_left(event):
    global left_clicks
    global right_clicks 
    left_clicks += 1
    lbl_top.config(text='The RED box: ' + str(left_clicks) + ' clicks and the BLUE box: ' + str(right_clicks) + ' clicks', font=font_val)

def click_right(event):
    global left_clicks
    global right_clicks 
    right_clicks += 1
    lbl_top.config(text='The RED box: ' + str(left_clicks) + ' clicks and the BLUE box: ' + str(right_clicks) + ' clicks', font=font_val)
    
win = tk.Tk()

# Use one frame to implement top Label widget
top_frm = tk.Frame(win)
top_frm.pack(side=tk.TOP, expand=tk.TRUE, fill=tk.BOTH)
lbl_top = tk.Label(top_frm)
lbl_top.config(text='The RED box: ' + str(left_clicks) + ' clicks and the BLUE box: ' + str(right_clicks) + ' clicks', font=font_val)
lbl_top.pack(side=tk.TOP, expand=tk.TRUE, fill=tk.BOTH)

# Use one frame to implement the bottom two label widgets
bot_frm = tk.Frame(win)
bot_frm.pack(side=tk.TOP, expand=tk.TRUE, fill=tk.BOTH)
lbl_left = tk.Label(bot_frm, text='LEFT', bg='red')
lbl_left.bind('<Button-1>', click_left)
lbl_left.pack(side=tk.LEFT, expand=tk.TRUE, fill=tk.BOTH)
lbl_right = tk.Label(bot_frm, text='RIGHT', bg='blue')
lbl_right.pack(side=tk.LEFT, expand=tk.TRUE, fill=tk.BOTH)
lbl_right.bind('<Button-1>', click_right)

win.mainloop()

