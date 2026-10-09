sales = [
    ("North", 12000),
    ("South", 18000),
    ("West", 9500),
    ("North", 22000),
    ("East", 15000),
    ("South", 11000)
]

print("All tuples:")
for s in sales:
    print(s)

print("\nRegions:")
for s in sales:
    print(s[0])

print("\nSales amounts:")
for s in sales:
    print(s[1])

print("\nSales > 12000:")
for s in sales:
    if s[1] > 12000:
        print(s)

total_sales = sum(s[1] for s in sales)
print("\nTotal Sales:", total_sales)

highest = max(s[1] for s in sales)
lowest = min(s[1] for s in sales)
print("\nHighest Sales:", highest)
print("Lowest Sales:", lowest)

sales_amounts = [s[1] for s in sales]
print("\nSales Amounts List:", sales_amounts)

unique_regions = set(s[0] for s in sales)
print("\nUnique Regions:", unique_regions)

sorted_by_sales = sorted(sales, key=lambda x: x[1])
print("\nSorted by Sales Amount:", sorted_by_sales)

sorted_by_region = sorted(sales, key=lambda x: x[0])
print("\nSorted by Region Name:", sorted_by_region)
