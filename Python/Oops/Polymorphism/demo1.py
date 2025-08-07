
'''
polymorphism allows the same method name to behave differently based on the object that it is called on.
For example, if we have a method `draw()` in both `Circle` and `Square` classes, calling `draw()` on an instance of `Circle` will execute the circle's drawing logic, while calling it on an instance of `Square` will execute the square's drawing logic.
This is a key feature of polymorphism in object-oriented programming.
'''

'''
There are 2 main types:

Compile-time polymorphism (method overloading) – Python does not natively support this like Java or C++.

Runtime polymorphism (method overriding + duck typing) – Python fully supports this.


Real-world Example:
A Dog and a Cat both have a method speak()

When you call speak() on a dog, it says “Woof”

When you call speak() on a cat, it says “Meow”

Same method name, different behavior — that’s polymorphism.
'''
#Polymorphism via Duck Typing in Python
class Dog:
    def speak(self):
        return "Woof"
class Cat:
    def speak(self):
        return "Meow"

for animal in (Dog(),Cat()):
    print(animal.speak())


