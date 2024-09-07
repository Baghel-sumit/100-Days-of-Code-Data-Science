""" 

BMI = weight(kg) / height ^ 2

"""

weight = float(input("Please tell us your weight in kg: "))

height = float(input("Please enter your height in m: "))


print("BMI: ", int(weight / (height ** 2)))


# Rounding off the number

print(round(5 / 3, 2))

print(5 // 3) # Floor Division

# Increment 

score = 2

score += 3

print("increment", score)

# F-strings

print(f"increment data with f-string {score}")