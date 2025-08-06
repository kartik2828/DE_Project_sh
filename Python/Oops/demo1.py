# What is class and objects in python

'''
class - class is blueprint or a template for creating objects. It defines the structure.
objects - object is the instance of the class. 

'''
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving")

mycar = Car("Toyota", "Camry") # this is an object
mycar.drive()