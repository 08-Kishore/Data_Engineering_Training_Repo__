shipment_weight=int(input("enter shipment weight:"))
cost=int(input("enter cost:"))

cost_per_kg=cost/shipment_weight
print(cost_per_kg)

if shipment_weight > 20:
    print("Heavy")
elif 10 <= shipment_weight <= 20:
    print("Medium")
else:
    print("Light")

for i in range(1,21):
    print(i)

for i in range(1,21):
    if i%2==0:
        print(i)

i=5
while i>0:
    print("Processing")
    i-=1
