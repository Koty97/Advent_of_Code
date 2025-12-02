import math
import os.path
from itertools import permutations, combinations
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])
def first(verbose=False):
    file = open("18.input", "r")
    sizex=7
    sizey=7
    board=[['.' for i in range(sizex)] for j in range(sizey)]
    bits_to_simulate=12
    for i,line in enumerate(file):
        board[int(line.split(",")[1])][int(line.split(",")[0])]="#"
        if i==bits_to_simulate-1:
            break
    print()
    return None


def second(verbose=False):
    file = open("18.input", "r")

    return None


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first(verbose=False)))
print("Result of Day {} Part 2: {}".format(current_day, second(verbose=True)))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
