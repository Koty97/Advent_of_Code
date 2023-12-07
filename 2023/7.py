import os.path
import re

current_day = os.path.basename(__file__.split(".")[0])


def get_hand_score(hand, verbose):
    score = 0
    cards = {}
    values = []
    for card in hand:
        if card in cards:
            cards[card] = cards[card] + 1
        else:
            cards[card] = 1
    for card in cards.values():
        values.append(card)
    values = sorted(values)
    if verbose: print(cards, sorted(values))
    if 5 in values:
        if verbose: print("Five of a kind")
        score = 7
    elif 4 in values:
        if verbose: print("Four of a kind")
        score = 6
    elif 3 in values and 2 in values:
        if verbose: print("Full house")
        score = 5
    elif 3 in values:
        if verbose: print("Three of a kind")
        score = 4
    elif len(values) == 3 and values[0] == 1 and values[1] == 2 and values[2] == 2:
        if verbose: print("Two pair")
        score = 3
    elif len(values) == 4 and values[3] == 2:
        if verbose: print("One pair")
        score = 2
    elif len(values) == 5:
        if verbose: print("High card")
        score = 1
    return score


def first(verbose=False):
    file = open("7.input", "r")
    hands = []
    bids = []
    for line in file:
        hands.append(line.split(" ")[0].strip())
        bids.append(int(line.split(" ")[1].strip()))
    if verbose: print(hands)
    if verbose: print(bids)
    hands_dict = {}
    for hand in hands:
        score = get_hand_score(hand, verbose)
        hands_dict[hand] = score
    if verbose: print(hands_dict)
    for hand in hands_dict:
        for hand2 in hands_dict:
            if hand != hand2:
                print("Comparing {} with {}; {} vs {}; winning {}".format(hand,hand2,hands_dict[hand],hands_dict[hand2],""))
        # COMPARE
        print(hand, hands_dict[hand])
        pass
    summary = 0
    return summary


def second(verbose=False):
    file = open("7.input", "r")
    summary = 0

    return summary


print("Result of Day {} Part 1: {}".format(current_day, first()))
print("Result of Day {} Part 2: {}".format(current_day, second()))
