sales = [65000, 4500, 36000, 12000, 18000, 72000, 9000]

dict1={
    "id":101,
    "name":"Laptop",
    "city":"Mumbai",
    "orders":22,
    "active":True
}

def calculate_total(price, quantity):
    amount = price * quantity
    return amount

def calculate_discount(amount):
    if amount <= 20000:
        discount=amount*0.10
        return discount
    else:
        discount=amount*0.05
        return discount

def sum_list(lst):
    sum = 0
    for item in lst:
        sum += item
    return sum

def dict_func(dict1):
    if dict1.get("active",False):
        return "Available"
    else:
        return "Out of Stock"

num=int(input("Enter a number:"))
sqr_num=lambda x: x**2
print(sqr_num(num))

list2 = list(filter(lambda s:s>20000,sales))
print(list2)

map_dict=list(map(lambda s:s["city"],dict1))
print(map_dict)

unique_list=list(set(map_dict))
print(unique_list)

sorted_dict=sorted(dict1.items(), key=lambda x: x["price"])