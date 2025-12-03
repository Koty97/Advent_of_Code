import os.path
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])


def common(element_count, verbose=False):
    file = open("{}.input".format(current_day), "r")
    summary = 0
    for i, line in enumerate(file):
        line = line.strip()
        element_count = element_count
        length = len(line)
        max_length = length - element_count + 1
        max_val = [0] * element_count
        index = [0] * element_count
        for j in range(0, max_length):
            if int(line[j]) > max_val[0]:
                max_val[0] = int(line[j])
                index[0] = j
        for x in range(0, element_count - 1):
            max_length = max_length + 1
            for j in range(index[x] + 1, max_length):
                if int(line[j]) > max_val[x + 1]:
                    max_val[x + 1] = int(line[j])
                    index[x + 1] = j
        if verbose: print(max_val)
        max_str = "".join(str(i) for i in max_val)
        summary = summary + int(max_str)
        if verbose: print(index)
        if verbose: print("-------------")
    return summary


def first_old(verbose=False):
    file = open("{}.input".format(current_day), "r")
    summary = 0
    for line in file:
        max_numbers = [0, 0]
        max_indexes = [0, 0]
        for i, char in enumerate(line.strip()):
            if int(char) > max_numbers[0]:
                if max_numbers[0] > max_numbers[1]:
                    max_numbers[1] = max_numbers[0]
                    max_indexes[1] = max_indexes[0]
                max_numbers[0] = int(char)
                if i < len(line.strip()) - 1:
                    max_numbers[1] = 0
                max_indexes[0] = i
            elif int(char) > max_numbers[1]:
                max_numbers[1] = int(char)
                max_indexes[1] = i
        if verbose: print("N:", max_numbers)
        if verbose: print("I:", max_indexes)
        if max_indexes[0] > max_indexes[1]:
            temp = max_numbers.pop()
            max_numbers.append(max_numbers[0])
            max_numbers[0] = temp
            if verbose: print("\tFixing order")
            if verbose: print("N:", max_numbers)
        summary = summary + int("{}{}".format(max_numbers[0], max_numbers[1]))
        if verbose: print("--------------")
    return summary


def first(verbose=False):
    return common(2, verbose)


def second(verbose=False):
    return common(12, verbose)


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first()))
print("Result of Day {} Part 2: {}".format(current_day, second()))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
