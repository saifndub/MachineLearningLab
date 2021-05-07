import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

data = pd.read_csv("data-linear-reg.csv")
length = len(data)
start = 0
count = 0
xx = 0
x1 = 0
y1 = 0
mult = 0
for var in range(start, length):
  a = data.at[var,'x']
  b = data.at[var,'y']
  plt.scatter(a,b)
  if(math.isnan(a)==False and math.isnan(b)==False):
    x1 = x1 + a
    y1 = y1 + b
    mult = mult + (a*b)
    xx = xx + (a*a)
a_x1 = float("{:.2f}".format(x1/length))
a_y1 = float("{:.2f}".format(y1/length))
a_xx = float("{:.2f}".format(xx/length))
a_mult = float("{:.2f}".format(mult/length))
t_w1 = (a_mult-(a_x1*a_y1))/(a_xx-(a_x1*a_x1))
t_w0 = (a_y1-(t_w1*a_x1))

w1 = float("{:.3f}".format(t_w1))
w0 = float("{:.3f}".format(t_w0))
x_id = 1
y = w0 + (w1*x_id)
print("The value of w0 =",w0,"and w1 =",w1)
print("Equation is : y = w0 + w1*x")
print("Last 2 digit of Id :", x_id)
print("predicted value of y :", y)