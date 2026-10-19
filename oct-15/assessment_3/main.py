import event_utils


print("Booking Amount:", event_utils.calculate_booking_amount(5, 1200))
print("Discounted Amount:", event_utils.calculate_discount(6000, 10))
print("Capacity Check:", event_utils.check_event_capacity(150, 200))


from event_utils import calculate_booking_amount
print("Direct Import Booking Amount:", calculate_booking_amount(3, 1000))


import event_utils as eu
print("Alias Booking Amount:", eu.calculate_booking_amount(2, 800))
