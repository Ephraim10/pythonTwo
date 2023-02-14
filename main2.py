from database import Product
try:
    p_name = input("Enter the product name\n")
    p_quantity = input("Enter quantity\n")
    p_price = input("Enter  price\n")
    Product.create(name=p_name, quantity=p_quantity, price=p_price)
    print("Product saved successfully")
except:
    print("An error occurred.Please try again")
