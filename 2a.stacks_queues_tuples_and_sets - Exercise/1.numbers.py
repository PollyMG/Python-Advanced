first = set([int(x) for x in input().split()])
second = set([int(y) for y in input().split()])
n = int(input())
for _ in range(n):
    line = input().split()
    command = line[0]
    command_set = line[1]
    if command == "Add" and command_set == "First":
        [first.add(int(x)) for x in line[2:]]
    elif command == "Add" and command_set == "Second":
        [second.add(int(y)) for y in line[2:]]
    elif command == "Remove" and command_set == "First":
        current_set = set([int(x) for x in line[2:]])
        first = first.difference(current_set)
    elif command == "Remove" and command_set == "Second":
        current_set = set([int(y) for y in line[2:]])
        second = second.difference(current_set)
    else:
        print(first.issubset(second) or second.issubset(first))
print(', '.join(str(x) for x in sorted(first)))
print(', '.join(str(x) for x in sorted(second)))

