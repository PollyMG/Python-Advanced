def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


def searched_matrix(matrix, search):
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if char == search:
                return y, x


n = int(input())
matrix = [list(input()) for row in range(n)]
# for row in range(n):
#     row_data = list(input())
#     matrix.append(row_data)


food_quantity = 0

snake_row, snake_col = searched_matrix(matrix, 'S')

directions = {
     "up": (-1, 0),
     "down": (1, 0),
     "left": (0, -1),
     "right": (0, 1),
}
out_territory = False
snake_movements = []
while is_in_range(snake_row, snake_col, n):
    if food_quantity == 10:
        break
    direction = input()
    if direction in directions:
        next_snake_row = snake_row + directions[direction][0]
        next_snake_col = snake_col + directions[direction][1]

        if not is_in_range(next_snake_row, next_snake_col, n):
            matrix[snake_row][snake_col] = '.'
            out_territory = True
            break

        if matrix[next_snake_row][next_snake_col] == "*":
            food_quantity += 1
            matrix[snake_row][snake_col] = '.'
            snake_row, snake_col = next_snake_row, next_snake_col
            matrix[next_snake_row][next_snake_col] = 'S'
            continue

        if matrix[next_snake_row][next_snake_col] == "B":
            matrix[snake_row][snake_col] = '.'
            matrix[next_snake_row][next_snake_col] = '.'
            new_snake_row, new_snake_col = searched_matrix(matrix, 'B')
            matrix[new_snake_row][new_snake_col] = 'S'
            snake_row, snake_col = new_snake_row, new_snake_col
            continue
        matrix[snake_row][snake_col] = '.'
        snake_row, snake_col = next_snake_row, next_snake_col
        matrix[snake_row][snake_col] = 'S'

if out_territory:
    print("Game over!")
    print(f"Food eaten: {food_quantity}")
if food_quantity == 10:
    print("You won! You fed the snake.")
    print(f"Food eaten: {food_quantity}")
[print(''.join(pos)) for pos in matrix]