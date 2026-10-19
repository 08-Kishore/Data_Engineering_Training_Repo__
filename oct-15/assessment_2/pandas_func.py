import pandas  as pd
import numpy as np
df = pd.read_csv("shipments.csv")#type:ignore

res=df.query("status=='Delivered'")
print(res)
print()

res=df["status"].count()
print(res)

df["date"]=pd.to_datetime(df["shipment_date"])
df["month"]=df["date"].dt.month

res=df["month"].count()
print(res)

res=df.groupby("destination")["cost"].mean()
print(res)

res=df.groupby("destination")["weight"].sum()
print(res)

sel_col=["shipment_id","shipment_date","destination","status"]
df=pd.read_csv("shipments.csv",usecols=sel_col)#type:ignore
print(df)

shipment=pd.read_csv("shipments.csv")#type:ignore
hubs=pd.read_csv("hubs.csv")#type:ignore
med=pd.merge(shipment,hubs,on="hub_id",how="inner")

res=med.groupby("hub_name")["cost"].sum()
print(res)

res=med.groupby("hub_name")["shipment_id"].count()
print(res)

ship_cost=med.groupby("hub_name")["cost"].sum().reset_index()
srt_ship_cost=ship_cost.sort_values(by="cost",ascending=False)
print(srt_ship_cost)

srt_ship_cost.to_csv("result_of_shipment_cost.csv",index=False)
srt_ship_cost.to_json("result_of_shipment_cost.json",orient="records")
print("hi")

med["cost_per_kg"]=med["cost"]/med["weight"]

med["Price_category"]=np.where(
    med["cost"]>=1200,'Expensive','Normal')

med["performance_category"] = np.select(
    [
        (med["status"] == "Delivered") & (med["cost"] >= 1200),
        (med["status"] == "Delivered") & (med["cost"] < 1200),
        (med["status"] == "Pending") & (med["cost"] >= 1200),
        (med["status"] == "Pending") & (med["cost"] < 1200),
    ],
    [
        "High Value Delivered",
        "Standard Delivered",
        "High Value Pending",
        "Standard Pending",
    ],
    default="Other"
)

med.to_csv("shipment_analysis.csv",index=False)
print("hi")