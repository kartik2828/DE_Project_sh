
# What is __init__ method in python classes ? Is it a constructor ? what happesns if we don't define it.

'''
__init__ method is a special method in python, acts like a constructor. which is called the dunder method.
It is a constructor method & it is automatically called when an object is created. 

 There are three types of access modifiers.

1) Public eg. def main(self): accessible everywhere 
2) Protected  eg. def _main(self): should only be use inside the class or subclass 
3) Private   eg def __main(self): can only be access with in the same class 


if we do not defined this then python initialize default constructor.
'''
class Person:
    def __init__(self, name):
        self.name = name

result = Person('Kartik')
print(result.name)



