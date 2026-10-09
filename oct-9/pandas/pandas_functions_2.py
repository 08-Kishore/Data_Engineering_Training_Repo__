import pandas as pd
df = pd.read_csv("orders.csv")
print(df["product"])
print(
    df[
        ["order_id","product","amount"]
    ])

delivered=df.query("status == 'Delivered'")
print(delivered)

result=df.query("amount > 20000")
print(result)

print(
    df["status"].value_counts()
)
print()
result=(
    df.groupby("status")
    .size()
)
print(result)

df["order_date"]=pd.to_datetime(df["order_date"])
df["month"]=df["order_date"].dt.month
print(df)

