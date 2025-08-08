'''
Abstraction means hiding complex implementation details and showing only the necessary features to the user.
'''

'''
Achieved in Python mainly using:

Abstract Classes (from abc module)

Interfaces (Python doesn’t have direct interfaces, but abstract classes can act as them)
'''

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Started")
    def stop(self):
        print("Car stopped")    

class Bike(Vehicle):
    def start(self):
        print("Bike started")
    def stop(self):
        print("Bike stop")    

list = [Car(),Bike()]

for i in list:
    i.start()
    i.stop()