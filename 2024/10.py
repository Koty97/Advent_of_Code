import os.path
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])


def first(verbose=False):
    file = open("10.input", "r")
    numbers = []
    for line in file:
        numbers.append(int(line.strip()))
    numbers.append(0)
    numbers.append(max(numbers) + 3)
    numbers.sort()
    if verbose: print("Sorted numbers: {}".format(numbers))
    differences = {}
    for i, number in enumerate(numbers):
        try:
            if verbose: print(
                "Difference between {} and {} is {}".format(number, numbers[i + 1], numbers[i + 1] - number))
            if differences.get(numbers[i + 1] - number) is None:
                differences[numbers[i + 1] - number] = 0
            differences[numbers[i + 1] - number] = differences[numbers[i + 1] - number] + 1
        except:
            pass
    if verbose: print("Differences are: {}".format(differences))
    return differences[1] * differences[3]


def second(verbose=False):
    file = open("10.input", "r")
    numbers = []
    for line in file:
        numbers.append(int(line.strip()))
    numbers.append(0)
    numbers.append(max(numbers) + 3)
    numbers.sort()
    print(numbers)
    possible_nodes = {}
    summary=0
    for i, number in enumerate(numbers):
        filt=list(filter(lambda x: (0 < x - number <= 3), numbers))
        if len(filt)!=0:
            possible_nodes[number] = filt
    for element in possible_nodes.items():
        print(element)
    print(possible_nodes)
    return None


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first(verbose=False)))
print("Result of Day {} Part 2: {}".format(current_day, second()))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
