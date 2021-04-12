import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("studentScore.csv")
data = df[['gender','race/ethnicity']]
#print(data)
data1 = data.groupby(['race/ethnicity','gender']).size().reset_index(name='counts') #.count()
length = len(data1)
start = 0
listGroup = []
listMale = []
listFemale = []
for var in range(start, length):
    a = data1['race/ethnicity'][var]
    if a not in listGroup:
        listGroup.append(a)

male = data1.loc[data1['gender'] == 'male']
listMale = male['counts'].tolist()
print(listMale)

female = data1.loc[data1['gender'] == 'female']
listFemale = female['counts'].tolist()
print(listFemale)

x_indexes = np.arange(len(listGroup))
width = 0.40

plt.bar(x_indexes - width/2, listMale, width=width, label="Male")
plt.bar(x_indexes + width/2, listFemale, width=width, label="Female")

plt.legend()
plt.xticks(ticks=x_indexes, labels=listGroup)
plt.xlabel('Group')
plt.ylabel('Gender')
plt.title('Gender by Group')
plt.tight_layout()

plt.show()