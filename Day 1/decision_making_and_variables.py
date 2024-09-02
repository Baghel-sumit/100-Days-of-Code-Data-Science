# Variables -> used to store data
# 1. int
# 2. float
# 3. string
# 4. bool

"""
    x = 4
    y = "JOHN"
    print(x, y)
"""

"""

Casting

If you want to specify the data type of a variable, this can be done with casting.

x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0


print(x, y, z)


Get the Type

You can get the data type of a variable with the type() function.

print("Type of x:", type(x))
print("Type of y:", type(y))
print("type of z:", type(z))

Single or Double Quotes?
String variables can be declared either by using single or double quotes:


x = "John"
y = 'John'

print(x, y, "See both are same")



Case-Sensitive
Variable names are case-sensitive.

a = 4
A = "John"
print(a, A)


# Assign multiple values to multiple variables

x, y, z = "variable1", "variable2", "variable3"

print(x, y, z)

x = y = z = "variable1"

print(x, y, z)

x, y, z = [ "variable1", "variable2", "variable3" ]

print(x, y, z)

# Global variables

def myfunc():
  print("Inside of function", x)
  
myfunc()


def myFunc():
    global globalVariable
    globalVariable = 10
    
    print("inside function", globalVariable)
    
myFunc()

print("outside function", globalVariable)
    
rangeVariable = range(6)

print("range", rangeVariable)


for x in "banana":
    print(x)
    
print(len("banan"))


txt = "It is very free for us to recognize that it is very easy for us."

if "free" in txt:
    print("Yes, 'free' is present.")
    
if "free" not in txt:
    print("No, 'free' is not present.")
    
    
print("printing txt ranging:", txt[0:9])

print("printing from start:", txt[:9])
print("printing from end:", txt[9:])
print("printing from start to end:", txt[9:], txt[:9])


# Negative indexing

print("printing in reverse order: ", txt[-11:-1])


#  String methods

print("Upper method:", txt.upper())
print("lower method:", txt.lower())
print("remove white space:", txt.strip())
print("replace a letter:", txt.replace(" ", ""))
print("split a string::", txt.split(" "))

print("Concetenation:", txt + "sumit")

print("encodeed string:", txt.encode())

"""


# Testing Boolean
""" 
print(10 > 9)

print(9 > 10)

a = 9
b= 10

if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")
    
print(bool("Hello"))

"""


# Python Operators

""" 
Python divides the operators in the following groups:

1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators
5. Identity operators
6. Membership operators
7. Bitwise operators



print("Addition:", 10 + 2)
print("Subtraction: ", 10 - 2)
print("Multiplication:", 10 * 2)
print("Division:", 10 /2 )
print("Modulus:", 10 % 2)
print("Exponentiation:", 10 **2 )
print("Floor Division", 10 // 2)


print("And Condition:", 10 > 9 and 10 == 10)
print("Or Condition:", 10 > 9 or 10 == 11)
print("Not condition:", not(10 > 9))



x = [ 1,2,3,4 ]
y = [ 1,2,3,4 ]

print("Compare", x is y)

print("Compare not", x is not y)



txt = "I'm free from now as the member of the universe"

print("Check membership", "free" in txt, "free" not in txt)

"""


# List -> Python list is used to store multiple items in a single variable.

thisList = [ "Apple", "Orange", "Banana", "Cherry", "Mango", "Apple" ]

print("LIst", thisList)

print("length", len(thisList))

print("type", type(thisList))

print("Access item", thisList[1])

print("last item", thisList[-1])

print("Range", thisList[2:5])

print("Leaving first index", thisList[:2])

print("Leaving end value", thisList[2:])

print("range of negative indexes:", thisList[-3:])

if "Apple" in thisList:
    print("yes, apple is present in this list")
    
