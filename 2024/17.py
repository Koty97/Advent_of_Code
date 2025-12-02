import math
import os.path
from itertools import permutations, combinations
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])
def get_operand_value(operand,registry):
    if 0<=operand<=3:
        return operand
    elif operand==4:
        return registry["A"]
    elif operand==5:
        return registry["B"]
    elif operand==6:
        return registry["C"]
def proccess_opcode(opcode,operand,registry):
    if opcode==0:
        registry["A"]=int(registry["A"]/(pow(2,get_operand_value(operand,registry))))
        registry["i"]=int(registry["i"])+2
    elif opcode==1:
        registry["B"]=registry["B"]^operand
        registry["i"] = int(registry["i"]) + 2
    elif opcode==2:
        registry["B"]=get_operand_value(operand,registry)%8
        registry["i"] = int(registry["i"]) + 2
    elif opcode==3:
        if registry["A"]==0:
            registry["i"]=int(registry["i"])+2
        else:
            registry["i"]=int(operand)
    elif opcode==4:
        registry["B"]=registry["B"]^registry["C"]
        registry["i"] = int(registry["i"]) + 2
    elif opcode==5:
        registry["stdout"]=registry["stdout"]+str((get_operand_value(operand,registry)%8))+","
        registry["i"] = int(registry["i"]) + 2
    elif opcode==6:
        registry["B"]=int(registry["A"]/(pow(2,get_operand_value(operand,registry))))
        registry["i"] = int(registry["i"]) + 2
    elif opcode==7:
        registry["C"]=int(registry["A"]/(pow(2,get_operand_value(operand,registry))))
        registry["i"] = int(registry["i"]) + 2
def first(verbose=False):
    file = open("17.input", "r")
    program=[]
    registry={}
    registry["stdout"]=""
    registry["i"]=0
    for line in file:
        if "Register A" in line:
            registry["A"]=int(line.split(":")[1].strip())
            pass
        elif "Register B" in line:
            registry["B"]=int(line.split(":")[1].strip())
        elif "Register C" in line:
            registry["C"]=int(line.split(":")[1].strip())
        elif "Program" in line:
            for opcode in line.split(":")[1].split(","):
                program.append(int(opcode))
    print(registry)
    print(program)
    while registry["i"]<len(program)-1:
        print("Processing opcode {} with operand {}".format(program[int(registry["i"])],program[int(registry["i"])+1]))
        proccess_opcode(program[int(registry["i"])],program[int(registry["i"])+1],registry)
    registry["stdout"] = registry["stdout"][:-1]
    print(registry)
    print(program)
    return None


def second(verbose=False):
    file = open("17.input", "r")

    return None


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first(verbose=False)))
print("Result of Day {} Part 2: {}".format(current_day, second(verbose=True)))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
