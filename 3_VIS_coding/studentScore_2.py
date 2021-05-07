import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("studentScore.csv")
data = df[['writing score']]
#print(data)
mean = data.mean()
mean = mean['writing score']        #Save result from mean dataframe to mean variable
median = data.median()
median = median['writing score']    #Save result from median dataframe to median variable
mode = data.mode()
mode = mode['writing score']
varience = data.var()
varience = varience['writing score']    #Save result from varience dataframe to varience variable
#size = data['writing score'].count()

print("Mean of :", mean)
print("Median of :", median)
print("Mode of index", mode)
print("Varience of :", varience)





'''
Reference :
https://www.youtube.com/watch?v=UgYbGxD_n04
https://www.youtube.com/watch?v=4iWvii96A1c
https://www.youtube.com/watch?v=1nibr20RhFY

'''