import os.path
import re

current_day = os.path.basename(__file__.split(".")[0])


def first(verbose=False):
    file = open("6.input", "r")
    summary = 1
    pattern = "\\w*:\\s+(\\d+)\\s+(\\d+)\\s+(\\d+)\\s+(\\d+)"
    arr_time = list(re.findall(pattern, file.readline())[0])
    arr_distance = list(re.findall(pattern, file.readline())[0])
    for iterator in range(0, len(arr_time)):
        count = 0
        for x in range(0, int(arr_time[iterator])):
            if verbose: print(
                "With holding button for {}ms I could travel {}mm".format(x, (int(arr_time[iterator]) - x) * x))
            if (int(arr_time[iterator]) - x) * x > int(arr_distance[iterator]):
                if verbose: print("\tThis is better strategy")
                count = count + 1
        summary = summary * count
        if verbose: print("------------")
    return summary


def second(verbose=False):
    file = open("6.input", "r")
    summary = 0
    pattern = "\\w*:\\s+(\\d+)\\s+(\\d+)\\s+(\\d+)\\s+(\\d+)"
    time = list(re.findall(pattern, file.readline())[0])
    time = int("".join(time))
    distance = list(re.findall(pattern, file.readline())[0])
    distance = int("".join(distance))
    for x in range(0, time):
        if verbose: print(
            "With holding button for {}ms I could travel {}mm".format(x, (time - x) * x))
        if verbose: print("Comparing ")
        if (time - x) * x > distance:
            if verbose: print("\tThis is better strategy")
            summary = summary + 1
    return summary


print("Result of Day {} Part 1: {}".format(current_day, first()))
print("Result of Day {} Part 2: {}".format(current_day, second()))
