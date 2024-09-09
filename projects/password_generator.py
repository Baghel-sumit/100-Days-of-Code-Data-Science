# Generate password

import random

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',  # Lowercase
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'   # Uppercase
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
    '[', ']', '{', '}', '|', '\\', ';', ':', '\'', '"', ',', '.', '/', 
    '<', '>', '?', '`', '~'
]

finalPassword = ''

alphabetCount = int(input("how many alphabet characters do you want in password: "))

for _ in range(0, alphabetCount):
    randomCharacter = random.choice(alphabet)
    
    finalPassword += randomCharacter


numbersCount = int(input("How many numbers do you want in password: "))

for _ in range(0, numbersCount):
    randomNumber = random.choice(numbers)
    
    finalPassword += randomNumber


specialCharacterCount = int(input("How many special character do you want in password: "))

for _ in range(0, specialCharacterCount):
    randomSpecialCharacter = random.choice(special_characters)
    
    finalPassword += randomSpecialCharacter

def shuffleString(str):
    charList = list(str)
    
    random.shuffle(charList)
    
    return ''.join(charList)
    
print(f"you final password is: {shuffleString(finalPassword)}")