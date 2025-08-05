
# Explain the difference between *args and **kwargs in Python.
'''
1) *args = in this we can pass multiple argument. without declaring them in the function.
2) **kwargs = in this we can pass multiple argumemnts in the form of key-value pair.
'''
def demo_function(*sum):
    result = 0
    for i in sum:
        result += i
    return result
obj1 = demo_function(1,2,3,4,5)
print(obj1)


def demo_function_with_kwargs(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}={value}")
obj  = demo_function_with_kwargs(name="kartik",age=23, city="Pune")
print(obj)

    
