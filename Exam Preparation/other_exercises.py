def get_magic_triangle(n):
    triangle = [[1], [1, 1]]

    for row_index in range(2, n):
        triangle.append([])
        triangle[-1].append(1)
        for column_index in range(1, row_index):
            triangle[-1].append(triangle[row_index - 1][column_index - 1] +\
            triangle[row_index - 1][column_index])
        triangle[-1].append(1)
    return triangle


print(get_magic_triangle(5))
print(get_magic_triangle(4))