import csv

with open("products.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open("products.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)