import math
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
    summary = 0
    for situation in situations:
        if verbose: print("Situation: {}".format(situation))
        for a in range(0, 100):
            for b in range(0, 100):
                eqx = a * int(situation["A"][0]) + b * int(situation["B"][0]) == int(situation["Prize"][0])
                eqy = a * int(situation["A"][1]) + b * int(situation["B"][1]) == int(situation["Prize"][1])
                if eqy and eqx:
                    if verbose: print("Winning {} {}".format(a, b))
                    summary = summary + (a * 3) + (b)
                    break
    return summary

def custom_gcd(a,b,x,y,xprev,yprev):
    q,r=divmod(a,b)
    xnew=xprev - q*x
    ynew=yprev - q*y
    if r==0:
        return b,y,x
    else:
        return custom_gcd(b,r,xnew,ynew,x,y)
def second(verbose=False):
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
    summary = 0
    for situation in situations:
        if verbose: print("Situation: {}".format(situation))
        gcdx=custom_gcd(int(situation["A"][0]), int(situation["B"][0]),1,0,0,1)
        gcdy=custom_gcd(int(situation["A"][1]), int(situation["B"][1]),0,0,0,1)
        solutions=[]
        if int(situation["Prize"][0]) % gcdx[0] == 0 and int(situation["Prize"][1]) % gcdy[0] == 0:
            print("\t{}={}*{}+{}*{}".format(gcdx[0], gcdx[1], int(situation["A"][0]), gcdx[2], int(situation["B"][0])))
            partic=(gcdx[1]*int(situation["Prize"][0]),gcdx[2]*int(situation["Prize"][0]))
            print("\tParticular solution: {}".format(partic))
            at=int(partic[0]/int(situation["B"][0]))#Problém se znaménkem, proč? Jak změnit
            bt=int(partic[1]/int(situation["A"][0]))
            if bt>at:
                temp=bt
                bt=at
                at=temp
            for t in range(bt,at):
                x=partic[0]+(int(situation["B"][0])*t)
                y=partic[1]+(-int(situation["A"][0])*t)
                if x>=0 and y>=0:
                    if (x,y) not in solutions:
                        solutions.append((x,y))
                    print((x,y))
            print("\t----------------")
            print("\t{}={}*{}+{}*{}".format(gcdy[0], gcdy[1], int(situation["A"][1]), gcdy[2], int(situation["B"][1])))
            partic = (gcdy[1] * int(situation["Prize"][1]), gcdy[2] * int(situation["Prize"][1]))
            print("\tParticular solution: {}".format(partic))
            at = int(partic[0] / int(situation["B"][1]))  # Problém se znaménkem, proč? Jak změnit
            bt = int(partic[1] / int(situation["A"][1]))
            if bt > at:
                temp = bt
                bt = at
                at = temp
            for t in range(bt, at):
                x = partic[0] + (int(situation["B"][1]) * t)
                y = partic[1] + (-int(situation["A"][1]) * t)
                if x >= 0 and y >= 0 and (x,y) in solutions:
                    print((x, y))

            print("-----------------")

    return summary


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first(verbose=False)))
print("Result of Day {} Part 2: {}".format(current_day, second(verbose=False)))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
