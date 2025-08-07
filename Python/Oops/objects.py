
# Objects 

class Car:
    def __init__(self, name, color, company):
        self.name = name
        self.color = color
        self.company = company

    def detail(self):
        return f"This car name is {self.name}. Its color is {self.color} and company name is {self.company}"

obj = Car("Scorpio N", "black", "Mahindra")
result = obj.detail()
print(result)
        