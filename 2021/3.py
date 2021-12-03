import helper


def first():
    num_of_steps = 0
    num_of_chars = 0
    f = open("3.input", "r", encoding="UTF-8")
    temp = f.readline().replace("\n", "")
    for line in f:
        if num_of_steps == 0: num_of_chars = len(line.replace("\n", ""))
        num_of_steps = num_of_steps + 1
    f.close()
    f = open("3.input", "r", encoding="UTF-8")
    gamma, epsilon = "", ""
    final = [0] * num_of_chars
    for line in f:
        for i, char in enumerate(temp):
            final[i] = final[i] + int(line[i])
    for i, val in enumerate(final):
        gamma = gamma + str(int(final[i] > num_of_steps / 2))
        epsilon = epsilon + str(int(final[i] < num_of_steps / 2))
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print(gamma * epsilon)


def second():
    result = 1
    for n in range(0, 2):
        line_list = []
        f = open("3.input", "r", encoding="UTF-8")
        length = 0
        for line in f:
            length = len(line)
            line_list.append(line.replace("\n", ""))
        for x in range(0, length):
            most_common = str(helper.get_most_common(line_list, x))
            if n == 0:
                most_common = "0" if most_common == "1" else "1"
            if len(line_list) > 1:
                line_list = list(filter(lambda l: l[x] == most_common, line_list))
        result = result * int(line_list[0], 2)
        f.close()
    print(result)


first()
second()
