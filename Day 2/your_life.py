""" 

input: float , your age
output: left days, weeks and years from 90 years

1 year total weeks - 52
1 year total days - 365

"""

age = float(input("Please provide your age: "))

leftYears = 90 - age
leftWeeks = leftYears * 52
leftDays = leftYears * 365

print(f"you have {leftYears} years, {leftWeeks} weeks and {leftDays} days")

