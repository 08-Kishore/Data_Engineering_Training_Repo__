product_name=input("enter product name")
price=float(input("enter price"))
quantity=int(input("enter quantity"))


total_price=price*quantity


if total_price>=50000:
    discount=total_price*0.10
    disc_total_price=total_price-discount
    print("total price is ",disc_total_price)
else:
    discount=total_price*0.05
    disc_total_price=total_price-discount
    print("total price is ",disc_total_price)


print(f"original price is {total_price} - discount {discount} = final price is {disc_total_price}")


stock_quantity=int(input("enter stock quantity"))
if stock_quantity>20:
    print("High Stock")
elif 20 > stock_quantity <= 1:
    print("Low Stock")
else:
    print("Out of stock")


for i in range(1,11):
    print(i)


stock=5
while stock<=1:
    print(stock)
    stock=stock-1
print(stock)


for i in range(1,11):
    if i==5:
        continue
    if i==8:
        break
    print(i)