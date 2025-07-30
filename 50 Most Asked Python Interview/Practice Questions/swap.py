
# How do you swap two variables in Python ?

a = 10
b = 7

# without using temp variable

def my_func():
    global a,b
    b = a-b   #3
    a = a-b
    b = a+b
    print(f"a is:{a},b is:{b}")
my_func()

"""
def temp_function():
    global a,b
    temp = a
    a = b
    b = temp
    print(f"a is:{a},b is:{b}")
temp_function()

"""
