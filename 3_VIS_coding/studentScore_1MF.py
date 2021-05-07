import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("studentScore.csv")
data = df[['gender','race/ethnicity']]
#print(data)
data1 = data.groupby(['race/ethnicity','gender']).size().reset_index(name='counts') #.count()
listGroup = []
listMale = []
listFemale = []
for i,row in data1.iterrows():
    a = row['race/ethnicity']
    if a not in listGroup:
        listGroup.append(a)
print("Group :", listGroup)

male = data1.loc[data1['gender'] == 'male']
listMale = male['counts'].tolist()
print("Male :",listMale)

female = data1.loc[data1['gender'] == 'female']
listFemale = female['counts'].tolist()
print("Female :",listFemale)

x_indexes = np.arange(len(listGroup))
width = 0.40

plt.bar(x_indexes - width/2, listMale, width=width, label="Male")
plt.bar(x_indexes + width/2, listFemale, width=width, label="Female")

plt.legend()
plt.xticks(ticks=x_indexes, labels=listGroup)
plt.xlabel('Group Name')
plt.ylabel('Number of Students')
plt.title('Number of Students according to Gender of Each Group')
plt.tight_layout()

plt.show()