#nested loop

rows = int(input("How many rows do you want: "))
columns = int(input("How many columns do you want: "))
symbol = input("Please input the symbol to be used: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ")
    print()