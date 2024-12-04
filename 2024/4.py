import os.path
import re
from time import perf_counter

current_day = os.path.basename(__file__.split(".")[0])
def transpose(text):
    r_text = ""
    matrix = []
    for line in text.split("\n"):
        line_matrix = []
        for char in line.strip():
            line_matrix.append(char)
        matrix.append(line_matrix)
    t_matrix = list(zip(*matrix))
    for line in list(t_matrix):
        for char in line:
            r_text = r_text + char
        r_text = r_text + "\n"
    return r_text


def findstrcount(regex_search, text):
    summary = 0
    for line in text.split("\n"):
        re_result = re.findall(regex_search, line)
        summary = summary + len(re_result)
    return summary


def finddiagcount(text):
    summary = 0
    matrix = []
    for line in text.split("\n"):
        line_matrix = []
        for char in line.strip():
            line_matrix.append(char)
        matrix.append(line_matrix)
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            if matrix[row][col] == "X":
                try:
                    if row + 1 >= 0 and col + 1 >= 0 and matrix[row + 1][col + 1] == "M":
                        if row + 2 >= 0 and col + 2 >= 0 and matrix[row + 2][col + 2] == "A":
                            if row + 3 >= 0 and col + 3 >= 0 and matrix[row + 3][col + 3] == "S":
                                summary = summary + 1
                except:
                    pass
                try:
                    if row + 1 >= 0 and col - 1 >= 0 and matrix[row + 1][col - 1] == "M":
                        if row + 2 >= 0 and col - 2 >= 0 and matrix[row + 2][col - 2] == "A":
                            if row + 3 >= 0 and col - 3 >= 0 and matrix[row + 3][col - 3] == "S":
                                summary = summary + 1
                except:
                    pass
                try:
                    if row - 1 >= 0 and col - 1 >= 0 and matrix[row - 1][col - 1] == "M":
                        if row - 2 >= 0 and col - 2 >= 0 and matrix[row - 2][col - 2] == "A":
                            if row - 3 >= 0 and col - 3 >= 0 and matrix[row - 3][col - 3] == "S":
                                summary = summary + 1
                except:
                    pass
                try:
                    if row - 1 >= 0 and col + 1 >= 0 and matrix[row - 1][col + 1] == "M":
                        if row - 2 >= 0 and col + 2 >= 0 and matrix[row - 2][col + 2] == "A":
                            if row - 3 >= 0 and col + 3 >= 0 and matrix[row - 3][col + 3] == "S":
                                summary = summary + 1
                except:
                    pass
    return summary


def first(verbose=False):
    file = open("4.input", "r")
    summary = 0
    file_content = file.read()
    summary = summary + findstrcount("XMAS", file_content)
    summary = summary + findstrcount("SAMX", file_content)
    summary = summary + findstrcount("XMAS", transpose(file_content))
    summary = summary + findstrcount("SAMX", transpose(file_content))
    summary = summary + finddiagcount(file_content)
    file.close()
    return summary


def second(verbose=False):
    file = open("4.input", "r")
    summary = 0
    matrix = []
    for line in file:
        line_matrix = []
        for char in line.strip():
            line_matrix.append(char)
        matrix.append(line_matrix)
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            if matrix[row][col] == "A":
                try:
                    word = matrix[row - 1][col - 1] + matrix[row][col] + matrix[row + 1][col + 1]
                    if word == "MAS" or word == "SAM":
                        word = matrix[row - 1][col + 1] + matrix[row][col] + matrix[row + 1][col - 1]
                        if word == "MAS" or word == "SAM":
                            summary = summary + 1
                except:
                    pass
    return summary


time_start = perf_counter()
print("Result of Day {} Part 1: {}".format(current_day, first()))
print("Result of Day {} Part 2: {}".format(current_day, second()))
time_end = perf_counter()
print(f'Took {time_end - time_start} seconds')
