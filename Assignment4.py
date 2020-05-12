#CWID 889478913
#Name Michael Rozsypal
#Assignment 4


import pandas as pd
import matplotlib.pyplot as plt 


df = pd.read_csv('breast-cancer-wisconsin.csv')

df = df.replace(to_replace = "?", value = "0")
df["bare_nucleoli"] = pd.to_numeric(df["bare_nucleoli"])


print("Writing the dataframe to JSON")
df.to_json('breast-cancer-wisconsin.json')

print("Printing Dataframe")
print(df)


print("Printing the mean and standard deviation of the columns")
#This prints out every column from the dataframe with the exception of id
data = df[["clump_thickness","size_uniformity","shape_uniformity","marginal_adhesion","epithelial_size","bare_nucleoli","bland_chromatin","normal_nucleoli","mitoses","class"]].aggregate(['mean','std'])
print(data)


plt.title("All Columns in box plots")
bp = df.boxplot(column = ["clump_thickness","size_uniformity","shape_uniformity","marginal_adhesion","epithelial_size","bare_nucleoli","bland_chromatin","normal_nucleoli","mitoses","class"])
plt.show()

# plt.title("All Columns in distribution")
# dp = df.plot.kde()
# print(dp)