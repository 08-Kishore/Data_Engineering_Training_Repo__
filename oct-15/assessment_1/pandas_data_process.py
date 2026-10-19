import pandas as pd

df=pd.read_csv("orders.csv") # type:ignore

print(df.head())

print(df.dtypes)

print(df.shape)

res=df.query("stat=='Delivered'")
print(res)

res=df.query("quantity>2")
print(res)

df["order_value"]=df["quantity"]*df["unit_price"]

count_orders=df.groupby("stat").count()
print(count_orders)

df["order_date"]=pd.to_datetime(df["order_date"])

df["month"]=df["order_date"].dt.month

cnt_stat=df.groupby(["month","stat"]).size()
print(cnt_stat)

tot_val=df.groupby("category")["order_value"].sum()
print(tot_val)

avg_val=df.groupby("category")["order_value"].mean()
print(avg_val)

srt_val=df.sort_values("order_value",ascending=False)
print(srt_val)

