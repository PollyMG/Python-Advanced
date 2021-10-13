from collections import deque


def best_list_pureness(numbers, k):
    data = {}
    numbers = deque(numbers)
    for rotation in range(k + 1):
        if rotation == len(numbers):
            break
        result = sum([index * number for index, number in enumerate(numbers)])
        data.update({rotation: result})
        # numbers.appendleft(numbers.pop())
        numbers.rotate()
    max_pureness = max(data.values())
    for key, value in data.items():
        if max_pureness == value:
            return f"Best pureness {value} after {key} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
