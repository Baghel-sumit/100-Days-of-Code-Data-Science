# 1. Python program to check whether the string is Symmetrical or Palindrome
""" 
def is_palindrome(str):
    return str == str[::-1]

def is_symmetric(str):
    
    size = len(str)
    mid  = size // 2
    
    if (size % 2 == 0):
        return str[mid:] == str[:mid]
    else:
        return str[:mid] == str[mid + 1:]
    
def is_symmetric_two(str):
    mid = len(str) // 2
    
    return str[:mid] == str[-mid:]

str = "amaama"

if is_palindrome(str):
    print("Provided string is palindrome")
if is_symmetric_two(str):
    print("Provided string is symmetric")
    
    
"""
# 2. Reverse Words in a Given String in Python
""" 
sentence = "geeks quiz practice code"

newSentence = ' '.join(sentence.split()[::-1])

print(newSentence)

"""
# 3. How to Remove Letters From a String in Python


# (i) Replace method of string

str = "GeeksForGeeks"

""" 
print("After replacing e:", str.replace("e", ""))

print("After removing first occurrence of e", str.replace("e", "", 1))

n = 4

print(f"After removing {n} occurrences: ", str.replace("e", "", n))

"""

# (ii) translate method of string

