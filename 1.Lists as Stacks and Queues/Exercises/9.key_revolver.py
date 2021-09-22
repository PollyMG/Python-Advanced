from collections import deque
price_bullet = int(input())
size_gun_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
value_of_intelligence = int(input())
shots_count = size_gun_barrel

while locks and bullets:
    current_bullet = bullets.pop()
    current_lock = locks[0]
    shots_count -= 1
    value_of_intelligence -= price_bullet
    if current_lock >= current_bullet:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")
    if shots_count == 0 and bullets:
        print("Reloading!")
        shots_count = size_gun_barrel

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${value_of_intelligence}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
