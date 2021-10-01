n = int(input())
matrix = []
for row in range(n):
    matrix.append([int(x) for x in input().split(', ')])
# flattening_matrix = []
# for row in matrix:
#     flattening_matrix.extend(row)
# print(flattening_matrix)
print([x for row in matrix for x in row])