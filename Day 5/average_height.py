# calculate average height

heights = input("Please enter persons' heights: ").split()

for index in range(0, len(heights)):
    heights[index] = int(heights[index])


sumOfHeights = 0

for personH in heights:
    sumOfHeights += personH

print("Average of height: ", sumOfHeights / len(heights))