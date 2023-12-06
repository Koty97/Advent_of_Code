import os.path
import re

current_day = os.path.basename(__file__.split(".")[0])


def first(verbose=False):
    file = open("5.input", "r")
    summary = 0
    dictionary = {}
    dictionary["seeds"] = file.readline().split(": ")[1].strip().split(" ")
    current_index = ""
    for line in file:
        name_pattern = r"([.\S]*)\s*\w*:"
        match = re.search(name_pattern, line)
        if match is None and line != "\n":
            if verbose: print("\tAdding {} to {}".format(line.strip(), current_index))
            dictionary[current_index].append(line.strip())
        elif match is not None:
            current_index = match.group(0).split(" ")[0]
            dictionary[current_index] = []
            if verbose: print("Found {}".format(current_index))
    if verbose: print(dictionary)
    where_to_map = {}
    if verbose: print("Seeds: {}".format(dictionary["seeds"]))
    current_list = dictionary["seeds"]
    for seed in current_list:
        where_to_map[seed] = int(seed)
    new_map = {}
    for iterator in range(len(dictionary) - 1):
        if verbose: print(
            "With iterator {} name is {} and value {}".format(iterator, list(dictionary.keys())[iterator + 1],
                                                              dictionary[list(dictionary.keys())[iterator + 1]]))
        for seed in current_list:
            for my_map in dictionary[list(dictionary.keys())[iterator + 1]]:
                my_map = my_map.split(" ")
                if verbose: print(
                    "Checking if {} is in range {}-{}".format(seed, int(my_map[1]),
                                                              int(my_map[1]) + int(my_map[2]) - 1))
                if int(seed) in range(int(my_map[1]), int(my_map[1]) + int(my_map[2])):
                    new_map[seed] = int(my_map[0]) + (int(seed) - int(my_map[1]))
                    break
                else:
                    try:
                        new_map[seed] = int(seed)
                    except:
                        break
                if verbose: print("By map:{}, seed {} should be mapped to {}".format(my_map, seed, new_map))
        if verbose: print("Resulting map: {}".format(new_map))
        current_list = list(new_map.values())
        if verbose: print("Mapping {} to {}".format(new_map, where_to_map))
        for x in new_map.items():
            where_to_map[list(where_to_map.keys())[list(where_to_map.values()).index(int(x[0]))]] = int(x[1])
        new_map = {}
        if verbose: print("New base list: {}".format(current_list))
    return sorted(where_to_map.values())[0]


def second(verbose=False):
    file = open("5.input", "r")
    summary = 0
    dictionary = {}
    base={}
    base["seeds"]=file.readline().split(": ")[1].strip().split(" ")
    dictionary["seeds"] = []
    val=0
    for i,x in enumerate(base["seeds"]):
        if not i%2:
            val=int(x)
        else:
            for y in range(val,val+int(x)):
                dictionary["seeds"].append(y)
    if verbose: print(dictionary["seeds"])
    current_index = ""
    for line in file:
        name_pattern = r"([.\S]*)\s*\w*:"
        match = re.search(name_pattern, line)
        if match is None and line != "\n":
            if verbose: print("\tAdding {} to {}".format(line.strip(), current_index))
            dictionary[current_index].append(line.strip())
        elif match is not None:
            current_index = match.group(0).split(" ")[0]
            dictionary[current_index] = []
            if verbose: print("Found {}".format(current_index))
    if verbose: print(dictionary)
    where_to_map = {}
    if verbose: print("Seeds: {}".format(dictionary["seeds"]))
    current_list = dictionary["seeds"]
    for seed in current_list:
        where_to_map[seed] = int(seed)
    new_map = {}
    for iterator in range(len(dictionary) - 1):
        if verbose: print(
            "With iterator {} name is {} and value {}".format(iterator, list(dictionary.keys())[iterator + 1],
                                                              dictionary[list(dictionary.keys())[iterator + 1]]))
        for seed in current_list:
            for my_map in dictionary[list(dictionary.keys())[iterator + 1]]:
                my_map = my_map.split(" ")
                if verbose: print(
                    "Checking if {} is in range {}-{}".format(seed, int(my_map[1]),
                                                              int(my_map[1]) + int(my_map[2]) - 1))
                if int(seed) in range(int(my_map[1]), int(my_map[1]) + int(my_map[2])):
                    new_map[seed] = int(my_map[0]) + (int(seed) - int(my_map[1]))
                    break
                else:
                    try:
                        new_map[seed] = int(seed)
                    except:
                        break
                if verbose: print("By map:{}, seed {} should be mapped to {}".format(my_map, seed, new_map))
        if verbose: print("Resulting map: {}".format(new_map))
        current_list = list(new_map.values())
        if verbose: print("Mapping {} to {}".format(new_map, where_to_map))
        for x in new_map.items():
            where_to_map[list(where_to_map.keys())[list(where_to_map.values()).index(int(x[0]))]] = int(x[1])
        new_map = {}
        if verbose: print("New base list: {}".format(current_list))
    return sorted(where_to_map.values())[0]


print("Result of Day {} Part 1: {}".format(current_day, first()))
print("Result of Day {} Part 2: {}".format(current_day, second()))
