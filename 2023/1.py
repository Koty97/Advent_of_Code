import os.path
import re

current_day = os.path.basename(__file__.split(".")[0])


def first(verbose=False):
    file = open("1.input", "r")
    summary = 0
    for line in file:
        if verbose: print("Reading {}".format(line.strip()))
        pattern = "(\\d)"
        digits = re.findall(pattern, line)
        if len(digits) > 0:
            if verbose: print("Found: {} - ".format(digits[0], digits[len(digits) - 1]))
            number = digits[0] + digits[len(digits) - 1]
            number = int(number)
        else:
            number = 0
        if verbose: print("Old sum: {}".format(summary))
        if verbose: print("Adding: {}".format(number))
        summary = summary + number
        if verbose: print("New sum: {}".format(summary))
        if verbose: print("--------------------------")
    return summary


def second(verbose=False):
    number_words = {"zero": 0,
                    "one": 1,
                    "two": 2,
                    "three": 3,
                    "four": 4,
                    "five": 5,
                    "six": 6,
                    "seven": 7,
                    "eight": 8,
                    "nine": 9}
    file = open("1.input", "r")
    summary = 0

    pattern = "(?=("
    for word in list(number_words.keys()):
        pattern = pattern + "{}|".format(word)
        pass
    pattern = pattern + "\\d))"
    if verbose: print("Created pattern {}".format(pattern))
    for line in file:
        if verbose: print("Reading {}".format(line.strip()))
        digits = re.findall(pattern, line)
        number_a = 0
        number_b = 0
        if len(digits) > 0:
            if number_words.get(digits[0]) != None:
                number_a = number_words.get(digits[0])
            else:
                number_a = digits[0]
            if number_words.get(digits[len(digits) - 1]) != None:
                number_b = number_words.get(digits[len(digits) - 1])
            else:
                number_b = digits[len(digits) - 1]
        if verbose: print("Found: {} - {}".format(number_a, number_b))
        if verbose: print("Old sum: {}".format(summary))
        if verbose: print("Adding: {}".format(int(str(number_a) + str(number_b))))
        summary = summary + (int(str(number_a) + str(number_b)))
        if verbose: print("New sum: {}".format(summary))
        if verbose: print("--------------------------")
    return summary


print("Result of Day {} Part 1: {}".format(current_day, first()))
print("Result of Day {} Part 2: {}".format(current_day, second()))
