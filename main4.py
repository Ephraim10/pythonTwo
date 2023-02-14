from database import Students
try:
    s_name = input("Enter your name\n")
    s_gender = input("Enter your gender\n")
    s_grade = input("Enter the grade you scored\n")
    s_level = input("Enter your education level\n")
    s_age = input("Enter your age\n")
    Students.create(name=s_name, gender=s_gender, grade=s_grade, level=s_level, age=s_age)
    print("Your data has been saved successfully")
except:
    print("Failed, enter valid data")