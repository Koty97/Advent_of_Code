import os.path

current_day = os.path.basename(__file__.split(".")[0])


def first(verbose=False):
    file = open("1.input", "r")
    left = []
    right = []
    summary = 0
    for line in file:
        if verbose: print("Reading {}".format(line.strip()))
        left.append(line.strip().split("   ")[0])
        right.append(line.strip().split("   ")[1])
        left.sort()
        right.sort()
    if verbose: print("Left {}".format(left))
    if verbose: print("Right {}".format(right))
    if len(left) == len(right):
        for i in range(0, len(left)):
            summary = summary + abs(int(left[i]) - int(right[i]))
    return summary


def second(verbose=False):
    file = open("1.input", "r")
    left = []
    right = []
    summary = 0
    for line in file:
        if verbose: print("Reading {}".format(line.strip()))
        left.append(line.strip().split("   ")[0])
        right.append(line.strip().split("   ")[1])
    if verbose: print("Left {}".format(left))
    if verbose: print("Right {}".format(right))
    if len(left) == len(right):
        for i in range(0, len(left)):
            summary = summary + right.count(left[i]) * int(left[i])
    return summary


print("Result of Day {} Part 1: {}".format(current_day, first()))
print("Result of Day {} Part 2: {}".format(current_day, second()))