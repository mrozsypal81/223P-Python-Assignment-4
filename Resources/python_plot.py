#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:28:59 2020

@author: cpsc
"""

import matplotlib.pyplot as plt

fig = plt.figure(1)
fig1 = plt.figure(2)
fig2 = plt.figure(3)

ax =fig.add_subplot(1,1,1)
ax11 = fig1.add_subplot(2,1,1)
ax21= fig2.add_subplot(2,2,1)
ax22= fig2.add_subplot(2,2,2)
ax23 = fig2.add_subplot(2,2,3)

plt.figure(1)
plt.plot([1,2,3], [4,2,6])

plt.figure(2)
plt.boxplot([4,1,3,7,6,9])

