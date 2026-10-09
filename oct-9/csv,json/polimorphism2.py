class Employee:
    def work(self):
        print("Employee is working")

class Developer:
    def work(self):
        print("Developer is working")

class Tester:
    def work(self):
        print("Test is working")

def perform_work(employee):
    employee.work()

d1 = Developer()
t1 = Tester()
perform_work(d1)
perform_work(t1)