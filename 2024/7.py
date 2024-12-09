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
        print("Processing {}".format(y))
        y=y+1
        result = int(line.strip().split(":")[0])
        numbers = line.strip().split(":")[1].strip().split(" ")
        if verbose: print("Number array:".format(numbers))
        comb = combinations([operator.add, operator.mul] * (len(numbers) - 1), len(numbers) - 1)
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
    for line in file:
        print("Processing {}".format(y))
        y = y + 1
        result = int(line.strip().split(":")[0])
        numbers = line.strip().split(":")[1].strip().split(" ")
        if verbose: print("Number array:".format(numbers))
        comb = combinations([operator.mul,operator.add,concatenation] * (len(numbers) - 1), len(numbers) - 1)
        comb_list = []
        for i in list(comb):
            if i not in comb_list: comb_list.append(i)
        for var in comb_list:
            equation=numbers.copy()
            index=1
            for operation in var:
                equation.insert(index,operation)
                index=index+2
            if verbose: print("\teq={}".format(equation))
            if concatenation in var:
                for i,element in enumerate(equation):
                    if element == operator.mul or element == operator.add or element==concatenation:
                        equation.insert(i+1,element(int(equation[i-1]),int(equation[i+1])))
                        try:
                            equation.pop(i + 2)
                        except:
                            pass
                if verbose: print("\tResult is {}".format(equation[len(equation)-1]))
                is_ok = result == equation[len(equation)-1]
                if is_ok:
                    summary=summary+result
                    if verbose: print("\tAdding summ")
                    break
            else:
                index = 0
                summ = int(numbers[index])
                for operation in var:
                    summ = operation(summ, int(numbers[index + 1]))
                    index = index + 1
                if verbose: print("\tFor var {} result is {}".format(var, summ))
                is_ok = result == summ
                if is_ok:
                    summary = summary + result
                    if verbose: print("\tAdding summ")
                    break
            pass
    file.close()
    return summary


time_start = perf_counter()
#print("Result of Day {} Part 1: {}".format(current_day, first()))
print("Result of Day {} Part 2: {}".format(current_day, second()))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
