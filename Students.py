from database import Students


students = Students.select()

for students in Students:
    print(students.name, students.gender, students.grade, students.level, students.age)