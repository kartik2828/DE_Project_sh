

# What is the difference bw @staticmethod, @classmethod and regular instance method in python ?

'''
static method: these are not associated the class or instance.
They are defined using @staticmethod decorator.

classmethod : These are associated with the class and not the instance of the class.
Theey are defined using @classmethod decorator.


regular instance method: These are the most common one.
this is associated with instance of the class. 
here we have the self concept, when we define this method, the method's first argument is always self.
'''

class My_class():
    @staticmethod
    def static_method():
        print("This is a static method")

    @classmethod
    def class_method(cls):
        print("This is a class method of", cls)

    # @regularmethod - rgular method is not a decorator, it is just a method defined in the class.
    def instance_method(self):
        print("This is an instance methos of", self)
obj = My_class()

My_class.static_method()
My_class.class_method()
obj.instance_method("python")


