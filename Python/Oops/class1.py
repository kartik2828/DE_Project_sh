
class Smartphone:

    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
        

    def description(self):
        return f"This {self.name} is of {self.brand} company"

obj = Smartphone("Smartphone","Apple")
print(obj.description())

