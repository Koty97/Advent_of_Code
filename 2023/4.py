import os.path
import re

current_day = os.path.basename(__file__.split(".")[0])


def first(verbose=False):
    file = open("4.input", "r")
    summary = 0
    for line in file:
        scratched_numbers = line.split(":")[1].split("|")[0].strip().replace("  ", " ").split(" ")
        winning_numbers = line.split(":")[1].split("|")[1].strip().replace("  ", " ").split(" ")
        points = 0
        count = 0
        for number in scratched_numbers:
            if number in winning_numbers:
                if count == 0:
                    points = points + 1
                else:
                    points = points * 2
                count = count + 1
        if verbose:
            print(scratched_numbers)
        if verbose:
            print(winning_numbers)
        summary = summary + points
        if verbose:
            print(points)
        if verbose:
            print("---------------------")
    return summary


def second(verbose=False):
    file = open("4.input", "r")
    summary = 0
    regex_string = "Card\\s+(\\d+):"
    scratchcards = {}
    for line in file:
        name = re.search(regex_string, line).group(1)
        scratched_numbers = line.split(":")[1].split("|")[0].strip().replace("  ", " ").split(" ")
        winning_numbers = line.split(":")[1].split("|")[1].strip().replace("  ", " ").split(" ")
        properties = {"count": 1, "scratched_numbers": scratched_numbers, "winning_numbers": winning_numbers}
        scratchcards[name] = properties
    for x in scratchcards:
        count = 0
        if verbose:
            print("Processing card with index: {}".format(x))
        if verbose:
            print("\t with count: {}".format(scratchcards[x]["count"]))
        for iteration in range(0, scratchcards[x]["count"]):
            for number in scratchcards[x]["scratched_numbers"]:
                if number in scratchcards[x]["winning_numbers"]:
                    count = count + 1
                    if verbose:
                        print("Number found: {}".format(number))
            if verbose:
                print("Steps to increment: {}".format(count))
            to_hold = 0
            for i in range(count, 0, -1):
                if str(int(x) + i) in scratchcards:
                    if verbose:
                        print("Updating index: {}".format(str(int(x) + i)))
                    if verbose:
                        print("Original count: {}".format(scratchcards[str(int(x) + i)]["count"]))
                    scratchcards[str(int(x) + i)]["count"] = scratchcards[str(int(x) + i)]["count"] + 1
                    if verbose:
                        print("New count: {}".format(scratchcards[str(int(x) + i)]["count"]))
                else:
                    to_hold = to_hold + 1
            count = 0
            if verbose:
                print("----")
        if verbose:
            print("---------------")
    if verbose:
        print(scratchcards)
    for card in scratchcards:
        summary = summary + scratchcards[card]["count"]
    return summary


print("Result of Day {} Part 1: {}".format(current_day, first()))
print("Result of Day {} Part 2: {}".format(current_day, second()))
