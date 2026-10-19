import csv


with open("registrations.csv", "r") as f:
    reader = csv.DictReader(f)
    registrations = list(reader)


confirmed = list(filter(lambda r: r["status"] == "Confirmed", registrations))
print("Confirmed Registrations:")
for r in confirmed:
    print(r)


hyd_regs = list(filter(lambda r: r["city"] == "Hyderabad", registrations))
print("\nHyderabad Registrations:")
for r in hyd_regs:
    print(r)


for r in registrations:
    r["amount"] = int(r["amount"])


high_amounts = list(filter(lambda r: r["amount"] > 7000, registrations))
print("\nRegistrations with amount > 7000:")
for r in high_amounts:
    print(r)


total_amount = sum(r['amount'] for r in registrations)
print("\nTotal Registration Amount:", total_amount)


cities = set(map(lambda r: r["city"], registrations))
print("\nUnique Cities:", cities)
