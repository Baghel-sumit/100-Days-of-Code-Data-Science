print("Welcome to roller coster ride!!!")

height = int(input("Please enter your height in cm: "))

if (height >= 120):
    age = int(input("Please enter your age: "))
    if (age > 18):
        print("you can ride as well as adult.")
    else:
        print("you can ride but you are not adult.")
else:
    print("Sorry, you can't ride on roller coster.")



# Check whether the provided number is an odd number or even number

number = int(input("Enter any integer: "))

if (number % 2 == 0):
    print("Provided number is even number")
else:
    print("Provided number is odd number")
    
    
# if else ladder

print("Welcome to roller coster ride!!!")

height = int(input("Please enter your height in cm: "))

if (height >= 120):
    age = int(input("Please enter your age: "))
    if (age < 12):
        print("U are under 12")
    elif (age > 18):
        print("you can ride as well as adult.")
    elif (age > 22):
        print("You can ride roller coaster and you are more than 22")
    else:
        print("you can ride but you are not adult.")
else:
    print("Sorry, you can't ride on roller coster.")
