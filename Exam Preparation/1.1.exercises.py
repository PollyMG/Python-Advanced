from collections import deque


def best_list_pureness(numbers, k):
    numbers = deque(numbers)
    best_pureness = {}
    for rotation in range(k + 1):
        result_sum = sum([index * number for index, number in enumerate(numbers)])
        best_pureness.update({rotation:result_sum})
        numbers.rotate()
    max_pureness = max(best_pureness.values())
    for key, value in best_pureness.items():
        if max_pureness == value:
            return f"Best pureness {value} after {key} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
