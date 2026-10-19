from random import choice

import pandas as pd
import numpy as np


customers = pd.read_csv("customers.csv")#type:ignore
orders = pd.read_csv("orders.csv")#type:ignore

merged = pd.merge(customers,orders,on="customer_id",how="inner")

merged["order_value"]=merged["quantity"]*merged["unit_price"]

result=merged[["order_id","customer_name","city","product","stat","order_value"]]
print(result)

res=merged.query("city=='Hyderabad'")
print(res)

tot_order=merged.groupby("city")["order_value"].count()
print(tot_order)

tot_sales=merged.groupby("city")["order_value"].sum()
print(tot_sales)

avg_order=merged.groupby("city")["order_value"].mean()
print(avg_order)

srt_city_rslt=tot_sales.sort_values(ascending=False)
print(srt_city_rslt)

srt_city_rslt.to_csv("city_sales_summary.csv",index=False)

srt_city_rslt.to_json("city_sales_summary.json",orient="records")

conditions=[
    merged["order_value"]>=50000,
    (merged["order_value"] >= 15000) & (merged["order_value"] < 50000),
    merged["order_value"]>=0
]
ch=["High","Medium","Low"]


merged["order_size"]=np.select(conditions,ch,default="low")

#print(merged.columns)
merged["priority_customer"]=np.where(
    merged["segment"]=="Corporate","Priority","Normal"
)
merged.to_csv("enriched_orders.csv",index=False)