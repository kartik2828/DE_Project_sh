# Count vowels and consonants in a string

def count_vowels_consonants(s):
    vowels = 'aeiou'

    v_count = 0
    c_count = 0

    for i in s.lower():
        if i.isalpha():
            if i in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

v, c = count_vowels_consonants("Kartik Sharma")
print("vowels", v)
print("consonants", c)