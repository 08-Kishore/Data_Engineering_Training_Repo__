import csv
list1=[]
with open("shipments.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        list1.append(row)
print(list1)
with open('shipments.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"Shipment id:{row['shipment_id']}, Coustomer:{row['customer']}, Status:{row['status']}")

with open('shipments.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        weight=float(''.join([c for c in row['weight'] if c.isdigit() or  c=='.']))
        cost=float(''.join([c for c in row['cost'] if c.isdigit() or c=='.']))
        print(f"Shipment id:{row['shipment_id']}, Cost:{cost}, Weight:{weight}")

tot=0
with open('shipments.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cost=float(''.join([c for c in row['cost'] if c.isdigit() or c=='.']))
        tot+=cost

print("Total cost is ",tot)

list2=[]
with open('shipments.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cost = float(''.join([c for c in row['cost'] if c.isdigit() or c == '.']))
        if cost>700:
            list2.append(row)

print(list2)

with open('shipments.csv') as f:
    reader = csv.DictReader(f)
    delivered_shipments = list(filter(lambda row:row['status']=='Delivered', reader))
    for shipment in delivered_shipments:
        print(f"Shipment id:{shipment['shipment_id']}, Status:{shipment['status']}")


with open('shipments.csv') as f:
    reader = csv.DictReader(f)
    shipment_weighted = list(filter(
        lambda row: float(''.join([c for c in row['weight'] if c.isdigit() or c == '.'])) > 10,
        reader
    ))
    for shipment in shipment_weighted:
        weight = float(''.join([c for c in shipment['weight'] if c.isdigit() or c == '.']))
        print(f"Shipment id: {shipment['shipment_id']}, Weight: {weight}")

with open("shipments.csv") as f:
    reader = csv.DictReader(f)
    cities = list(map(lambda row: row['city'], reader))
    print("All Cities:", cities)
with open("shipments.csv") as f:
    reader = csv.DictReader(f)
    unique_cities = set(map(lambda row: row['city'], reader))
    print("Unique Cities:", unique_cities)



with open("shipments.csv") as f:
    reader = list(csv.DictReader(f))

    sorted_by_cost = sorted(reader, key=lambda row: float(''.join([c for c in row['cost'] if c.isdigit() or c == '.'])))
    print("\nSorted by Cost (Low → High):")
    for row in sorted_by_cost:
        cost = float(''.join([c for c in row['cost'] if c.isdigit() or c == '.']))
        print(f"Shipment ID: {row['shipment_id']}, Cost: {cost}")

    sorted_by_weight = sorted(reader, key=lambda row: float(''.join([c for c in row['weight'] if c.isdigit() or c == '.'])), reverse=True)
    print("\nSorted by Weight (High → Low):")
    for row in sorted_by_weight:
        weight = float(''.join([c for c in row['weight'] if c.isdigit() or c == '.']))
        print(f"Shipment ID: {row['shipment_id']}, Weight: {weight}")
    sorted_by_customer = sorted(reader, key=lambda row: row['customer'])

    for row in sorted_by_customer:
        print(f"Shipment ID: {row['shipment_id']}, Customer: {row['customer']}")
    for row in reader:
        weight = float(''.join([c for c in row['weight'] if c.isdigit() or c == '.']))
        cost = float(''.join([c for c in row['cost'] if c.isdigit() or c == '.']))
        cost_per_kg = (lambda c, w: c / w if w != 0 else 0)(cost, weight)
        print(f"Shipment ID: {row['shipment_id']}, Cost per kg: {cost_per_kg:.2f}")
