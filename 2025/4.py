import os.path
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])


def get_adjacent_pos(i, j, max_i, max_j, adjacent_tiles=1):
    result = []
    for i_n in range(i - adjacent_tiles, i + adjacent_tiles + 1):
        if i_n >= 0 and i_n <= max_i:
            for j_n in range(j - adjacent_tiles, j + adjacent_tiles + 1):
                if j_n >= 0 and j_n <= max_j:
                    result.append((i_n, j_n))
    result.remove((i, j))
    return result


def print_arr(arr):
    for line in arr:
        s = ""
        for char in line:
            s = s + char
        print(s)


def first(verbose=False):
    file = open("{}.input".format(current_day), "r")
    summary = 0
    arr = []
    for line in file:
        line = line.strip()
        a = []
        for char in line:
            a.append(char)
        arr.append(a)
    for i, line in enumerate(arr):
        for j, char in enumerate(line):
            if char == "@":
                adj_count = 0
                adj = get_adjacent_pos(i, j, len(arr) - 1, len(line) - 1)
                if verbose:
                    print(f"Char at {i},{j} - adjacent {adj}")
                for coords in adj:
                    if verbose:
                        print(f"\t{coords}={arr[coords[0]][coords[1]]}")
                    if arr[coords[0]][coords[1]] == "@":
                        adj_count = adj_count + 1
                if verbose:
                    print(f"\t\tFound {adj_count} adjacent '@'")
                if adj_count < 4:
                    summary = summary + 1
    return summary


def second(verbose=False):
    file = open("{}.input".format(current_day), "r")
    summary = 0

    arr = []
    for line in file:
        line = line.strip()
        a = []
        for char in line:
            a.append(char)
        arr.append(a)
    removed = 1
    while removed != 0:
        removed = 0
        if verbose:
            print_arr(arr)
        for i, line in enumerate(arr):
            for j, char in enumerate(line):
                if char == "@":
                    adj_count = 0
                    adj = get_adjacent_pos(i, j, len(arr) - 1, len(line) - 1)
                    if verbose:
                        print(f"Char at {i},{j} - adjacent {adj}")
                    for coords in adj:
                        if verbose:
                            print(f"\t{coords}={arr[coords[0]][coords[1]]}")
                        if arr[coords[0]][coords[1]] == "@":
                            adj_count = adj_count + 1
                    if verbose:
                        print(f"\t\tFound {adj_count} adjacent '@'")
                    if adj_count < 4:
                        summary = summary + 1
                        if verbose:
                            print("\tRemoved object")
                        arr[i][j] = "."
                        removed = removed + 1
        if verbose:
            print("----------------------")
    return summary


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first()))
print("Result of Day {} Part 2: {}".format(current_day, second()))
time_end = perf_counter()
print(f"Took {time_end - time_start} seconds")