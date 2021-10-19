from collections import deque

fire_effects = deque([int(x) for x in input().split(', ')])
fire_power = [int(x) for x in input().split(', ')]

palm_count = 0
willow_count = 0
crossette_count = 0
succeed = False
while True:
    if palm_count >= 3 and willow_count >= 3 and crossette_count >= 3:
        succeed = True
        break
    if not fire_power or not fire_effects:
        break

    cur_effect = fire_effects[0]
    cur_power = fire_power[-1]
    if cur_effect <= 0:
        fire_effects.popleft()
        continue
    if cur_power <= 0:
        fire_power.pop()
        continue

    sum = cur_effect + cur_power
    if sum % 3 == 0 and sum % 5 == 0:
        crossette_count += 1
        fire_power.pop()
        fire_effects.popleft()
    elif sum % 3 == 0:
        palm_count += 1
        fire_power.pop()
        fire_effects.popleft()
    elif sum % 5 == 0:
        willow_count += 1
        fire_power.pop()
        fire_effects.popleft()
    else:
        cur_effect -= 1
        fire_effects.popleft()
        fire_effects.append(cur_effect)

if succeed:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if fire_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in fire_effects])}")
if fire_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in fire_power])}")
print(f"Palm Fireworks: {palm_count}")
print(f"Willow Fireworks: {willow_count}")
print(f"Crossette Fireworks: {crossette_count}")