import os.path
import re
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])


def shuffle_line(line, rules,verbose):
    pass


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
            if not is_ok:
                for i in range(0, 4):  # 🤮🤮🤮 but it works
                    for rule in rules:
                        if (rule.split("|")[0]) in line and (rule.split("|")[1] in line):
                            if verbose:
                                print("{} and {} is in {}".format(rule.split("|")[0], rule.split("|")[1], line))
                            is_ok = line.index(rule.split("|")[0]) < line.strip().index(
                                rule.split("|")[1])
                            if not is_ok:
                                line = line.replace(rule.split("|")[0], "XL")
                                line = line.replace(rule.split("|")[1], rule.split("|")[0])
                                line = line.replace("XL", rule.split("|")[1])
                                if verbose:
                                    print("notok", line)
                summary = summary + int(line.strip().split(",")[len(line.split(",")) // 2])
            if verbose: print("--------------------")
    file.close()
    return summary


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first()))
print("Result of Day {} Part 2: {}".format(current_day, second()))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
