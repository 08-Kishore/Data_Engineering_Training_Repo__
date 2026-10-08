product={
    "product_id":101,
    "product_name":"Laptop",
    "product_price":65000,
    "category":"Electronics"
}
print(product)

print(product["product_name"])
print(product.get("brand"))
product["price"]=70000
product["stock"]=10000
print(product)

product.pop("category")
del product["price"]