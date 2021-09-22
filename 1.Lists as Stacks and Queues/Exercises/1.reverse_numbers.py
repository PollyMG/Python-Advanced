stack = input().split()

reverse_stack = []
while stack:
    # removed_el = stack.pop()
    # reverse_stack.append(removed_el)
    reverse_stack.append(stack.pop())
print(' '.join(reverse_stack))