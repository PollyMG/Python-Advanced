from collections import deque
green_light_seconds = int(input())
free_window_seconds = int(input())
cars = deque()
cars_counter = 0
crashed = False

command = input()

while not command == "END":
    if command == "green":
        if cars:
            current_car = cars.popleft()
            seconds_left = green_light_seconds - len(current_car)
            while seconds_left > 0:
                cars_counter += 1
                if cars:
                    current_car = cars.popleft()
                    seconds_left -= len(current_car)
                else:
                    break
            if seconds_left == 0:
                cars_counter += 1
            if free_window_seconds >= abs(seconds_left):
                if seconds_left < 0:
                    cars_counter += 1
            else:
                car_was_hit_at = free_window_seconds + seconds_left
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[car_was_hit_at]}.")
                crashed = True
                break
    else:
        cars.append(command)
    command = input()
if not crashed:
    print("Everyone is safe.")
    print(f"{cars_counter} total cars passed the crossroads.")