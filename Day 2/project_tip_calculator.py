""" 

inputs - 
1. Take the amount of total bill
2. Take the percentage of tip share
3. Count of persons

output - 
1. Provide the bill amount for each person has to pay with tip share

"""

totalBill = float(input("Enter total bill amount: "))
tipShare = int(input("Enter the percentage of tip: "))
totalPersons = int(input("Enter the total number of people: "))

singlePersonShare = ( totalBill + ( tipShare / 100 ) ) / totalPersons

print("single person share: ", singlePersonShare)