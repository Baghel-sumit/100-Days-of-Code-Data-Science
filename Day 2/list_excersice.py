# 1. Python program to interchange first and last elements in a list
""" 
my_list = [ 1,2,3,4,5,6,7,8,9,10 ]


my_list[0], my_list[-1] = my_list[-1], my_list[0]


print(my_list)

"""


# Using Temporary variable

""" 
def swapList(newList):
    size = len(newList)
    
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    
    return newList
    
my_list = [ 1,2,3,4,5,6 ]

print(swapList(my_list))

"""


# 2. Python Program to Swap Two Elements in a List

""" 
my_list = [ 1,2,3,4,5,6 ]

pos1, pos2 = 1, 2

my_list[pos1], my_list[pos2] = my_list[pos2], my_list[pos1]


print(my_list) 
"""

# using temp variable
""" 
my_list = [ 1,2,3,4,5 ]

pos1, pos2 = 1,2

temp = my_list[pos1]
my_list[pos1] = my_list[pos2]
my_list[pos2] = temp

print(my_list)

"""

# 3. Find the length of the list
""" 
my_list = [ 1,2,3,4,5,6,7,8,9,10 ]

print(len(my_list))

counter = 0

for i in my_list:
    counter += 1

print(counter)

"""

# 4. Maximum of two numbers
""" 
var1, var2 = 1,2

maximumNumber = var1 if var1 >= var2 else var2

print(maximumNumber)

"""

# Using max function
""" 
var1, var2 = 1, 2

maximumNumber = max(var1, var2)

print(maximumNumber)

"""

# 5. Minimum of two numbers
""" 
var1, var2 = 1, 3

minimumNumber = var1 if var1 <= var2 else var2

print("minimum Number:", minimumNumber)


# Using min function

var1, var2 = 1, 3

minimumNumber = min(var1, var2)

print("minimum Number:", minimumNumber)

"""
