
# What is the difference between __new__ and __init__ ?


'''
__new__ is a special method just like __init__. It is used before object creation. It is called before __init__.
'''

class Person:
    
    def __new__(cls, name):
        print(f"His name is {name}")
        instance = super().__new__(cls)
        return instance
        
    def __init__(self, name):
        print("Inside __init__ method")
        self.name = name    
obj = Person("Lovekesh")
print(obj.name)




