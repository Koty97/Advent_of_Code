def sum_to_zero(number):
    return int((pow(number, 2) + number) / 2)


def first():
    f = open("7.input", "r", encoding="UTF-8")
    array_of_crabs = [int(i) for i in f.readline().split(",")]
    fuel_variants = {}
    for i in range(min(array_of_crabs), max(array_of_crabs) + 1):
        for element in array_of_crabs:
            try:
                fuel_variants[i] = fuel_variants[i] + abs(element - i)
            except:
                fuel_variants[i] = abs(element - i)
    print(min(fuel_variants.values()))
    f.close()


def second():
    f = open("7.input", "r", encoding="UTF-8")
    array_of_crabs = [int(i) for i in f.readline().split(",")]
    fuel_variants = {}
    for i in range(min(array_of_crabs), max(array_of_crabs) + 1):
        for element in array_of_crabs:
            try:
                fuel_variants[i] = fuel_variants[i] + sum_to_zero(abs(element - i))
            except:
                fuel_variants[i] = sum_to_zero(abs(element - i))
    print(min(fuel_variants.values()))


first()
second()
