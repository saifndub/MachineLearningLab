import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("studentScore.csv")
data = df[['gender','race/ethnicity']]
data1 = data.groupby(['race/ethnicity']).size().reset_index(name='counts') #.count()
#print(data1)
listGroup = []
listStudent = []

listGroup = data1['race/ethnicity'].tolist()
print("Group :",listGroup)

listStudent = data1['counts'].tolist()
print("Students :",listStudent)

x_indexes = np.arange(len(listGroup))
width = 0.40

plt.bar(x_indexes, listStudent, width=width, label="Number of students")

plt.legend()
plt.xticks(ticks=x_indexes, labels=listGroup)
plt.xlabel('Group Name')
plt.ylabel('Number of Student')
plt.title('Number of Student according to Group')
plt.tight_layout()

plt.show()