# Tue 18 Mar 2014 06:46:09 PM EDT
#!/usr/bin/env python

def card_value(card_value):
    if card_value.isdigit():
        return int(card_value)
    else:
        if card_value == "T":
            return 10
        elif card_value == "J":
            return 11
        elif card_value == "Q":
            return 12
        elif card_value == "K":
            return 13
        else:
            return 14

def suite_value(suite):
    if suite == "C":
        return 0
    elif suite == "D":
        return 1
    elif suite == "H":
        return 2
    elif suite == "S":
        return 3

def suite_count(suites):
    suite_count = [0] * 4

    for suite in suites:
        suite_count[suite_value(suite)] += 1

    return suite_count

def is_royal(values):
    if 10 in values and 11 in values and 12 in values and 13 in values and 14 in values:
        return True
    else:
        return False

def is_straight(values):
    values = sorted(values)
    initial = values[0]

    for value in values:
        if value == initial:
            initial += 1
        else:
            return False

    return True

def hand_value(hand):
    hands = {'royal flush': 10,
             'straight flush': 9,
             'four of a kind': 8,
             'full house': 7,
             'flush': 6,
             'straight': 5,
             'three of a kind': 4,
             'two pairs': 3,
             'one pair': 2,
             'high card': 1}

    cards = hand.split(" ")
    values = [card_value(card[0]) for card in cards]
    suites = [card[1] for card in cards]
    suiteCount = suite_count(suites)

    print cards
    print values
    print suites
    print suiteCount

    # check if royal flush, straight flush, or flush
    for i in range(4):
        if suiteCount[i] == 5:
            if is_royal(values):
                return hands['royal flush']
            elif is_straight(values):
                return hands['straight flush']
            else:
                return hands['flush']


if __name__ == '__main__':
    print hand_value('9D TD JD QD KD')