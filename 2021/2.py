import helper


def first():
    x = 0
    y = 0
    f = open("2.input", "r", encoding="UTF-8")
    for line in f:
        if "up" in line:
            y = y + int(line.split(" ")[1])
        elif "down" in line:
            y = y - int(line.split(" ")[1])
        elif "forward" in line:
            x = x + int(line.split(" ")[1])
    f.close()
    print(x * y * -1)


def second():
    x = 0
    y = 0
    aim = 0
    f = open("2.input", "r", encoding="UTF-8")
    for line in f:
        if "up" in line:
            aim = aim - int(line.split(" ")[1])
        elif "down" in line:
            aim = aim + int(line.split(" ")[1])
        elif "forward" in line:
            x = x + int(line.split(" ")[1])
            y = y + (aim * int(line.split(" ")[1]))
    f.close()
    print(y * x)
