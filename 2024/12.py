import operator
import os.path
import re
from itertools import chain, product, combinations, permutations
from time import perf_counter
import pprint

current_day = os.path.basename(__file__.split(".")[0])

map={}
def get_adjacent(field,matrix,unvisited_fields,id):
    directions = [
        [1, 1], [-1, -1], [1, -1], [-1, 1],
        [1, 0], [0, 1], [-1, 0], [0, -1]
    ]
    code = matrix[field[0]][field[1]]
    if map.get(id) is not None:
        map[id].append([field[0]],[field[1]])
    else:
        map[id]=[[field[0]],[field[1]]]
    for direction in directions:
        try:
            if matrix[field[0]+direction[0]][field[1]+direction[1]]==code:
                unvisited_fields.remove([field[0]+direction[0],field[1]+direction[1]])
                get_adjacent([field[0] + direction[0],field[1] + direction[1]], matrix, unvisited_fields)
        except:
            pass
def first(verbose=False):
    file = open("12.input", "r")
    summary = 0
    matrix = []
    unvisited_fields = []
    for i, line in enumerate(file):
        line_matrix = []
        for j, char in enumerate(line.strip()):
            line_matrix.append(char)
            unvisited_fields.append([i, j])
        matrix.append(line_matrix)
    print(matrix)
#    for i,line in enumerate(matrix):
#        for j,field in enumerate(line):
    for i in range(0,8):
        for field in unvisited_fields:
            unvisited_fields.remove(field)
            print("Traversing letter {}".format(matrix[field[0]][field[1]]))
            get_adjacent(field,matrix,unvisited_fields,"{} [{},{}]".format(matrix[field[0]][field[1]],field[0],field[1]))
            print("-------------------")
    pprint.pprint(map)
    print(unvisited_fields)
    return summary


def second(verbose=False):
    file = open("12.input", "r")
    summary = 0
    matrix=[]
    unvisited_fields=[]
    for i,line in enumerate(file):
        line_matrix=[]
        for j,char in enumerate(line.strip()):
            line_matrix.append(char)
            unvisited_fields.append([i,j])
        matrix.append(line_matrix)
    print(matrix)
    print(unvisited_fields)
    return summary


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first()))
#print("Result of Day {} Part 2: {}".format(current_day, second()))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
