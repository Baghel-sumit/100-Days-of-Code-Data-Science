# Who will pay the bill ?
import random

nameString = input("Please enter the names by comma separation -> ")

namesList = nameString.split(", ")

randomIndex = random.randint(0, len(namesList) - 1)

print(f"Today, {namesList[randomIndex]} is going to pay the bill")

# with choice method

print(f"Today, {random.choice(namesList)} is going to pay the bill")