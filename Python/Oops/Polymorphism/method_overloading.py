'''
method overloading means having multiple methods with the same name but different parameters.

Python doesn’t support traditional method overloading. Instead, it allows default values or variable arguments to handle this.
'''

class calculator:
    def add(self, a=0,b=0,c=0):
        return a + b + c

cal = calculator()
print(cal.add(1,2,3))    
print(cal.add(1,2)) 


class calculator2:
    def add(self, *args):
        return sum(args)
obj = calculator2()
print(obj.add(1, 2, 3))
print(obj.add(1, 2))    