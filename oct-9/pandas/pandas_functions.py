import pandas as pd

pf=pd.read_csv("orders.csv")
print(pf)
print(pf.head())
print(pf.tail())
print(pf.columns)
print(pf.dtypes)
print(pf.shape)
pf.info()