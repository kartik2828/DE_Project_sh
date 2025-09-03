# Most Asked Python Questions for Data Engineer
# Ques1) Check if a string is Palindrome

def check_palindrome(s):
    s = s.lower()
    return s == s[::-1]
obj = check_palindrome('Nitin')
obj1 = check_palindrome('Hello')

print(obj)
print(obj1) 
