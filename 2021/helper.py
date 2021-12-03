# For Day 1
def add_to_stack(stack, a):
    stack.pop(0) if len(stack) == 3 else 0
    stack.append(a)
    return stack


# For Day 1
def sum_stack(stack):
    return stack[0] + stack[1] + stack[2] if len(stack) == 3 else 0


# For Day 3
def get_most_common(line_list, position):
    num_of_steps = 0
    value = 0
    for line in line_list:
        value = value + int(line[position])
        num_of_steps = num_of_steps + 1
    if value < num_of_steps / 2:
        return 0
    elif value > num_of_steps / 2:
        return 1
    else:
        return 1
