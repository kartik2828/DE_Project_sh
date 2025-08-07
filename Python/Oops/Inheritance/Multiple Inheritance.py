

'''
Multiple inheritance in Python allows you to construct a class based 
on more than one parent classes. The Child class thus inherits the attributes and method from all parents
'''

class Parent:
    def pen(self):
        print("This is a pen")
class Parent2:
    def pencil(self):
        print("This is a pencil")  
class Child(Parent,Parent2):
    def childmehtod(self):
        self.pen()
        self.pencil()
        return "They both are use for writing"

obj = Child()
print(obj.childmehtod())                 
