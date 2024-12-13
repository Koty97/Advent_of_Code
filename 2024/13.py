import os.path
from itertools import permutations, combinations
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])


def first(verbose=False):
    file = open("13.input", "r")
    situations = []
    situation = {}
    for i, line in enumerate(file):
        if "Button A" in line:
            situation["A"] = [line.strip().split(":")[1].split(", ")[0].replace(" X+", ""),
                              line.strip().split(":")[1].split(", ")[1].replace("Y+", "")]
        if "Button B" in line:
            situation["B"] = [line.strip().split(":")[1].split(", ")[0].replace(" X+", ""),
                              line.strip().split(":")[1].split(", ")[1].replace("Y+", "")]
        if "Prize" in line:
            situation["Prize"] = [line.strip().split(":")[1].split(", ")[0].replace(" X=", ""),
                              line.strip().split(":")[1].split(", ")[1].replace("Y=", "")]
            situations.append(situation)
            situation = {}
            pass
    for situation in situations:
        a=0
        b=0
        for a in range(0,1000):
            for b in range(0,1000):
                eqx=a*int(situation["A"][0]) + b*int(situation["B"][0]) == situation["Prize"][0]
                eqy=a*int(situation["A"][1]) + b*int(situation["B"][1]) == situation["Prize"][1]
                if eqy and eqx:
                    print("Winning {} {}".format(a,b))
        print(situation)
    return None


def second(verbose=False):
    file = open("13.input", "r")

    return None


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first(verbose=False)))
print("Result of Day {} Part 2: {}".format(current_day, second(verbose=False)))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
