import os.path
import re
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])


def first(verbose=False):
    file = open("3.input", "r")
    summary = 0
    file_content = file.read()
    regex_result = re.findall("mul\\(\\d+,\\d+\\)", file_content)
    for mul in regex_result:
        mul_stripped = mul.replace("mul(", "").replace(")", "").split(",")
        summary = summary + (int(mul_stripped[0]) * int(mul_stripped[1]))
    file.close()
    return summary


def second(verbose=False):
    file = open("3.input", "r")
    summary = 0
    file_content = file.read()
    regex_result = re.finditer("(mul\(\d+,\d+\))|(do\(\))|(don't\(\))", file_content)
    list = []
    for instruction in regex_result:
        list.append(instruction.group())
    apply = True
    for instruction in list:
        if instruction == "don't()":
            apply = False
        elif instruction == "do()":
            apply = True
        else:
            if apply:
                mul_stripped = instruction.replace("mul(", "").replace(")", "").split(",")
                summary = summary + (int(mul_stripped[0]) * int(mul_stripped[1]))
    file.close()
    return summary

time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first()))
print("Result of Day {} Part 2: {}".format(current_day, second()))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')