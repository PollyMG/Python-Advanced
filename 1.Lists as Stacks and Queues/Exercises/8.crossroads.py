from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()
passed_cars = 0

crashed = False
while not crashed:
    command = input()
    if command == "END":
        break
    if command == "green":
        current_green_light = green_light
        while cars and current_green_light > 0:
            car = cars.popleft()
            if current_green_light >= len(car) or \
                    current_green_light + free_window >= len(car):
                passed_cars += 1
                current_green_light -= len(car)
            else:
                print("A crash happened!")
                print(f'{car} was hit at {car[current_green_light + free_window]}.')
                crashed = True
                break
    else:
        cars.append(command)
if not crashed:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")