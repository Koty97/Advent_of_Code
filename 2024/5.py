import os.path
import re
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])


def first(verbose=False):
    file = open("5.input", "r")
    summary = 0
    rules = []
    for line in file:
        if "|" in line:
            rules.append(line.strip())
        elif "," in line:
            is_ok = True
            for number in line.split(","):
                for rule in rules:
                    if number in rule:
                        try:
                            is_ok = is_ok and line.strip().index(rule.split("|")[0]) < line.strip().index(
                                rule.split("|")[1])
                            if verbose: print(
                                "{} and {} in {} is ok: {}".format(rule.split("|")[0], rule.split("|")[1], line.strip(),
                                                                   is_ok))
                        except:
                            pass
            if is_ok:
                if verbose: print("For {} printing {}".format(line, line.strip().split(",")[len(line.split(",")) // 2]))
                summary = summary + int(line.strip().split(",")[len(line.split(",")) // 2])
            if verbose: print("--------------------")
    file.close()
    return summary


def second(verbose=False):
    file = open("5.input", "r")
    summary = 0
    rules = []
    file.close()
    return summary


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first()))
print("Result of Day {} Part 2: {}".format(current_day, second()))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
