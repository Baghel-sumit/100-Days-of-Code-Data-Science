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
    
    totalPrice = 12
    
    if (age < 12):
        print("child tickets are $5")
        totalPrice = 5
    elif (age <= 18):
        print("Youth tickets are $7")
        totalPrice = 7
    else:
        print("Adult tickets are $12")
        
    wants_photo = input("Do want a photo taken ? type Y or N - ")
    
    if (wants_photo == "Y" or wants_photo == "y"):
        print(f"Your total price is : ${totalPrice + 3}")
    else:
        print(f"Your total bill is : ${totalPrice}")
        
else:
    print("Sorry, you can't ride on roller coster.")
