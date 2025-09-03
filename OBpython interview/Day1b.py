
# Reverse a string without using built-in functions

def rev_string(w):
    rev = ""
    for i in w:
        rev = i + rev
    return rev

print(rev_string('Hello_brother'))
    

