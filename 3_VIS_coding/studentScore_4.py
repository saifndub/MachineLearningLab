import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("studentScore.csv")
data = df[['parental level of education']]
#print(data)
data1 = data.groupby(['parental level of education']).size().reset_index(name='counts') #.count()
#print(data1)
parental_level = data1['parental level of education'].tolist()
print("Parental Level :",parental_level)
count_level = data1['counts'].tolist()
print("Number of person :",count_level)

fig1, ax1 = plt.subplots()
ax1.pie(count_level, labels=parental_level, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
