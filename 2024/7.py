import operator
import os.path
import re
from itertools import chain, product, combinations, permutations
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])

def concatenation(a,b):
    return int(str(a)+str(b))
def first(verbose=False):
    file = open("7.input", "r")
    summary = 0
    y=0
    for line in file:
        if verbose: print("Processing {}".format(y))
        y=y+1
        result = int(line.strip().split(":")[0])
        numbers = line.strip().split(":")[1].strip().split(" ")
        if verbose: print("Number array:".format(numbers))
        comb = list(product([operator.mul, operator.add], repeat=len(numbers) - 1))
        comb_list = []
        for i in list(comb):
            if i not in comb_list: comb_list.append(i)
        for var in comb_list:
            is_ok = True
            index = 0
            summ = int(numbers[index])
            for operation in var:
                summ = operation(summ, int(numbers[index + 1]))
                index = index + 1
            if verbose: print("\tFor var {} result is {}".format(var, summ))
            is_ok = result == summ
            if is_ok:
                summary=summary+result
                break
    file.close()
    return summary


def second(verbose=False):
    file = open("7.input", "r")
    summary = 0
    y = 0
    lines=[]
    for line in file:
        lines.append(line.strip())
    file.close()
    lines=sorted(lines,key=len)
    for y,line in enumerate(lines):
        if verbose: print("Processing {}".format(y))
        result = int(line.strip().split(":")[0])
        numbers = line.strip().split(":")[1].strip().split(" ")
        if verbose: print("Number array: {} with result {}".format(numbers, result))
        comb_list = list(product([operator.mul, operator.add, concatenation], repeat=len(numbers) - 1))
        for i, combination in enumerate(comb_list):
            equation = list(chain.from_iterable(zip(numbers, list(combination))))
            equation.append(numbers[-1])
            index = 0
            for j, element in enumerate(equation):
                if not str(element).isnumeric():
                    if verbose: print(
                        "\tOperation {} between {} and {} results {}".format(element, index, equation[j + 1],
                                                                             element(int(index), int(equation[j + 1]))))
                    index = element(int(index), int(equation[j + 1]))
                    if index > result:
                        break
                if j == 0:
                    index = element
            if index == result:
                if verbose: print("\tResult found, breaking")
                summary = summary + result
                break
            if verbose: print("\t---------------")
    return summary


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first(verbose=False)))
print("Result of Day {} Part 2: {}".format(current_day, second(verbose=False)))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
