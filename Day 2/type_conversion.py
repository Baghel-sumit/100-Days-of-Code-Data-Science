# How to get the type of data

print(type("hello"))
print(type(3445))
print(type(34.345))
print(type(False))

# type conversion while taking output ( type casting )


str = input("Enter string: ")

integerData = int(input("Enter any integer: "))

floatData = float(input("Enter any float: "))

booleanData = bool(input("Enter any bool object"))

print("All Data types", type(str), type(integerData), type(floatData), type(booleanData))



# Sum of digits of a two digits number

number = int(input("Please provide a two digit number: "))

secondDigit = int(number % 10)
firstDigit = int(number // 10)

print("Sum of digits: ", secondDigit + firstDigit)