import helper


def first():
    f = open("1.input", "r", encoding="UTF-8")
    num_of_increasing = 0
    last = int(f.readline().replace("\n", ""))
    for x in f:
        x = int(x.replace("\n", ""))
        num_of_increasing += 1 if x > last else 0
        last = x
    print(num_of_increasing)


def second():
    stack = []
    last_sum = 0
    num_of_increasing = 0
    f = open("1.input", "r", encoding="UTF-8")
    for x in f:
        x = int(x.replace("\n", ""))
        helper.add_to_stack(stack, x)
        num_of_increasing += 1 if helper.sum_stack(stack) > last_sum else 0
        last_sum = helper.sum_stack(stack)
    print(num_of_increasing - 1)
