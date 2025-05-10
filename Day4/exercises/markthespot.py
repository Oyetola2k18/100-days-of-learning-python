#uhmhm X marks the spot

row1 = ["❤️","❤️","❤️"]
row2 = ["❤️","❤️","❤️"]
row3 = ["❤️","❤️","❤️"]

map = [row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want the treasure?[ColumnRow]")

column =  position[0]
row = position[1]

deducted_col= (int(column)) - 1
deducted_row= (int(row)) - 1
map[deducted_row][deducted_col] = "X"

print(f"{row1}\n{row2}\n{row3}")

