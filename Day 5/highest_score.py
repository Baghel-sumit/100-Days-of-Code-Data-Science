# Find out which student got the highest score

scores = input("Please enter the scores of each student: ").split()

highestScore = 0

for score in scores:
    modifiedScore = int(score)
    if (modifiedScore > highestScore):
        highestScore = modifiedScore


print("highest score: ", highestScore)