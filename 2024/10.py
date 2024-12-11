import os.path
from itertools import permutations, combinations
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])


def is_adjacent(a, b):
    return ((a[0] + 1 == b[0] or a[0] - 1 == b[0]) and a[1] == b[1]) or (
                (a[1] + 1 == b[1] or a[1] - 1 == b[1]) and a[0] == b[0])

def get_adjacents_first(pos,value,dic,verbose):
    #while value<9:
    adjacents = []
    #for step in dic[value + 1]:
    for step in dic[str(value + 1)]:
        if is_adjacent(pos, step):
            adjacents.append(step)
    if verbose: print("\t{} has {} adjacents of value {}: {}".format(pos,len(adjacents), value + 1, adjacents))
    for adjacent in adjacents:
        if value+1!=9:
            get_adjacents_first(adjacent,value+1,dic,verbose)
        else:
            if dic.get("end") is not None:
                if dic.get("end").count(adjacent)==0:
                    dic["end"].append(adjacent)
            else:
                dic["end"]=[adjacent]
    return adjacents

def get_adjacents_second(pos,value,dic,verbose):
    #while value<9:
    adjacents = []
    #for step in dic[value + 1]:
    for step in dic[str(value + 1)]:
        if is_adjacent(pos, step):
            adjacents.append(step)
    if verbose: print("\t{} has {} adjacents of value {}: {}".format(pos,len(adjacents), value + 1, adjacents))
    for adjacent in adjacents:
        if value+1!=9:
            get_adjacents_second(adjacent,value+1,dic,verbose)
        else:
            if dic.get("end") is not None:
                if dic.get("end").count(adjacent)==0:
                    dic["end"].append(adjacent)
            else:
                dic["end"]=[adjacent]
    return adjacents
def first(verbose=False):
    file = open("10.input", "r")
    matrix = []
    dic = {}
    for i, line in enumerate(file):
        line_matrix = []
        for j, char in enumerate(line.strip()):
            if dic.get(char) is None:
                dic[char] = [[i, j]]
            else:
                dic[char].append([i, j])
        matrix.append(line_matrix)

    summary=0
    for start in dic["0"]:
        if verbose: print("Starting from {}".format(start))
        value = 0
        get_adjacents_first(start, value, dic,verbose)
        if verbose: print("Ends: {}\n".format(dic["end"]))
        summary=summary+len(dic["end"])
        dic["end"]=[]
    return summary


def second(verbose=False):
    file = open("10.input", "r")
    matrix = []
    dic = {}
    for i, line in enumerate(file):
        line_matrix = []
        for j, char in enumerate(line.strip()):
            if dic.get(char) is None:
                dic[char] = [[i, j]]
            else:
                dic[char].append([i, j])
        matrix.append(line_matrix)

    summary=0
    for start in dic["0"]:
        if verbose: print("Starting from {}".format(start))
        value = 0
        get_adjacents(start, value, dic,verbose)
        if verbose: print("Ends: {}\n".format(dic["end"]))
        summary=summary+len(dic["end"])
        dic["end"]=[]
    return summary


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first(verbose=False)))
print("Result of Day {} Part 2: {}".format(current_day, second()))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
