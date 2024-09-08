# Calculate the leap year

""" 
input: a year 
output: find out whether the provided year is a leap year or not

"""

year = int(input("Please enter a year: "))

if (year % 4 == 0 and year % 100 != 0):
    print("Provided year is a leap year")
elif (year % 400 == 0):
    print("provided year is a leap year")
else:
    print("Provided year is not a leap year")