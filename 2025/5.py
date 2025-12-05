import os.path
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])


def reduce(intervals_array):
    intervals_array.sort(key=lambda y: y[0])
    new_array = []
    last_joined = False
    for i, el in enumerate(intervals_array):
        if i + 1 < len(intervals_array):
            next_element = intervals_array[i + 1]
            if el == next_element:
                pass
            elif next_element[0] == el[0]:
                if next_element[1] > el[1]:
                    new_array.append((el[0], next_element[1]))
                    last_joined = True
                else:
                    new_array.append((el[0], el[1]))
                    last_joined = True
            elif el[0] < next_element[0] < el[1]:
                if next_element[1] > el[1]:
                    new_array.append((el[0], next_element[1]))
                else:
                    new_array.append((el[0], el[1]))
                last_joined = True
            elif next_element[0] == el[1]:
                if next_element[0] > el[0]:
                    new_array.append((el[0], next_element[1]))
                    last_joined = True
                else:
                    new_array.append((next_element[0], el[1]))
                    last_joined = True
            else:
                if not last_joined:
                    new_array.append((el[0], el[1]))
                last_joined = False
        else:
            if not last_joined:
                new_array.append(el)
    if len(new_array) != len(intervals_array):
        return reduce(new_array)
    else:
        return new_array


def first(verbose=False):
    file = open("{}.input".format(current_day), "r")
    summary = 0
    fresh_id_pairs = []
    for line in file:
        line = line.strip()
        if "-" in line:
            split_line = line.split("-")
            fresh_id_pairs.append((int(split_line[0]), int(split_line[1])))
        elif line != "":
            y = len(list(filter(lambda x: x[0] <= int(line) <= x[1], fresh_id_pairs)))
            if verbose: print(f"For {line} found {y}s")
            if y > 0:
                summary = summary + 1
    if verbose: print(fresh_id_pairs)
    return summary


def second(verbose=False):
    file = open("{}.input".format(current_day), "r")
    summary = 0
    fresh_id_pairs = []
    for line in file:
        line = line.strip()
        if "-" in line:
            split_line = line.split("-")
            fresh_id_pairs.append((int(split_line[0]), int(split_line[1])))
        else:
            break
    new = {}
    for pair in fresh_id_pairs:
        if verbose: print(f"Processing pair {pair}")
        filtered = list(
            filter(lambda x: x != pair and ((x[0] == pair[1] or x[1] == pair[0]) or (x[0] <= pair[1] <= x[1]) or (
                    x[0] <= pair[0] and x[1] >= pair[1])), fresh_id_pairs))
        if filtered:
            if len(filtered) > 1:
                if verbose: print(f"\tReducing {filtered}")
                new[pair] = reduce(filtered)
                if verbose: print(f"\tReduced to {new[pair]}")
            else:
                if verbose: print(f"\tFound one overlapping pair {filtered}")
                new[pair] = filtered
        else:
            if verbose: print(f"\tNo overlapping values found")
            new[pair] = []
    fin = []
    if verbose: print(f"Reducing original pairs with overlapping values")
    for pair in new.items():
        if pair[1]:
            arp = [pair[0], pair[1][0]]
            res = reduce(arp)
            fin.append(res[0])
        else:
            fin.append(pair[0])
    if verbose: print(f"Reducing all values")
    for pair in reduce(fin):
        summary = summary + (pair[1] - pair[0] + 1)
    return summary


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first()))
print("Result of Day {} Part 2: {}".format(current_day, second()))
time_end = perf_counter()
print(f"Took {time_end - time_start} seconds")