class Emmployee:
    def work(self):
        print("Emmployee is working")

class Developer(Emmployee):
    def work(self):
        print("Developer is working")

e1=Emmployee()
d1=Developer()
e1.work()
d1.work()