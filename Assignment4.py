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

#Correlation coefficient between clump_thickness and size_uniformity
a = df["clump_thickness"].corr(df["size_uniformity"])
print("Correlation coefficient between clump_thickness and size_uniformity")
print(a)


print("Correlation coefficient between clump_thickness and size_uniformity Scatter Plot")
plt.scatter(df["clump_thickness"], df["size_uniformity"])
plt.show()

print("If the correlation is possitve and closer to 1 then it is a positive correlation")
print("IF the correlation is negative closer to -1 then it is a negative correlation")
print("if the correlation is close to 0 then it has no correlation")


print("This is the grouped mean and standard deviation by class")
grouped = df.groupby(['class'])
groupeddata = grouped[["clump_thickness","size_uniformity","shape_uniformity","marginal_adhesion","epithelial_size","bare_nucleoli","bland_chromatin","normal_nucleoli","mitoses","class"]].aggregate(['mean','std'])
print(groupeddata)

for gname,i in grouped:
    temp = str(gname)
    plt.title("All Columns in box plots grouped by class "+temp)
    bp = i.boxplot(column = ["clump_thickness","size_uniformity","shape_uniformity","marginal_adhesion","epithelial_size","bare_nucleoli","bland_chromatin","normal_nucleoli","mitoses","class"])
    print("Class ",gname)
    data = i[["clump_thickness","size_uniformity","shape_uniformity","marginal_adhesion","epithelial_size","bare_nucleoli","bland_chromatin","normal_nucleoli","mitoses","class"]].aggregate(['mean','std'])
    print(data)

    plt.show()



#To describe the above analysis I would say there is correlation between different columns and having breast cancer signs