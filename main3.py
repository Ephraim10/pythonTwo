from database import Employees
try:
    e_name = input("Enter your name\n")
    e_gender = input("Enter your sex\n")
    e_age = input("Enter your age\n")
    Employees.create(name=e_name, gender=e_gender, age=e_age)
    print("Your data has been saved successfully")
except:
    print("Failed, enter valid data")