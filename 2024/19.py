import math
import os.path
from itertools import permutations, combinations
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])
def first(verbose=False):
    file = open("19.input", "r")
    available = []
    designs = []
    possible=[]
    max_length = 0
    for line in file:
        if "," in line:
            for design in line.split(","):
                if len(design.strip())>max_length:
                    max_length=len(design.strip())
                available.append(design.strip())
        elif line.strip() != "":
            designs.append(line.strip())
    print(available)
    print(designs)
    for design in designs:
        last_break=0
        for i in range(0,len(design)):
            searched_word=design[last_break:i+1]
            print("Searching for {}".format(searched_word))
            if searched_word in available:
                last_break=i+1
                #possible.append(design)


    return None


def second(verbose=False):
    file = open("19.input", "r")

    return None


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first(verbose=False)))
print("Result of Day {} Part 2: {}".format(current_day, second(verbose=True)))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
