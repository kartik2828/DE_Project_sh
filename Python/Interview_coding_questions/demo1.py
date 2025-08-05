'''
You are given a list if numbers. Write a python function to return a new list contining only the 
even numbers from the original list.
'''

numbers = [1,2,3,4,5,5,6,7,8,9,10]

def even_number():
    list = []
    for i in numbers:
        if i%2==0:
            list.append(i)
    return list

result = even_number()
print(result)        