import os.path
from itertools import permutations, combinations
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])


def get_nodes_distance(loc_a, loc_b):
    return [loc_b[0] - loc_a[0], loc_b[1] - loc_a[1]]


def first(verbose=False):
    file = open("8.input", "r")
    matrix = []
    antennas = {}
    antinodes=[]
    i = 0
    for line in file:
        line_matrix = []
        j = 0
        for char in line.strip():
            if char != ".":
                if antennas.get(char) is not None:
                    antennas.get(char).append([i, j])
                else:
                    antennas[char] = [[i, j]]
            line_matrix.append(char)
            j = j + 1
        matrix.append(line_matrix)
        i = i + 1
    if verbose: print(antennas)
    max_size=49
    for key,value in antennas.items():
        perm = combinations(value,2)
        for i in perm:
            distance=get_nodes_distance(i[0],i[1])
            if 0<=i[0][0]-distance[0]<=max_size and 0<=i[0][1]-distance[1]<=max_size and antinodes.count([i[0][0]-distance[0],i[0][1]-distance[1]])==0:
                antinodes.append([i[0][0]-distance[0],i[0][1]-distance[1]])
                if verbose: print("Apeending antinode {} for {}".format([i[0][0]-distance[0],i[0][1]-distance[1]], key))
            if 0<=i[1][0]+distance[0] <= max_size and 0<=i[1][1]+distance[1] <= max_size and antinodes.count([i[1][0]+distance[0],i[1][1]+distance[1]])==0:
                antinodes.append([i[1][0]+distance[0],i[1][1]+distance[1]])
                if verbose: print("Apeending antinode {} for {}".format([i[1][0]+distance[0],i[1][1]+distance[1]],key))
    if verbose: print(antinodes)
    return len(antinodes)


def second(verbose=False):
    file = open("8.input", "r")
    matrix = []
    antennas = {}
    antinodes=[]
    i = 0
    for line in file:
        line_matrix = []
        j = 0
        for char in line.strip():
            if char != ".":
                if antennas.get(char) is not None:
                    antennas.get(char).append([i, j])
                else:
                    antennas[char] = [[i, j]]
            line_matrix.append(char)
            j = j + 1
        matrix.append(line_matrix)
        i = i + 1
    print(antennas)
    max_size=49
    for key,value in antennas.items():
        perm = combinations(value,2)
        for i in perm:
            distance=get_nodes_distance(i[0],i[1])
            print("Distance between {} and {} is {}".format(i[0],i[1],distance))
            if 0<=i[0][0]+distance[0]<max_size and 0<=i[0][1]+distance[1]<max_size and antinodes.count([i[0][0]+distance[0],i[0][1]+distance[1]])==0:
                antinodes.append([i[0][0]+distance[0],i[0][1]+distance[1]])
            if 0<=i[0][0]-distance[0]<=max_size and 0<=i[0][1]-distance[1]<=max_size and antinodes.count([i[0][0]-distance[0],i[0][1]-distance[1]])==0:
                antinodes.append([i[0][0]-distance[0],i[0][1]-distance[1]])
                new_node=[i[0][0]-distance[0],i[0][1]-distance[1]]
                while 0<=new_node[0]<max_size and 0<=new_node[1]<max_size:
                    if antinodes.count(new_node)==0:
                        print("Apending antinode {} for {}".format(new_node, key))
                        antinodes.append(new_node)
                    new_node=[new_node[0]-distance[0],new_node[1]-distance[1]]
                new_node=[i[0][0]+distance[0],i[0][1]+distance[1]]
                while 0<=new_node[0]<max_size and 0<=new_node[1]<max_size:
                    if antinodes.count(new_node)==0:
                        print("Apending antinode {} for {}".format(new_node, key))
                        antinodes.append(new_node)
                    new_node=[new_node[0]+distance[0],new_node[1]+distance[1]]
                print("Apeending antinode {} for {}".format([i[0][0]-distance[0],i[0][1]-distance[1]], key))
            if 0<=i[1][0]+distance[0] < max_size and 0<=i[1][1]+distance[1] <= max_size and antinodes.count([i[1][0]+distance[0],i[1][1]+distance[1]])==0:
                antinodes.append([i[1][0]+distance[0],i[1][1]+distance[1]])
                new_node=[i[1][0]+distance[0],i[1][1]+distance[1]]
                while 0<=new_node[0]<max_size and 0<=new_node[1]<max_size:
                    if antinodes.count(new_node)==0:
                        print("Apending antinode {} for {}".format(new_node, key))
                        antinodes.append(new_node)
                    new_node=[new_node[0]+distance[0],new_node[1]+distance[1]]
                new_node = [i[1][0] - distance[0], i[1][1] - distance[1]]
                while 0<=new_node[0]<max_size and 0<=new_node[1]<max_size:
                    if antinodes.count(new_node)==0:
                        print("Apending antinode {} for {}".format(new_node, key))
                        antinodes.append(new_node)
                    new_node=[new_node[0]-distance[0],new_node[1]-distance[1]]
                print("Apeending antinode {} for {}".format([i[1][0]+distance[0],i[1][1]+distance[1]],key))
    for antenna in antennas.values():
        for coord in antenna:
            if antinodes.count(coord)==0:
                antinodes.append(coord)
    antinodes.sort()
    print(antinodes)
    return len(antinodes)


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first(verbose=False)))
print("Result of Day {} Part 2: {}".format(current_day, second()))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
