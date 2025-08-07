'''
Hybrid Inheritance is a combination of two or more types of inheritance 
(e.g. multilevel + multiple, or hierarchical + multilevel).

      A
    B   C
      D

'''

class A:
    def show_A(self):
        print("This is class A")
class B(A):
    def show_B(self):
        print("This is class B")
class C(A):
    def show_C(self):
        print("This is class C")
class D(B,C):
    def show_D(self):
        print("This is class D")

obj = D()
obj.show_A()
obj.show_B()
obj.show_C() 
obj.show_D()

# In this structure, if both B and C had a 
# method with the same name, Python would use MRO (Method Resolution Order) to decide which one to call.