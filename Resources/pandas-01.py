#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:40:41 2020

@author: cpsc
"""

import pandas as pd

# Row-based constructor
df = pd.DataFrame([['James', 55, 'M'], ['Jeff', 35, 'M'], ['Judy', 25, 'F']], columns=['First Name', 'Age', 'Gender'], index=['r01', 'r02', 'r03'])
print(df)

df = pd.DataFrame([{'First Name':'James', 'Age':55, 'Gender':'M'}, {'First Name':'Jeff', 'Age':35, 'Gender':'M'}, {'First Name':'Judy', 'Age':25, 'Gender':'F'}], index=['r01', 'r02', 'r03'])
print(df)

# Column-based constructor
df = pd.DataFrame({'First Name':['James', 'Jeff', 'Judy'], 'Age':[55,35,25], 'Gender':['M', 'M', 'F']})
print(df)

# Indexing operator

# Access one column
sel = df['First Name']
print(sel)

# multiple columns (fancy indexing)
sel = df[['First Name', 'Age']]
print(sel)

#sel = df[0]
#print(df) 

# Access rows 
sel = df[0:2]
print(sel)

# Using Age property 
sel = df[(df.Age < 40) & (df['Gender'] == 'M')]
print(sel)

df1 = pd.DataFrame({'First Name':['Chris', 'Eric'], 'Age':[68,40], 'Gender':['M', 'M']})
df2 = df + df1
print(df2)

# properties
print(df.index)
for i in df.index:
    print(i) 

print(df.columns)

print(df.values)


