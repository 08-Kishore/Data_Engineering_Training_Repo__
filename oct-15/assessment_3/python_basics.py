attendee_name=input("Enter attendee name: ")
no_of_tickets=int(input("Enter number of tickets: "))
ticket_price=int(input("Enter ticket price: "))

total_booking_price=no_of_tickets*ticket_price
print(total_booking_price)

if total_booking_price>10000:
    discount=total_booking_price*0.10
else:
    discount=total_booking_price*0.05

discount_price=total_booking_price-discount
print(f"attendee name: {attendee_name} booked no_of_tickets {no_of_tickets} at price: {discount_price}")

event_capacity=int(input("Enter event capacity: "))
no_of_registerations=int(input("Enter number of registerations: "))

if event_capacity==no_of_registerations:
    print("Full")
elif event_capacity>no_of_registerations:
    print("Seats Available")
else:
    print("Invalid Data")

for i in range(1,16):
    print(i)

for i in range(1,16):
    if i%3==0:
        print(i)

i=10
while i>0:
    print(i)
    i-=1

for i in range(1,16):
    if i%3==0:
        continue
    elif i==5:
        break
    print(i)