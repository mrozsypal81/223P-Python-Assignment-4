#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 20:20:26 2020

@author: cpsc
"""

import pandas as pd

# Row-based constructor
df = pd.DataFrame([['James', 55, 'M'], ['Jeff', 35, 'M'], ['Judy', 25, 'F']], columns=['First Name', 'Age', 'Gender'], index=['r01', 'r02', 'r03'])
print(df)

# csf file
df.to_csv('person.csv')

df.to_csv('person_nh.csv', header=None)

df1 = pd.read_csv('person_nh.csv', header=None)
print(df1)


df.to_csv('person_ni.csv', index=False)

df1 = pd.read_csv('person_ni.csv')
print(df1)


df1 = pd.read_csv('person_nh.csv', header=None, names=['First Name', 'Age', 'Genger'])
print(df1)


# json file
df.to_json('person.json')

df1 = pd.read_json('person.json')
print(df1)



