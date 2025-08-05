

# What are the mutable and immutable types in python?

# Ans: list is mutable 

# eg. 
a = [1,2,3,4,5]
print(a)
a[3] = 90
print(a)


# sets are mutable 
c = {5,6,53,32,3}
c.add(100)
print(c)

# tuples are immutable 
b = (1,2,3,4)
print(b)


# Strings are immutable 
name  = 'kartik'
print('orginal name', name)

name  = name.replace('k','K')
print("after replace", name)

#===============================
'''
SUMMARY: Mutable => List, Set, dict
IMMU => tuple, str, int, float
'''