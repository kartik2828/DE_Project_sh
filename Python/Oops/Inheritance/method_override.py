
'''
Method Overriding happens when a child class defines a method with the same name as a method in its parent class.

The child class method overrides the parent class version.

When called using a child class object, the overridden version runs.
'''

class Vehicle:
    def description(self):
        return "This is a vehicle"
class Car(Vehicle):
    def description(self):
        return "This is a car"

obj = Car()
print(obj.description())  # Output: This is a car