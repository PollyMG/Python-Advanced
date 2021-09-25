count = int(input())
cars = set()
for _ in range(count):
    direction, car = input().split(', ')
    if direction == "IN":
        cars.add(car)
    elif direction == "OUT":
        cars.discard(car)

if cars:
    [print(car) for car in cars]
else:
    print("Parking Lot is Empty")