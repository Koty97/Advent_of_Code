import os.path
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])


def first(verbose=False):
    file = open("1.input", "r")
    pointer = 50
    summary = 0
    for line in file:
        if verbose: print("Reading {}".format(line.strip()))
        line = line.strip().replace("L", "-").replace("R", "+")
        pointer = pointer + int(line) % 100
        if pointer < 0:
            pointer = 100 + pointer
        elif pointer > 99:
            pointer = 0 + (pointer - 100)
        if pointer == 0:
            summary = summary + 1
        if verbose: print("New pointer value =  {}".format(pointer))
    return summary


def second(verbose=False):
    file = open("1.input", "r")
    pointer = 50
    summary = 0
    divs = []
    for line in file:
        if verbose: print("Reading {}".format(line.strip()))
        mode = line[0]
        line = line.strip().replace("L", "").replace("R", "")
        turns = int(line)
        division = turns // 100
        if verbose and division != 0: print("\tAdding {} full sets".format(division))
        summary = summary + division
        modulo = turns % 100
        if mode == "L":
            if pointer - modulo < 0:
                if pointer != 0 and (pointer - modulo) % 100 != 0:
                    summary = summary + 1
                pointer = (pointer - modulo) % 100
            else:
                pointer = pointer - modulo
        else:
            if pointer + modulo > 99:
                if pointer != 0 and (pointer + modulo) % 100 != 0:
                    summary = summary + 1
                pointer = (pointer + modulo) % 100
            else:
                pointer = pointer + modulo
        if pointer == 0:
            summary = summary + 1
        if verbose: print("\tNew pointer value =  {}".format(pointer))
    return summary


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first()))
print("Result of Day {} Part 2: {}".format(current_day, second(verbose=True)))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
