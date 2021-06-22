import pandas as pd

df = pd.read_csv("data.csv", header=0)
uniques = df.filter("hey")
print(df.info())
print(df)
