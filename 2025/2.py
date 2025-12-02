import os.path
from time import perf_counter
import re

current_day = os.path.basename(__file__.split(".")[0])


def first(verbose=False):
    file = open("{}.input".format(current_day), "r")

    summary = 0
    for line in file:
        for pair in line.split(","):
            start = pair.split("-")[0]
            end = pair.split("-")[1]
            if verbose: print("Processing range {}-{} ({} numbers)".format(start, end, int(end) - int(start)))
            for i in range(int(start), int(end) + 1):
                number_string = str(i)
                number_string_length = len(number_string)
                if number_string_length % 2 == 0:
                    if verbose: print("ID {} is divisible by 2".format(i))
                    left_half = number_string[0:int(number_string_length / 2)]
                    right_half = number_string[int(number_string_length / 2):int(number_string_length)]
                    is_id_invalid = left_half == right_half
                    if is_id_invalid:
                        if verbose: print("ID {} invalid, as {} repeats 2 times".format(i, left_half))
                        summary = summary + i
    return summary


def second(verbose=False):
    file = open("{}.input".format(current_day), "r")
    summary = 0
    for line in file:
        for pair in line.split(","):
            start = pair.split("-")[0]
            end = pair.split("-")[1]
            if verbose: print("Processing range {}-{} ({} numbers)".format(start, end, int(end) - int(start)))
            for t in range(int(start), int(end) + 1):
                test = str(t)
                if len(test) == 1:
                    continue
                is_one_repetition = (test == test[0] * len(test))
                if not is_one_repetition:
                    for i in range(2, len(test)):
                        if len(test) % i == 0:
                            part = test[0:int(len(test) / i)]
                            r = re.findall(part, test)
                            if len(r) == i:
                                summary = summary + t
                                if verbose: print("Marking {} invalid, as {} repeats {} times".format(t, r[0], i))
                                break
                else:
                    summary = summary + t
                    if verbose: print("Marking {} invalid, as {} repeats {} times".format(t, test[0], len(test)))
    return summary


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first()))
print("Result of Day {} Part 2: {}".format(current_day, second()))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
