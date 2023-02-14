from database import Product


product = Product.select()

for product in Product:
    print(product.name, product.quantity, product.price)