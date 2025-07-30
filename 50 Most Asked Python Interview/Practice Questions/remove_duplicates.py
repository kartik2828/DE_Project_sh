
# How do you remove duplicates from a list?

colors = ['red','green','yellow','red','green','white','blue']
uniq_list = []
"""
# by making list as a set 

uniq_lst = list(set(colors))
print(uniq_lst)

"""

for i in colors:
    if i not in uniq_list:
        uniq_list.append(i)

print(uniq_list)

