class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print(f"Name:{self.name}")
        print(f"Salary:{self.salary}")

class Developer(Employee):
    pass

dev=Developer("Arun",1000)
dev.display()