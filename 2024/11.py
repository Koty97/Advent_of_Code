import operator
import os.path
import re
from itertools import chain, product, combinations, permutations
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])

def first(verbose=False):
    file = open("11.input", "r")
    summary = 0
    input=file.read()
    stones=input.strip().split(" ")
    for stone in stones:
        stones[stones.index(stone)]=int(stone)
    print(stones)
    blink_count=25
    for x in range(0,blink_count):
        new_stones=[]
        print(x)
        for i,stone in enumerate(stones):
            if stone==0:
                new_stones.append(1)
            elif len(str(stone))%2==0:
                l=int(str(stone)[:int((len(str(stone))/2))])
                r=int(str(stone)[int((len(str(stone))/2)):len(str(stone))])
                new_stones.append(l)
                new_stones.append(r)
            else:
                new_stones.append(stone*2024)
        #print(new_stones)
        stones=new_stones.copy()
    return len(stones)


def second(verbose=False):
    file = open("11.input", "r")
    summary = 0
    input=file.read()
    stones=input.strip().split(" ")
    for stone in stones:
        stones[stones.index(stone)]=int(stone)
    print(stones)
    blink_count=75
    for x in range(0,blink_count):
        new_stones=[]
        print(x)
        for i,stone in enumerate(stones):
            if stone==0:
                new_stones.append(1)
            elif len(str(stone))%2==0:
                l=int(str(stone)[:int((len(str(stone))/2))])
                r=int(str(stone)[int((len(str(stone))/2)):len(str(stone))])
                new_stones.append(l)
                new_stones.append(r)
            else:
                new_stones.append(stone*2024)
        #print(new_stones)
        stones=new_stones.copy()
    return len(stones)


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first()))
print("Result of Day {} Part 2: {}".format(current_day, second()))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
