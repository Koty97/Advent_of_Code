import os.path

current_day = os.path.basename(__file__.split(".")[0])


def first(verbose=False):
    file = open("2.input", "r")
    summary = 0
    for line in file:
        numbers = list(map(int, line.strip().split(" ")))
        is_ok = True
        if verbose: print("Number row {}".format(numbers))
        if numbers == sorted(numbers) or numbers == sorted(numbers, reverse=True):
            if verbose: print("\tRow succeeded first test.")
            for i in range(0, len(numbers)):
                if 0 < i < len(numbers):
                    if verbose: print(
                        "\tChecking if number {} is 1-3 away: {}, change was {}".format(numbers[i], 0 < abs(
                            int(numbers[i]) - int(numbers[i - 1])) < 4, abs(
                            int(numbers[i]) - int(numbers[i - 1]))))
                    if (0 < abs(int(numbers[i]) - int(numbers[i - 1])) < 4) is False:
                        is_ok = False
        else:
            if verbose: print("\tRow did not succeed first test.")
            is_ok = False
        if verbose: print("\tNumber row {} is {}".format(numbers, is_ok))
        summary = summary + int(is_ok)
    return summary


def second(verbose=False):
    file = open("2.input", "r")
    summary = 0
    failed=0
    tries=0
    for line in file:
        numbers = list(map(int, line.strip().split(" ")))
        is_ok = True
        if verbose: print("Number row {}".format(numbers))
        if numbers == sorted(numbers) or numbers == sorted(numbers, reverse=True):
            if verbose: print("\tRow succeeded first test.")
            for i in range(0, len(numbers)):
                if 0 < i < len(numbers):
                    if verbose: print(
                        "\tChecking if number {} is 1-3 away: {}, change was {}".format(numbers[i], 0 < abs(
                            int(numbers[i]) - int(numbers[i - 1])) < 4, abs(
                            int(numbers[i]) - int(numbers[i - 1]))))
                    if (0 < abs(int(numbers[i]) - int(numbers[i - 1])) < 4) is False:
                        is_ok = False
        else:
            if verbose: print("\tRow did not succeed first test.")
            is_ok = False
        if not is_ok:
            if verbose: print("\tRow failed tests, evaluating exceptions for part 2.")
            for i in range(0, len(numbers)):
                new_numbers = numbers.copy()
                new_numbers.pop(i)
                if verbose: print("\tNew row {}".format(new_numbers, is_ok))
                if new_numbers == sorted(new_numbers) or new_numbers == sorted(new_numbers, reverse=True):
                    if verbose: print("\t\tNew row succeeded first test.")
                    failed_tries=0
                    for i in range(0, len(new_numbers)):
                        if 0 < i < len(new_numbers):
                            if verbose: print(
                                "\t\tChecking if number {} is 1-3 away: {}, change was {}".format(new_numbers[i], 0 < abs(
                                    int(new_numbers[i]) - int(new_numbers[i - 1])) < 4, abs(
                                    int(new_numbers[i]) - int(new_numbers[i - 1]))))
                            if (0 < abs(int(new_numbers[i]) - int(new_numbers[i - 1])) < 4) is False:
                                failed_tries=failed_tries+1
                    if failed_tries==0:
                        if verbose: print("\t\tException managed successfully\n")
                        is_ok=True
                        break
        if verbose: print("\tNumber row {} is {}\n".format(numbers, is_ok))
        summary = summary + int(is_ok)
    return summary


print("Result of Day {} Part 1: {}".format(current_day, first()))
print("Result of Day {} Part 2: {}".format(current_day, second(True)))
