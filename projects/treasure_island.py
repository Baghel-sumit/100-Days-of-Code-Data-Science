# Treasure island

print("Welcome to Treasure Island\nYour mission is to find the treasure")

leftOrRight = input("You are at a cross road. where do you want to go? Type 'left' or 'right' => ")

if (leftOrRight == "left"):
    swimOrWait = input("Type 'swim' if you want to go like swim , or type wait if you want to wait for boat ")
    
    if (swimOrWait == "swim"):
        doorName = input("Now you have three door in front of you,\ntype 'red' to choose red door\ntype 'blue' to choose blue door\ntype 'yellow' to choose yellow door\n=> ")
        
        if (doorName == "yellow"):
            print("you won the game!!!")
        else:
            print("Game over!!! sorry better luck next time")
    else:
        print("Game over!!! sorry better luck next time")
else:
    print("Game over!!! sorry better luck next time")
    