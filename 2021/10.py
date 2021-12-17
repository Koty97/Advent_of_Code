def first():
    f = open("10.input", "r", encoding="UTF-8")
    stack = []
    available_characters = {"(": ")", "<": ">", "{": "}", "[": "]"}
    values = {")": 3, "]": 57, "}": 1197, ">": 25137}
    i = 0
    for line in f:
        line = line.replace("\n", "")
        for char in line:
            if char in available_characters.keys():
                stack.append(char)
            else:
                pop = stack.pop()
                if char != available_characters.get(pop):
                    i = i + int(values.get(char))
    print(i)


def second():
    f = open("10.input", "r", encoding="UTF-8")
    stack = []
    available_characters = {"(": ")", "<": ">", "{": "}", "[": "]"}
    values = {")": 1, "]": 2, "}": 3, ">": 4}
    results = []
    i = 0
    error = False
    for line in f:
        line = line.replace("\n", "")
        for char in line:
            if char in available_characters.keys():
                stack.append(char)
            else:
                pop = stack.pop()
                if char != available_characters.get(pop):
                    error = True
        if not error:
            stack.reverse()
            for char in stack:
                i = i * 5 + int(values.get(available_characters.get(char)))
            results.append(int(i))
        stack = []
        i = 0
        error = False
    results.sort()
    print(results[int((len(results)) / 2)])


first()
second()
