# We'll calculate the true love

print("welcome to love calculator!!!")

name1 = input("What is your name ? ")
name2 = input("What is her name ? ")

fullName = name1.lower() + name2.lower()

trueCount = 0

for item in [ "t", "r", "u", "e" ]:
    trueCount += fullName.count(item)
    
loveCount = 0

for item in ["l", "o", "v", "e"]:
    loveCount += fullName.count(item)
    
trueLoveCount = int(f"{trueCount}{loveCount}")

if (trueLoveCount < 10 or trueLoveCount > 90):
    print(f"Your score is {trueLoveCount}, you go together like coke and mentos.")
elif (trueLoveCount >= 40 and trueLoveCount <= 50):
    print(f"Your score is {trueLoveCount}, you are alright together.")
else:
    print(f"Your score is {trueLoveCount}")