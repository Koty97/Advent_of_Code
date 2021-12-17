def sum_dictionary(dictionary):
    sum_dict = 0
    for key in dictionary:
        sum_dict = sum_dict + dictionary[key]
    return (sum_dict)


def first_old(iterations):
    f = open("6.input", "r", encoding="UTF-8")
    fish = f.readline().split(",")
    how_many_to_add = 0
    for x in range(0, iterations):
        for y in range(0, how_many_to_add):
            fish.append(9)
        how_many_to_add = 0
        for i, fi in enumerate(fish):
            fi = int(fi)
            if fi - 1 < 0:
                fi = 7
            elif fi - 1 == 0:
                how_many_to_add = how_many_to_add + 1
            fish[i] = fi - 1
    f.close()


def first(iterations):
    f = open("6.input", "r", encoding="UTF-8")
    fish = f.readline().split(",")
    count = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }  # LAMBDA
    new_count = {}
    six_to_add = 0
    for fi in fish:
        count[int(fi)] = count[int(fi)] + 1
    for x in range(0, iterations):
        for idx in count:
            if idx != 0:
                new_count[idx - 1] = count[idx]
            else:
                new_count[8] = count[idx]
                if count[idx] != 0:
                    six_to_add = six_to_add + count[idx]
        new_count[6] = new_count[6] + six_to_add
        count = new_count
        six_to_add = 0
        new_count = {}
    f.close()
    #print(sum_dictionary(count))


def second():
    first(256)


import time

f = open("6_old.output", "a", encoding="UTF-8")

for x in range(1, 257):
    print(x)
    start = time.time()
    first_old(x)
    end = time.time()
    f.write("{},{}\n".format(x, end - start))
#first(105)


# second()
