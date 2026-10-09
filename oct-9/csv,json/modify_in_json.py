import json
with open('products.json',"r") as f:
    products = json.load(f)
for product in products:
    if product["product_id"] == 101:
        product["price"]=70000


with open('products.json', 'w') as f:
    json.dump(products, f,indent=4)