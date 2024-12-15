import math
import os.path
from time import perf_counter

from PIL import Image
import numpy as np
from scipy import ndimage
from scipy.ndimage import *
current_day = os.path.basename(__file__.split(".")[0])


def simulate_movement(robot, boundaries,verbose):
    if robot["pos"]["x"] + robot["velocity"]["x"] < 0:
        robot["pos"]["x"] = robot["pos"]["x"] + robot["velocity"]["x"] + boundaries[0]
    elif robot["pos"]["x"] + robot["velocity"]["x"] >= boundaries[0]:
        robot["pos"]["x"] = robot["pos"]["x"] + robot["velocity"]["x"] - boundaries[0]
    else:
        robot["pos"]["x"] = robot["pos"]["x"] + robot["velocity"]["x"]

    if robot["pos"]["y"] + robot["velocity"]["y"] < 0:
        robot["pos"]["y"] = robot["pos"]["y"] + robot["velocity"]["y"] + boundaries[1]
    elif robot["pos"]["y"] + robot["velocity"]["y"] >= boundaries[1]:
        robot["pos"]["y"] = robot["pos"]["y"] + robot["velocity"]["y"] - boundaries[1]
    else:
        robot["pos"]["y"] = robot["pos"]["y"] + robot["velocity"]["y"]
    if verbose: print("New robot attributes: {}".format(robot))
    return None


def first(verbose=False):
    file = open("14.input", "r")
    robots = []
    for line in file:
        robot = {}
        robot["pos"] = {}
        robot["velocity"] = {}
        robot["pos"]["x"] = int(line.strip().split(" ")[0].split("=")[1].split(",")[0])
        robot["pos"]["y"] = int(line.strip().split(" ")[0].split("=")[1].split(",")[1])
        robot["velocity"]["x"] = int(line.strip().split(" ")[1].split("=")[1].split(",")[0])
        robot["velocity"]["y"] = int(line.strip().split(" ")[1].split("=")[1].split(",")[1])
        robots.append(robot)
    steps = 100
    sizex, sizey = 101, 103
    for step in range(0, steps):
        for robot in robots:
            simulate_movement(robot, (sizex, sizey),verbose)
    q1,q2,q3,q4=0,0,0,0
    for robot in robots:
        if robot["pos"]["x"] <math.floor(sizex/2) and robot["pos"]["y"] <math.floor(sizey/2):
            if verbose: print("{} is in Q1".format(robot["pos"]))
            q1=q1+1
        elif robot["pos"]["x"]>math.floor(sizex/2) and robot["pos"]["y"] <math.floor(sizey/2):
            if verbose: print("{} is in Q2".format(robot["pos"]))
            q2= q2 + 1
        elif robot["pos"]["x"] <math.floor(sizex/2) and robot["pos"]["y"] >math.floor(sizey/2):
            if verbose: print("{} is in Q3".format(robot["pos"]))
            q3 = q3 + 1
        elif robot["pos"]["x"] >math.floor(sizex/2) and robot["pos"]["y"] >math.floor(sizey/2):
            if verbose: print("{} is in Q4".format(robot["pos"]))
            q4 = q4 + 1
    if verbose: print("Q1: {}, Q2: {}, Q3: {}, Q4: {}".format(q1,q2,q3,q4))
    return q1*q2*q3*q4

def get_clusters(robots,sizex,sizey):
    board=[[(0,0,0) for i in range(sizey)] for j in range(sizex)]
    for robot in robots:
        board[robot["pos"]["x"]][robot["pos"]["y"]]=(255,255,255)
    board= np.array(board)
    lw, num = ndimage.label(board)
    area = ndimage.sum(board, lw, index=np.arange(lw.max() + 1))
    return (board,max(area))
def second(verbose=False):
    file = open("14.input", "r")
    robots = []
    for line in file:
        robot = {}
        robot["pos"] = {}
        robot["velocity"] = {}
        robot["pos"]["x"] = int(line.strip().split(" ")[0].split("=")[1].split(",")[0])
        robot["pos"]["y"] = int(line.strip().split(" ")[0].split("=")[1].split(",")[1])
        robot["velocity"]["x"] = int(line.strip().split(" ")[1].split("=")[1].split(",")[0])
        robot["velocity"]["y"] = int(line.strip().split(" ")[1].split("=")[1].split(",")[1])
        robots.append(robot)
    steps = 10000
    sizex, sizey = 101, 103
    m=0
    maxboard=""
    for step in range(0, steps):
        for robot in robots:
            simulate_movement(robot, (sizex, sizey),verbose)
        n=get_clusters(robots,sizex,sizey)
        maxboard=n[0]
        if int(n[1])==175185:
            m=step+1
            break
    Image.fromarray(np.asarray(maxboard,dtype=np.uint8)).show()
    return m


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first(verbose=False)))
print("Result of Day {} Part 2: {}".format(current_day, second(verbose=False)))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
