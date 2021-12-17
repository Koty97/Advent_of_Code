def is_winning_board(board):
    winning_line = len(board) * ["X"]
    for line in board:
        if line == winning_line:
            return True
    for x in range(0, len(board)):
        column = []
        for line in board:
            column.append(line[x])
        if column == winning_line:
            return True
        column = []
    return False


def get_board_result(board, called_number):
    result = 0
    for line in board:
        for number in line:
            if number != "X":
                result = result + int(number)
    return result * int(called_number)


def first():
    f = open("4.input", "r", encoding="UTF-8")
    drawn_numbers = f.readline().replace("\n", "").split(",")
    matrix = []
    array = []
    for line in f:
        if line != "\n":
            line = line.replace("\n", "").replace("  ", " ")
            if line[0] == " ":
                line = line[1:]
            array.append(line.split(" "))
        elif array:
            matrix.append(array)
            array = []

    for number in drawn_numbers:
        for board in matrix:
            for line in board:
                if number in line:
                    line[line.index(number)] = "X"
            if is_winning_board(board):
                print(get_board_result(board, number))
                return 0


def second():
    f = open("4.input", "r", encoding="UTF-8")
    drawn_numbers = f.readline().replace("\n", "").split(",")
    matrix = []
    array = []
    for line in f:
        if line != "\n":
            line = line.replace("\n", "").replace("  ", " ")
            if line[0] == " ":
                line = line[1:]
            array.append(line.split(" "))
        elif array:
            matrix.append(array)
            array = []

    for number in drawn_numbers:
        for board in matrix:
            for line in board:
                if number in line:
                    line[line.index(number)] = "X"
            if is_winning_board(board):
                if len(matrix) != 1:
                    matrix.remove(board)
                    drawn_numbers.insert(drawn_numbers.index(number), number)
                else:
                    print(get_board_result(board, number))
                    return 0


first()

second()
