from database import Employees


employees = Employees.select()

for employees in Employees:
    print(employees.name, employees.gender, employees.age)