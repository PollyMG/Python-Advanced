def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


word = input()
n = int(input())
matrix = [list(input()) for row in range(n)]
player_row, player_col = 0, 0
for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'P':
            player_row, player_col = row, col
commands_count = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
for com in range(commands_count):
    command = input()
    if command == "up":
        next_row = player_row + directions["up"][0]
        next_col = player_col + directions["up"][1]
        if not is_in_range(next_row, next_col, n):
            if word:
                word = word[:len(word) - 1]
                next_row, next_col = player_row, player_col
        else:
            if matrix[next_row][next_col] == "-":
                matrix[player_row][player_col] = matrix[next_row][next_col]
                matrix[next_row][next_col] = matrix[player_row][player_col]
            else:
                word = word + matrix[next_row][next_col]
                matrix[next_row][next_col] = "P"
                matrix[player_row][player_col] = "-"
            player_row, player_col = next_row, next_col

    if command == "down":
        next_row = player_row + directions["down"][0]
        next_col = player_col + directions["down"][1]
        if not is_in_range(next_row, next_col, n):
            if word:
                word = word[:len(word) - 1]
                next_row, next_col = player_row, player_col
        else:
            if matrix[next_row][next_col] == "-":
                matrix[player_row][player_col] = matrix[next_row][next_col]
                matrix[next_row][next_col] = matrix[player_row][player_col]
            else:
                word = word + matrix[next_row][next_col]
                matrix[next_row][next_col] = "P"
                matrix[player_row][player_col] = "-"
            player_row, player_col = next_row, next_col
    if command == "left":
        next_row = player_row + directions["left"][0]
        next_col = player_col + directions["left"][1]
        if not is_in_range(next_row, next_col, n):
            if word:
                word = word[:len(word) - 1]
                next_row, next_col = player_row, player_col
        else:
            if matrix[next_row][next_col] == "-":
                matrix[player_row][player_col] = matrix[next_row][next_col]
                matrix[next_row][next_col] = matrix[player_row][player_col]
            else:
                word = word + matrix[next_row][next_col]
                matrix[next_row][next_col] = "P"
                matrix[player_row][player_col] = "-"
            player_row, player_col = next_row, next_col
    if command == "right":
        next_row = player_row + directions["right"][0]
        next_col = player_col + directions["right"][1]
        if not is_in_range(next_row, next_col, n):
            if word:
                word = word[:len(word) - 1]
                next_row, next_col = player_row, player_col
        else:
            if matrix[next_row][next_col] == "-":
                matrix[player_row][player_col] = matrix[next_row][next_col]
                matrix[next_row][next_col] = matrix[player_row][player_col]
            else:
                word = word + matrix[next_row][next_col]
                matrix[next_row][next_col] = "P"
                matrix[player_row][player_col] = "-"
            player_row, player_col = next_row, next_col


print(word)
[print(''.join(pos)) for pos in matrix]




