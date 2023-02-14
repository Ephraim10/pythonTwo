from peewee import *
from os import path
db_connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(db_connection, "emobilis.db"))

# Create a table called users in database


class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


User.create_table(fail_silently=True)


# Create a table called users in database
class Product(Model):
    name = CharField()
    quantity = CharField()
    price = CharField()

    class Meta:
        database = db


Product.create_table(fail_silently=True)


# Create a table called Employees in database
class Employees(Model):
    name = CharField()
    gender = CharField()
    age = CharField()

    class Meta:
        database = db


Employees.create_table(fail_silently=True)


# Create a table called students in database
class Students(Model):
    name = CharField()
    gender = CharField()
    grade = CharField()
    level = CharField()
    age = CharField()

    class Meta:
        database = db


Students.create_table(fail_silently=True)
