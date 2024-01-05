import pandas as pn
import matplotlib.pyplot as plt


data = pn.read_csv("output_table.csv")

print(data)

a = data["Survived"].value_counts()
print(a)

b = data.groupby("Survived")["Pclass"].value_counts().unstack()
print(b)

# print(b[0])

b1 = data.groupby("Pclass")["Survived"].value_counts().unstack()





