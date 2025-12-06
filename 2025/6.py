import os.path
from time import perf_counter
import re

current_day = os.path.basename(__file__.split(".")[0])


def get_mat_from_array(arr):
    mat = []
    dimension = 0
    for el in arr:
        if len(el) > dimension:
            dimension = len(el)
    print(f"Dimension of mat is {dimension}")
    arr.sort(key=lambda el: -len(el))
    for i, el in enumerate(arr):
        for j, c in enumerate(el):
            pass
    return mat


def first(verbose=False):
    file = open("{}.input".format(current_day), "r")
    summary = 0
    coefficients = {}
    operators = {}
    for line in file:
        line = line.strip()
        if not line.startswith("*") and not line.startswith("+"):
            for i, num in enumerate(re.findall(r"\d+", line)):
                if i in coefficients:
                    coefficients[i].append(int(num))
                else:
                    coefficients[i] = [int(num)]
        else:
            for i, op in enumerate(re.findall(r"[*,+]", line)):
                operators[i] = op
    local_summary = 0
    for coeff_group in coefficients:
        if operators[coeff_group] == "*":
            for coeff in enumerate(coefficients[coeff_group]):
                if coeff[0] == 0:
                    local_summary = 1 * coeff[1]
                else:
                    local_summary = local_summary * coeff[1]
        else:
            for coeff in enumerate(coefficients[coeff_group]):
                local_summary = local_summary + coeff[1]
        if verbose: print(f"Column result is {local_summary}")
        summary = summary + local_summary
        local_summary = 0
    return summary


def second(verbose=False):
    file = open("{}.input".format(current_day), "r")
    summary = 0
    spaces = {}
    lines = []
    operators = []
    coefficients = {}
    lines_count = 0
    if verbose: print(f"Getting line_count, operators and delimiting indexes.")
    for i, line in enumerate(file):
        if not line.startswith("*") and not line.startswith("+"):
            for space in re.finditer(r"\s", line):
                if space.start() in spaces:
                    spaces[space.start()] = spaces[space.start()] + 1
                else:
                    spaces[space.start()] = 1
            lines.append(line.replace("\n", ""))
            lines_count = i + 1
        else:
            operators = re.sub("\s", "", line)
    if verbose: print(f"All spaces indexes {spaces}")
    spaces = list(filter(lambda x: spaces[x] == lines_count, spaces))
    if verbose: print(f"Space indexes occuring in all lines {spaces}")
    if verbose: print(f"Replacing delimiters with '|' and padding with 'X'")
    for i, line in enumerate(lines):
        if not line.startswith("*") and not line.startswith("+"):
            for space in spaces:
                line = line[:space] + '|' + line[space + 1:]
            lines[i] = line.replace(" ", "X")
    if verbose: print(f"Adding strings to coefficients.")
    for line in lines:
        for i, number in enumerate(line.split("|")):
            if number != "":
                if i in coefficients:
                    coefficients[i].append(number)
                else:
                    coefficients[i] = [number]
    edited_coefficitens = {}
    if verbose: print(f"Transposing coefficients.")
    for coeff_group in coefficients:
        dimension = len(coefficients[coeff_group][0])
        for i in range(dimension - 1, -1, -1):
            final_string = ""
            for coeff in coefficients[coeff_group]:
                final_string = final_string + coeff[i]
            final_int = int(final_string.replace("X", ""))  # RE
            if coeff_group in edited_coefficitens:
                edited_coefficitens[coeff_group].append(final_int)
            else:
                edited_coefficitens[coeff_group] = [final_int]
    local_summary = 0
    if verbose: print(f"Looping through coefficients and summing them.")
    for coeff_group in edited_coefficitens:
        if operators[coeff_group] == "*":
            for coeff in enumerate(edited_coefficitens[coeff_group]):
                if coeff[0] == 0:
                    local_summary = 1 * coeff[1]
                else:
                    local_summary = local_summary * coeff[1]
        else:
            for coeff in enumerate(edited_coefficitens[coeff_group]):
                local_summary = local_summary + coeff[1]
        if verbose: print(f"Column result is {local_summary}")
        summary = summary + local_summary
        local_summary = 0
    return summary


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first()))
print("Result of Day {} Part 2: {}".format(current_day, second()))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
