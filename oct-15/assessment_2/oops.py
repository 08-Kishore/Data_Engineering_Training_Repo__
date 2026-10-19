class Shipment:
    def __init__(self,shipment_id,destination,weight,cost):
        self.cost=cost
        self.shipment_id=shipment_id
        self.destination=destination
        self.weight=weight

    def display(self):
        print(self.shipment_id)
        print(self.destination)
        print(self.weight)
        print(self.cost)

class ExpressShipment(Shipment):
    def __init__(self,shipment_id,destination,weight,cost,surcharge):
        super().__init__(shipment_id,destination,weight,cost)
        self.surcharge=surcharge

    def display(self):
        print(self.shipment_id)
        print(self.destination)
        print(self.weight)
        print(self.surcharge)
        print(self.cost)

obj1=Shipment(101,"Hyderabad",50,100)
obj2=ExpressShipment(102,"Chennai",20,350,30)

obj1.display()
obj2.display()