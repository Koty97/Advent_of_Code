import math
import os.path
from itertools import permutations, combinations
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])
def first(verbose=False):
    file = open("16.input", "r")
    board=[]
    start_pos=0
    end_pos=0
    for i,line in enumerate(file):
        board_line=[]
        for j,char in enumerate(line.strip()):
            if char=="#":
                board_line.append(0)
            elif char==".":
                board_line.append(1)
            elif char=="S":
                start_pos=(i,j)
                board_line.append(1)
            elif char == "E":
                end_pos = (i, j)
                board_line.append(1)
                pass
        board.append(board_line)
    print()
    return None


def second(verbose=False):
    file = open("16.input", "r")

    return None


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first(verbose=False)))
print("Result of Day {} Part 2: {}".format(current_day, second(verbose=True)))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
