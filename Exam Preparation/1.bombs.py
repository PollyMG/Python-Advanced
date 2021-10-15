from collections import deque

bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]

datura_bombs = 0
cherry_bombs = 0
smoke_decoy_bombs = 0

succeed = False

while True:
    if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_decoy_bombs >= 3:
        succeed = True
        break

    if not bomb_effects or not bomb_casings:
        break

    current_bomb_effect = bomb_effects[0]
    current_bomb_casting = bomb_casings[-1]
    sum_bombs = current_bomb_effect + current_bomb_casting

    if sum_bombs == 40:
        datura_bombs += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif sum_bombs == 60:
        cherry_bombs += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif sum_bombs == 120:
        smoke_decoy_bombs += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        current_bomb_casting -= 5
        bomb_casings.pop()
        bomb_casings.append(current_bomb_casting)

if succeed:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")
else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bombs}")