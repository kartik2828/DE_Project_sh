# Explain Shallow copy and deep copy

# Shallow copy 

a  = [1,2,3]

b= a 
print (a)
print (b)

# but let say if i want to change in list b that will affect my list a also

b[0] = 4
print(a)
print(b)
# -----------------------------------------------------------------------------------
import copy

# shallow
Team = [[1, 2], [3, 4]]

shallow = copy.copy(Team)

print(Team[0] is shallow[0])

# Deep
deep = copy.deepcopy(Team)
print(Team[0] is deep[0])