
# What are python decorator?

# Decorator is a function that takes another function as an argument 

def decorator(func):
    def wrapper():
        print("this is a msg before the function call")
        func()
        print("This is a msg after the function call")
    return wrapper

@decorator
def say_hello():
    print("Hello")
say_hello()


