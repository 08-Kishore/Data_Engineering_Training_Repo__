def calculate_booking(ticket_price,tickets):
    return 'Total_amount:'+(ticket_price*tickets)

def accept_booking(amount):
    if amount >= 10000:
        print( "Yes Accepted"+"Discount :"+amount*0.10)
    else:
        print( " Accepted"+"Discount :"+amount*0.05)

def tot_booking_amount(list1):
    tot=sum(list1)
    print(tot)


increase_10 = lambda amt: amt * 1.10
print(increase_10(5000))


amounts = [4500, 7200, 3000, 9500, 6100]

high_amounts = list(filter(lambda a: a > 6000, amounts))
print(high_amounts)


registrations = [
    {"id": 1, "name": "Vikram", "status": "Confirmed", "amount": 5000, "city": "Chennai"},
    {"id": 2, "name": "Meera", "status": "Pending", "amount": 7000, "city": "Bangalore"},
    {"id": 3, "name": "Karan", "status": "Confirmed", "amount": 6500, "city": "Hyderabad"}
]

confirmed_regs = list(filter(lambda r: r["status"] == "Confirmed", registrations))
print(confirmed_regs)


cities = list(map(lambda r: r["city"], registrations))
print(cities)


unique_cities = set(map(lambda r: r["city"], registrations))
print(unique_cities)


sorted_regs = sorted(registrations, key=lambda r: r["amount"], reverse=True)
for reg in sorted_regs:
    print(reg["name"], reg["amount"])

