rows, columns = [int(x) for x in input().split()]
matrix = []
for row in range(rows):
    matrix.append([int(x) for x in input().split()])

max_sum = 0
best_row = 0
best_column = 0
for row in range(rows - 2):
    for col in range(columns - 2):
        current_sum = matrix[row][col] + \
                      matrix[row][col + 1] + \
                      matrix[row][col + 2] + \
                      matrix[row + 1][col] + \
                      matrix[row + 1][col + 1] + \
                      matrix[row + 1][col + 2] + \
                      matrix[row + 2][col] + \
                      matrix[row + 2][col + 1] + \
                      matrix[row + 2][col + 2]
        if current_sum >= max_sum:
            max_sum = current_sum
            best_row, best_column = row, col
print(f"Sum = {max_sum}")
print(matrix[best_row][best_column], matrix[best_row][best_column + 1], matrix[best_row][best_column + 2])
print(matrix[best_row + 1][best_column], matrix[best_row + 1][best_column + 1], matrix[best_row + 1][best_column + 2])
print(matrix[best_row + 2][best_column], matrix[best_row + 2][best_column + 1], matrix[best_row + 2][best_column + 2])
