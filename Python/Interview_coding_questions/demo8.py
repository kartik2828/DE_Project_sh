 # What is the difference between deepcopy() and using copy() on a list of dictionaries?
'''
deepcopy creates a new object and recursively adds copies of nested objected.
copy.deepcopy() 


while copy() means shallow copy, shallow copy point to the same object in the memory
copy.copy()

'''

import copy 
original = [{'name':'kartik', 'age':23},{'name':'Abhinav', 'age':29}]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow[0]['age'] = 30
print("Original:", original)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)


