import pandas as pd


df = pd.read_csv("registrations.csv")#type:ignore


print("First 5 rows:\n", df.head())
print("\nLast 5 rows:\n", df.tail())
print("\nShape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nData types:\n", df.dtypes)


print("\nSelected Columns:\n", df[["attendee_name", "city", "status", "amount"]])


confirmed = df.query("status == 'Confirmed'")
print("\nConfirmed Registrations:\n", confirmed)


high_amounts = df.query("amount > 6000")
print("\nRegistrations with amount > 6000:\n", high_amounts)


confirmed_hyd = df.query("status == 'Confirmed' and city == 'Hyderabad'")
print("\nConfirmed Registrations from Hyderabad:\n", confirmed_hyd)


status_counts = df["status"].value_counts()
print("\nRegistration Count by Status:\n", status_counts)


total_by_status = df.groupby("status")["amount"].sum()
print("\nTotal Amount by Status:\n", total_by_status)


avg_by_city = df.groupby("city")["amount"].mean()
print("\nAverage Amount by City:\n", avg_by_city)
