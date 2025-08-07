
'''
It is used to inherit the properties and behaviours of one class to another. The class that inherits another 
class is called a child class and the class that gets inherited is called a base class or parent class.

Types:
Single Inheritance
Multiple Inheritance
Multilevel Inheritance
Hierarchical Inheritance
Hybrid Inheritance
'''

# Single Inheritance

class Parent:
    def parentMethod(self):
        print("This is a parent class")

class Child(Parent):
    def childParent(self):
        print("This is a child class")

obj = Child()

obj.parentMethod()
obj.childParent()





