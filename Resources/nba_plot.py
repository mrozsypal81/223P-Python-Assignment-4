#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:19:52 2020

@author: cpsc
"""

import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_excel('nba statistics.xlsx', sheet_name='Sheet1') 
df.rename(columns={'PPGPointsPoints per game.':'PPG'}, inplace=True)
df.rename(columns={'RPGReboundsRebounds per game.':'RPG', 'APGAssistsAssists per game.':'APG', 'SPGStealsSteals per game.':'SPG', 'BPGBlocksBlocks per game.':'BPG'}, inplace=True)

#
plt.axes()
plt.hist(df['PPG'])
plt.title('Distribution of PPG Column')
plt.xlabel('Avg Points Per Game')
plt.ylabel('Count')
plt.show()

plt.hist(df['AGE'])
plt.title('Distribution of AGE Column')
plt.xlabel('AGE')
plt.ylabel('Count')
plt.show()

print(df['AGE'].describe())

plt.boxplot(df['AGE'])
plt.title('Distribution of AGE')
# plt.xticks(['1'], ['AGE'])
plt.show()

# Correlation 
plt.scatter(df['2PA'], df['2P%'])
plt.show()

plt.scatter(df['2PA'], df['PPG'])
plt.show()

sc = df.sort_values(by='2PA', inplace=True)
plt.plot(df['2PA'], df['PPG'])
plt.show()

'''
data = [[2,4,6,7,5,9], [7,3,4,9,5,5,8,4,9], [4,6,3,5,7]]
plt.boxplot(data, labels=['G1','G2','G3'])
plt.show()
'''

grouped = df.groupby('POS')
#print(grouped.groups)
#
labels = []
data = []
groups = grouped.groups
for k, v in groups.items():
    #print(k)
    labels.append(k)
    d = []
    for el in v:
        #print(el)
        d.append(df.loc[el, 'AGE'])
    data.append(d)
plt.boxplot(data, labels = labels)
plt.show()

'''
data = [5,2,9,8 ,11]
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
plt.bar(labels, data)
plt.show()
'''

mr = grouped['PPG'].mean()
print(type(mr))
plt.bar(mr.index, mr)
plt.show()



















