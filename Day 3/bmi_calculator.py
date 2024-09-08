height = int(input("Please provide your age: "))
weight = int(input("Please provide your weight: "))

bmi = round(weight / height ** 2, 2)

if (bmi < 18):
    print(f"your bmi is {bmi}, you are underweight")
elif (bmi >= 18 and bmi < 25):
    print(f"your bmi is {bmi}, you are normal weight")
elif (bmi >= 25 and bmi < 30):
    print(f"Your bmi is {bmi}, you are over weight")
elif (bmi >= 30 and bmi < 35):
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese")