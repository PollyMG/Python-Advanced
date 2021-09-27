from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
signs = deque(input().split())

total_honey = 0
while bees and nectar:
    bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar >= bee:
        current_sign = signs.popleft()
        if current_sign == "+":
            total_honey += abs(bee + current_nectar)
        elif current_sign == "-":
            total_honey += abs(bee - current_nectar)
        elif current_sign == "*":
            total_honey += abs(bee * current_nectar)
        elif current_sign == "/":
            if current_nectar > 0:
                total_honey += abs(bee / current_nectar)
    else:
        bees.appendleft(bee)
print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
