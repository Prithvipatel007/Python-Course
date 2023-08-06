row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to put the treasure?")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

#col = int(position) // 10   # returns int
#row = int(position) % 10

#map[row-1][col-1] = "X"

#print(f"{row1}\n{row2}\n{row3}")
