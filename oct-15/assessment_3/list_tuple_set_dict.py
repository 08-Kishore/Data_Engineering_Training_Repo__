from numpy.ma.extras import average

booking_amounts = [
5000, 3500, 7500, 6000,
4000, 7000, 3000, 10000
]

print(sum(booking_amounts))

print(average(booking_amounts))

print(max(booking_amounts))
print(min(booking_amounts))

for i in booking_amounts:
    if i>=5000:
        print(i)


booking_amounts.sort(reverse=True)
print(booking_amounts)

cities = [
"Hyderabad",
"Mumbai",
"Pune",
"Hyderabad",
"Delhi",
"Mumbai"
]

set1 = set(cities)
print(set1)
set1.add("New York")

print(len(set1))

tuple1=(101,"Birthday_party","Chennai",35)
event_id=tuple1[0]
event_name=tuple1[1]
venue=tuple1[2]
capacity=tuple1[3]

dict1={
    "registration_id":101,
    "attendee_name":"Arun",
    "city":"Chennai",
    "tickets":20,
    "status":"active",
    "amount":20000
}

dict1["status"]="inactive"

dict1["tickets"]+=20

dict1["email"]="abcdefgh@gmail.com"

for key,value in dict1.items():
    print(key,":",value)
