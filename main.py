from database import User
try:
    user_name = input("Enter name\n")
    user_email = input("Enter email\n")
    user_password = input("Enter password\n")
    User.create(name=user_name, email=user_email, password=user_password)
    print("data saved correctly")
except:
    print("Please enter valid data")
