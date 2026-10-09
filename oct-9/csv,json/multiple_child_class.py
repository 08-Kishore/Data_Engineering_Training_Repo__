from pickletools import string1


class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def code(self):
        print("Writing python code")

class Tester(Employee):
    def test(self):
        print("Testing application")

s1=Tester()
s1.work()
s2=Developer()
s2.work()
s2.code()
s1.test()