

# Check if a number is prime

def prime_num(num):
    if num<2:
        return False
    for i in range(2,num-1):
        if num%i == 0:
            return False
    return True
obj = prime_num(13)
print(obj)
