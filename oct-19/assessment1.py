from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Exercise 1: Employee Model
class Employee(BaseModel):
    id: int
    name: str
    department: str
    designation: str
    salary: float
    city: str

# In-memory list
employees = []

# Exercise 2: Add Employees (POST)
@app.post("/employees")
def add_employee(employee: Employee):
    employees.append(employee)
    return employee

# Exercise 3: Retrieve All Employees (GET)
@app.get("/employees")
def get_employees():
    return employees

# Exercise 4: Retrieve Employee by ID (GET)
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for emp in employees:
        if emp.id == employee_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

# Exercise 5: Update Employee (PUT)
@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated_employee: Employee):
    for index, emp in enumerate(employees):
        if emp.id == employee_id:
            employees[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail="Employee not found")

# Exercise 6: Delete Employee (DELETE)
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    for index, emp in enumerate(employees):
        if emp.id == employee_id:
            deleted = employees.pop(index)
            return {"Message": "Employee deleted", "Employee": deleted}
    raise HTTPException(status_code=404, detail="Employee not found")
