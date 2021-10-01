rows, columns = [int(x) for x in input().split(', ')]

matrix = []
for row in range(rows):
    matrix.append([int(x) for x in input().split()])

# for col in range(columns):
#     current_sum = 0
#     for row in range(rows):
#         current_sum += matrix[row][col]
#     print(current_sum)
columns_sum = [0] * columns
for row in range(rows):
    for col in range(columns):
        value = matrix[row][col]
        columns_sum[col] += value
for el in columns_sum:
    print(el)
