#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:58:10 2020

@author: cpsc
"""

import pandas as pd

# Row-based constructor
df = pd.DataFrame([['James', 55, 'M'], ['Jeff', 35, 'M'], ['Judy', 25, 'F']], columns=['First Name', 'Age', 'Gender'], index=['r01', 'r02', 'r03'])
print(df)

print(type(df.index), df.index)

print(len(df.index), df.index[1])

print(type(df.columns), df.columns)

print(len(df.columns), df.columns[1])

print(type(df.values), df.values)

print(df['Age'])

print(df.Age)

print('+++++')

# loc
print(type(df.loc))

sel = df.loc['r01', 'First Name']
print(sel) 

# fancy indexing
sel = df.loc[['r01', 'r02', 'r03'],['First Name', 'Age']]
print(sel)

sel = df.loc[:,['First Name', 'Age']]
print(sel)

# iloc
print(type(df.iloc))

sel = df.iloc[0, 0]
print(sel) 

# slicing
sel = df.iloc[0:2, 0:2]
print(sel)

# Updating the table

# Updating row index

df.index.values[1] = 'r03'
print(df)

sel = df.loc[df.index == 'r03']
print(sel)

print('==========')

df.index = ['c01', 'c02', 'c03']
print(df)

df.iloc[0, 0] = 'John'
print(df)

sel = df[df.Age<30]
print(sel)

sel = df.loc[df.Age<30, ['First Name', 'Age']]
print(sel)


df.set_value('c01', 'First Name', 'Eric')
print(df)



















