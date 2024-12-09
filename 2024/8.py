import os.path
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])
def first(verbose=False):
    file = open("6.input", "r")
    matrix = []
    visited_fields = []
    direction = 0
    summary=0
    return summary


def second(verbose=False):
    file = open("6.input", "r")
    matrix = []
    summary=0
    return summary


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first(verbose=False)))
print("Result of Day {} Part 2: {}".format(current_day, second()))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
