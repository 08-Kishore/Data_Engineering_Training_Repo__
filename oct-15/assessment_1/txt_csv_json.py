import csv
import json

with open("activity.txt","w")as f:
    f.write("Sentence 1 ...\n")
    f.write("Sentence 2 ...\n")
    f.write("Sentence 3 ...\n")

with open("activity.txt","a") as f:
    f.write("Sentence 4 added...")

with open("activity.txt","r") as f:
    lines = f.read()
    print(lines)


l1=[]
with open("customers.csv","r") as f:
    lines = csv.reader(f)
    for l in lines:
        l1.append(l)


with open("customers.csv","r") as f:
    reader = csv.DictReader(f)
    active_customers = [row for row in reader if row["active"]==True]

for customer in active_customers:
    print(customer)
    print()


with open("customers.csv","r") as f:
    reader = csv.DictReader(f)
    city_hyd=[row for row in reader if row["city"]=="Hyderabad"]

for city in city_hyd:
    print(city)
    print()


with open("products.json","r") as f:
    products = json.load(f)
for product in products:
    print(product["product_name"])

for product in products:
    if product["price"]>=10000:
        print(product["product_name"])

for product in products:
    print(product["supplier"]["name"],product["supplier"]["city"])

l2=[]
for product in products:
    l2.extend(product["colors"])

uniq=set(l2)
print(uniq)



for product in products:
    if product["product_id"] ==202:
        product["stock"]+=10

with open("updated_products.json","w") as f:
    json.dump(products,f,indent=4)