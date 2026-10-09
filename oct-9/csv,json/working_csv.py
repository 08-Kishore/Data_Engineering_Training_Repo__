import csv
with open("products.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "product_id",
        "product_name",
        "category",
        "price",
    ])
    writer.writerow([101,"Laptop","Electronics",65000])
    writer.writerow([102,"Computer","Computers",65000])
    writer.writerow([103,"Mobile","Mobiles",65000])
    writer.writerow([104,"Other","Others",65000])


