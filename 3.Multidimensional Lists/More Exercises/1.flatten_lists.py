# matrix = [[int(x) for x in row.split()] for row in input().split('|') ]
#
# flatten_lists = []
#
# for row in range(len(matrix)-1, -1, -1):
#     for col in range(len(matrix[row])):
#         flatten_lists.append(matrix[row][col])
# print(' '.join(map(str, flatten_lists)))

sublists = input().split('|')
result = []
for idx in range(len(sublists) - 1, -1, -1):
    elements = sublists[idx].split()
    result += elements

print(' '.join(result))
