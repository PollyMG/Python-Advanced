number_of_guests = int(input())
guests_list = set()
for _ in range(number_of_guests):
    guests_list.add(input())

command = input()
while not command == "END":
    if command in guests_list:
        guests_list.remove(command)
    command = input()
print(len(guests_list))


def is_vip(guest):
    return guest[0].isdigit()


vip_guests = sorted([x for x in guests_list if is_vip(x)])
regular_guests = sorted([y for y in guests_list if not is_vip(y)])
[print(g) for g in vip_guests]
[print(g) for g in regular_guests]
