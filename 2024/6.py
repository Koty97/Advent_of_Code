import os.path
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])
def add_direction(direction):
    if direction+90<=270:
        return direction+90
    else:
        return 0

def simulate_movement(matrix,pos,direction):
    visited_fields = []
    player_pos=pos.copy()
    while (direction == 0 and player_pos[0] != 0) or (direction == 90 and player_pos[1] != len(matrix[0])-1) or (direction == 180 and player_pos[0] != len(matrix)-1) or (direction == 270 and player_pos[1] != 0):
        if direction == 0 and matrix[player_pos[0] - 1][player_pos[1]]!="#":
            #print("\tMoving player from [{},{}] to [{},{}]".format(player_pos[0],player_pos[1],player_pos[0]-1,player_pos[1]))
            player_pos[0] = player_pos[0] - 1
        elif direction == 90 and matrix[player_pos[0]][player_pos[1]+1]!="#":
            #print("\tMoving player from [{},{}] to [{},{}]".format(player_pos[0], player_pos[1], player_pos[0],
            #                                                       player_pos[1]+1))
            player_pos[1] = player_pos[1] + 1
        elif direction == 180 and matrix[player_pos[0] + 1][player_pos[1]]!="#":
            #print("\tMoving player from [{},{}] to [{},{}]".format(player_pos[0], player_pos[1], player_pos[0] + 1,
            #                                                       player_pos[1]))
            player_pos[0] = player_pos[0] + 1
        elif direction == 270 and matrix[player_pos[0]][player_pos[1]-1]!="#":
            #print("\tMoving player from [{},{}] to [{},{}]".format(player_pos[0], player_pos[1], player_pos[0],
            #                                                       player_pos[1]-1))
            player_pos[1] = player_pos[1] - 1
        else:
            direction=add_direction(direction)
        visited_fields.append((player_pos[0], player_pos[1]))
        if visited_fields.count((player_pos[0], player_pos[1]))==7:
            return True
            break
def first(verbose=False):
    file = open("6.input", "r")
    matrix = []
    visited_fields = []
    direction = 0
    player_pos = []
    for line in file:
        matrix.append(list(line.strip()))
        if "^" in line:
            player_pos = [len(matrix) - 1, line.index("^")]
    visited_fields.append((player_pos[0], player_pos[1]))
    while (direction == 0 and player_pos[0] != 0) or (direction == 90 and player_pos[1] != len(matrix[0])-1) or (direction == 180 and player_pos[0] != len(matrix)-1) or (direction == 270 and player_pos[1] != 0):
        if direction == 0 and matrix[player_pos[0] - 1][player_pos[1]]!="#":
            player_pos[0] = player_pos[0] - 1
        elif direction == 90 and matrix[player_pos[0]][player_pos[1]+1]!="#":
            player_pos[1] = player_pos[1] + 1
        elif direction == 180 and matrix[player_pos[0] + 1][player_pos[1]]!="#":
            player_pos[0] = player_pos[0] + 1
        elif direction == 270 and matrix[player_pos[0]][player_pos[1]-1]!="#":
            player_pos[1] = player_pos[1] - 1
        else:
            if verbose: print("Player would encounter obstacle at [{},{}], changing direction from {} to {}".format(player_pos[0]-1,player_pos[1],direction,add_direction(direction)))
            direction=add_direction(direction)
        if (player_pos[0], player_pos[1]) not in visited_fields:
            visited_fields.append((player_pos[0], player_pos[1]))
    return len(visited_fields)


def second(verbose=False):
    file = open("6.input", "r")
    matrix = []
    summary=0
    direction = 0
    player_pos = []
    for line in file:
        matrix.append(list(line.strip()))
        if "^" in line:
            player_pos = [len(matrix) - 1, line.index("^")]
    for i,row in enumerate(matrix):
        for j,field in enumerate(row):
            if field == ".":
                print("Changing [{},{}] from {} to {}".format(i,j,"#","."))
                row[j]="#"
                if simulate_movement(matrix,player_pos,direction):summary=summary+1
                row[j] = "."
    return summary


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first(verbose=False)))
print("Result of Day {} Part 2: {}".format(current_day, second()))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
