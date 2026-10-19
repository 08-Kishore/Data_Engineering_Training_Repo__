def calculate_booking_amount(tickets, ticket_price):
    return tickets * ticket_price

def calculate_discount(amount, discount_rate):
    return amount - (amount * discount_rate / 100)

def check_event_capacity(tickets_requested, capacity):
    return tickets_requested <= capacity
