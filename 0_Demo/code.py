import pandas as pd
df=pd.read_csv("data.csv")
print("Total SFT", sum(df.sft))
print("Total Price", sum(df.price))