import math
import os.path
from itertools import permutations, combinations
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])


def print_board(board):
    for line in board:
        for char in line:
            print(char, end="")
        print("")
    print("")

def get_rating(board):
    summary=0
    for i,line in enumerate(board):
        for j,char in enumerate(line):
            if char=="O":
                summary=summary+(100*i)+j
    return summary
def first(verbose=False):
    file = open("15.input", "r")
    board = []
    moves = []
    player_pos = ()
    for i, line in enumerate(file):
        if line.startswith("#"):
            board_line = []
            for j, char in enumerate(line.strip()):
                board_line.append(char)
                if char == "@":
                    player_pos = (i, j)
            board.append(board_line)
        else:
            for char in line.strip():
                moves.append(char)
        pass
    if verbose: print(moves)
    if verbose: print(player_pos)
    if verbose: print(board[player_pos[0]][player_pos[1]])
    for move in moves:
        new_player_pos = ()
        if move == "<":
            if verbose: print("Moving <")
            new_player_pos = (player_pos[0], player_pos[1] - 1)
        elif move == ">":
            if verbose: print("Moving >")
            new_player_pos = (player_pos[0], player_pos[1] + 1)
        elif move == "v":
            if verbose: print("Moving v")
            new_player_pos = (player_pos[0] + 1, player_pos[1])
        elif move == "^":
            if verbose: print("Moving ^")
            new_player_pos = (player_pos[0] - 1, player_pos[1])
        board_element = board[new_player_pos[0]][new_player_pos[1]]
        if verbose: print("\tPlayer should move from {} to {}".format(player_pos, new_player_pos))
        if verbose: print("\tElement at {} is {}".format(new_player_pos, board_element))
        if board_element == "#":
            if verbose: print("\tCannot move, due to obstacle")
        elif board_element == ".":
            if verbose: print("\tFree space, moving")
            board[player_pos[0]][player_pos[1]] = board_element
            board[new_player_pos[0]][new_player_pos[1]] = "@"
            player_pos = new_player_pos
        elif board_element == "O":
            if verbose: print("\tBox ahead!")
            box_position = new_player_pos
            box_count = 0
            free_space=0
            while board[box_position[0]][box_position[1]] == "O":
                box_count = box_count + 1
                box_position=(box_position[0] + (new_player_pos[0] - player_pos[0]),box_position[1] + (new_player_pos[1] - player_pos[1]))
            box_position = new_player_pos
            while board[box_position[0]][box_position[1]] != "#":
                if board[box_position[0]][box_position[1]]==".":
                    free_space=free_space+1
                box_position = (box_position[0] + (new_player_pos[0] - player_pos[0]),
                                box_position[1] + (new_player_pos[1] - player_pos[1]))
            if free_space>0:
                for i in range(box_count,0,-1):
                    box_position = (player_pos[0] + (new_player_pos[0] - player_pos[0])*i,
                                    player_pos[1] + (new_player_pos[1] - player_pos[1])*i)
                    board[box_position[0]+(new_player_pos[0] - player_pos[0])][box_position[1]+(new_player_pos[1] - player_pos[1])]="O"
                    board[box_position[0]][box_position[1]]="."
                board[player_pos[0]][player_pos[1]] = board[new_player_pos[0]][new_player_pos[1]]
                board[new_player_pos[0]][new_player_pos[1]] = "@"
                player_pos = new_player_pos
        if verbose: print_board(board)
    return get_rating(board)


def second(verbose=False):
    file = open("15.input", "r")
    board = []
    moves = []
    player_pos = ()
    for i, line in enumerate(file):
        if line.startswith("#"):
            board_line = []
            for j, char in enumerate(line.strip()):
                if char=="O":
                    board_line.append("[")
                    board_line.append("]")
                else:
                    board_line.append(char)
                    board_line.append(char)
                if char == "@":
                    board_line[-1]="."
                    player_pos = (i, j*2)
            board.append(board_line)
        else:
            for char in line.strip():
                moves.append(char)
        pass
    if verbose: print(moves)
    if verbose: print(player_pos)
    if verbose: print(board[player_pos[0]][player_pos[1]])
    if verbose: print_board(board)
    for move in moves:
        new_player_pos = ()
        if move == "<":
            if verbose: print("Moving <")
            new_player_pos = (player_pos[0], player_pos[1] - 1)
        elif move == ">":
            if verbose: print("Moving >")
            new_player_pos = (player_pos[0], player_pos[1] + 1)
        elif move == "v":
            if verbose: print("Moving v")
            new_player_pos = (player_pos[0] + 1, player_pos[1])
        elif move == "^":
            if verbose: print("Moving ^")
            new_player_pos = (player_pos[0] - 1, player_pos[1])
        board_element = board[new_player_pos[0]][new_player_pos[1]]
        if verbose: print("\tPlayer should move from {} to {}".format(player_pos, new_player_pos))
        if verbose: print("\tElement at {} is {}".format(new_player_pos, board_element))
        if board_element == "#":
            if verbose: print("\tCannot move, due to obstacle")
        elif board_element == ".":
            if verbose: print("\tFree space, moving")
            board[player_pos[0]][player_pos[1]] = board_element
            board[new_player_pos[0]][new_player_pos[1]] = "@"
            player_pos = new_player_pos
        elif board_element == "[" or board_element == "]":
            if verbose: print("\tBox ahead!")
            box_position = new_player_pos
            box_count = 0
            free_space=0
            while board[box_position[0]][box_position[1]] == "[" or board[box_position[0]][box_position[1]] == "]":
                box_count = box_count + 1
                box_position=(box_position[0] + (new_player_pos[0] - player_pos[0]),box_position[1] + (new_player_pos[1] - player_pos[1]))
            box_position = new_player_pos
            while board[box_position[0]][box_position[1]] != "#":
                if board[box_position[0]][box_position[1]]==".":
                    free_space=free_space+1
                box_position = (box_position[0] + (new_player_pos[0] - player_pos[0]),
                                box_position[1] + (new_player_pos[1] - player_pos[1]))
            is_break = False
            if free_space>0:
                pass
            player_pos = new_player_pos
        if verbose: print_board(board)
    return get_rating(board)


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first(verbose=False)))
print("Result of Day {} Part 2: {}".format(current_day, second(verbose=True)))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
