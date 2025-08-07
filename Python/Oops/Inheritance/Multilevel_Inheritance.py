
class Grandfather:
    def grandfather_method(self):
        print("I am grand father")
class Father(Grandfather):
    def father_method(self):
        print("I am father")
class Son(Father):
    def son_method(self):
        print("I am son")   

obj = Son()

obj.son_method() 
obj.grandfather_method()
obj.father_method()
                    