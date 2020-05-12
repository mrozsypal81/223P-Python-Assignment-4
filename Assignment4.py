#CWID 889478913
#Name Michael Rozsypal
#Assignment 4


import pandas as pd
import matplotlib.pyplot as plt 


df = pd.read_csv('breast-cancer-wisconsin.csv')

print("Writing the dataframe to JSON")
df.to_json('breast-cancer-wisconsin.json')

print("Printing Dataframe")
print(df)