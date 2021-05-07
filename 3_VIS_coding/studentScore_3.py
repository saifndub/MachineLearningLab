import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#plt.style.use("fivethirtyeight")
df = pd.read_csv("studentScore.csv")
data = df['math score']

#ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

plt.hist(data, bins=bins, edgecolor='black')

plt.xlabel('Math score')
plt.ylabel('Number of students')
plt.title('Number of students according to Math Score')
plt.tight_layout()
plt.show()





'''
Reference :
https://www.youtube.com/watch?v=XDv6T4a0RNc&t=731s

'''
