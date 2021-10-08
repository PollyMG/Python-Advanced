matrix = [[int(x) for x in input().split()] for row in range(int(input()))]

command = input()
while not command == "END":
    name, row, col, value = command.split()
    value = int(value)
    row = int(row)
    col = int(col)
    if name == "Add" and row in range(len(matrix)) and col in range(len(matrix)):
        matrix[row][col] += value
    elif name == "Subtract" and row in range(len(matrix)) and col in range(len(matrix)):
        matrix[row][col] -= value
    else:
        print("Invalid coordinates")
    command = input()

for r in range(len(matrix)):
    for c in range(len(matrix)):
        print(matrix[r][c], end=' ')
    print()