from collections import deque
cups = deque([int(x) for x in input().split()])
bottles = [int(y) for y in input().split()]

total_water_left = 0

while cups and bottles:
    current_cup = cups[0]
    current_bottle = bottles[-1]
    if current_cup <= current_bottle:
        water_left = current_bottle - current_cup
        total_water_left += water_left
        current_cup = cups.popleft()
        current_bottle = bottles.pop()
    else:
        while not current_cup <= 0:
            if bottles:
                current_bottle = bottles.pop()
                current_cup -= current_bottle
        total_water_left += abs(current_cup)
        current_cup = cups.popleft()

if bottles:
    print(f"Bottles: {' '.join(map(str,bottles))}")
elif cups:
    print(f"Cups: {' '.join(map(str, cups))}")
print(f"Wasted litters of water: {total_water_left}")


