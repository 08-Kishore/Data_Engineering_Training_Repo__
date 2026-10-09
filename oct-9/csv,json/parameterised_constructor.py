class Employee:
    def __init__(self,emp_id,name,department,salary):
        self.emp_id=emp_id
        self.name=name
        self.department=department
        self.salary=salary

e1=Employee(1,"Arun",department="Software Engineer",salary=1000)
e2=Employee(2,"Sara",department="Data Analyst",salary=1000)