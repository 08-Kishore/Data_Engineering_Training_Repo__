sales = [65000, 4500, 36000, 12000, 18000, 72000, 9000]


print(sum(sales))


print(max(sales))


print(min(sales))


for sale in sales:
    if sale > 20000:
        print(sale)


sales.sort(reverse=True)


cities = {
    "Hyderabad",
    "Mumbai",
    "Delhi",
    "Hyderabad",
    "Pune",
    "Mumbai"
}
print(set(cities))


tuple1=(101,"Laptop","Electronics",75000)
product_id=tuple1[0]
product_name=tuple1[1]
category=tuple1[2]
price=tuple1[3]


dict1={
    "id":101,
    "name":"Laptop",
    "city":"Mumbai",
    "orders":22,
    "active":True
}


dict1["city"]="delhi"
dict1["orders"]+=1
dict1["email"]="abcdefgn@gmail.com"
for key,value in dict1.items():
    print(key,":",value)
