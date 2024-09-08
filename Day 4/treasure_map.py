# We are going to code treasure map

row1 = [ "💬", "💬", "💬" ]
row2 = [ "💬", "💬", "💬" ]
row3 = [ "💬", "💬", "💬" ]

map = [ row1, row2, row3 ]

print(f"Here is your treasure map \n{row1}\n{row2}\n{row3}")

position = input("Where do you want to keep your treasure with a space ? ")

[ firstIndexStr, secondIndexStr ] = position.split()

firstIndex = int(firstIndexStr) - 1
secondIndexStr = int(secondIndexStr) - 1

map[firstIndex][secondIndexStr] = '👑'

print(f"Here is your new treasure\n{map}")