rows, columns = [int(x) for x in input().split()]
word = input()
matrix = []
word_index = 0
for row in range(rows):
    matrix.append([None] * columns)
    for col in range(columns):
        if row % 2 == 0:
            matrix[row][col] = word[word_index]
        else:
            matrix[row][columns - 1 - col] =  word[word_index]
        word_index = (word_index + 1) % len(word)
[print(''.join(x)) for x in matrix]