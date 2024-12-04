import os.path
from time import perf_counter
import re

current_day = os.path.basename(__file__.split(".")[0])


def first(verbose=False):
    file = open("2.input", "r")
    summary = 0
    regex_string = "\\d+ "
    colors = ["red", "green", "blue"]
    for line in file:
        is_ok = True
        for color in colors:
            for match in re.findall(regex_string + color, line):
                if (color == "red" and int(match.split(" ")[0]) <= 12) or (
                        color == "green" and int(match.split(" ")[0]) <= 13) or (
                        color == "blue" and int(match.split(" ")[0]) <= 13):
                    pass
                else:
                    is_ok = False
        if is_ok == True:
            summary = summary + int(line.split(":")[0].split(" ")[1])
    return summary


def second(verbose=False):
    file = open("2.input", "r")
    summary = 0
    regex_string = "\\d+ "
    colors = ["red", "green", "blue"]
    for line in file:
        power=1
        for color in colors:
            biggest = 0
            for match in re.findall(regex_string + color, line):
                if int(match.split(" ")[0]) > biggest: biggest = int(match.split(" ")[0])
            if verbose: print("Biggest {} is {}".format(color, biggest))
            power=power*biggest
        summary=summary+power
    return summary


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first()))
print("Result of Day {} Part 2: {}".format(current_day, second()))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
