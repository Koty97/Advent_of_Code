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


# For Day 4
def is_winning_board(board):
    winning_line = len(board) * ["X"]
    for line in board:
        if line == winning_line:
            return True
    for x in range(0, len(board)):
        column = []
        for line in board:
            column.append(line[x])
        if column == winning_line:
            return True
        column = []
    return False


# For Day 4
def get_board_result(board, called_number):
    result = 0
    for line in board:
        for number in line:
            if number != "X":
                result = result + int(number)
    return result * int(called_number)
