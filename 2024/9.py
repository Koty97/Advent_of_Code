import os.path
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])


def first(verbose=False):
    file = open("9.input", "r")
    disk = []
    id=0
    free_space = False
    while True:
        number = file.read(1)
        if number!="":
            if free_space:
                if number!=str(0):
                    disk.append(int(number)*".")
            else:
                disk.append(int(number)*str(id))
                id=id+1
            free_space = not free_space
        if not number:
            break
    print(disk)
    for i,element in enumerate(disk):
        if "." in element:
            disk[i]="X"
    print(disk)
    summary = 0
    return summary


def second(verbose=False):
    file = open("9.input", "r")
    matrix = []
    summary = 0
    return summary


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first(verbose=False)))
print("Result of Day {} Part 2: {}".format(current_day, second()))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
