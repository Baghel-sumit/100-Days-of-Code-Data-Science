# Calculate pizza price

""" 

Small pizza - $15
Medium Pizza - $20
Large Pizza - $25

Pepperoni for small pizza = +$2
pepperoni for medium and large pizza = +$3

Extra cheese for any size of pizza = +$1


inputs - 

size = size of pizza = S ( small ), L ( Large ) and M ( Medium )
add_pepperoni = Y or N
extra_cheese = Y or N

output - 

total price of pizza

"""

small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25

pepperoni_for_small_size = 2
pepperoni_for_large_and_medium_size = 3

extra_cheese_price = 1

totalBill = 0

# inputs - 

size = input("Please tell us what size of pizza do you want to order\n Type s for small size\n Type l for large size\n Type m for medium size\n => ")
add_pepperoni = input("Do you want to add pepperoni?\n Type y for yes\n Type n for no\n => ")
extra_cheese = input("Do you want to add extra cheese?\n Type y for yes\n Type n for no\n => ")

if (size == 's'):
    totalBill += small_pizza_price
    if (add_pepperoni == 'y'):
        totalBill += pepperoni_for_small_size
elif (size == 'm'):
    totalBill += medium_pizza_price
    if (add_pepperoni == 'y'):
        totalBill += pepperoni_for_large_and_medium_size
else:
    totalBill += large_pizza_price
    if (add_pepperoni == 'y'):
        totalBill += pepperoni_for_large_and_medium_size
        
if (extra_cheese == 'y'):
    totalBill += extra_cheese_price


print(f"Your total bill is {totalBill}")