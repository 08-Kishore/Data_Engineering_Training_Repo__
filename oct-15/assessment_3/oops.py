class Event:
    def __init__(self, event_id, event_name, capacity, ticket_price):
        self.event_id = event_id
        self.event_name = event_name
        self.capacity = capacity
        self.ticket_price = ticket_price


    def display_event(self):
        print(f"Event ID: {self.event_id}, Name: {self.event_name}, "
              f"Capacity: {self.capacity}, Ticket Price: ₹{self.ticket_price}")


    def calculate_revenue(self, tickets_sold):
        return tickets_sold * self.ticket_price



event1 = Event(101, "Tech Conference", 200, 1500)
event2 = Event(102, "Music Festival", 500, 800)



class OnlineEvent(Event):
    def __init__(self, event_id, event_name, capacity, ticket_price, platform):
        super().__init__(event_id, event_name, capacity, ticket_price)  # 41. Use super()
        self.platform = platform


    def display_event(self):
        super().display_event()
        print(f"Platform: {self.platform}")



class PhysicalEvent(Event):
    def __init__(self, event_id, event_name, capacity, ticket_price, venue):
        super().__init__(event_id, event_name, capacity, ticket_price)
        self.venue = venue


    def display_event(self):
        super().display_event()
        print(f"Venue: {self.venue}")



events = [
    OnlineEvent(201, "AI Webinar", 300, 500, "Zoom"),
    PhysicalEvent(202, "Startup Meetup", 150, 1000, "Coimbatore Convention Hall")
]


for e in events:
    e.display_event()
    print("-" * 40)
