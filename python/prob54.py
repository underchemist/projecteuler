# Tue 18 Mar 2014 06:46:09 PM EDT
#!/usr/bin/env python3.3


class PokerHand():
    def __init__(self, hand_str):
        self.card_val = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                         '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11,
                         'Q': 12, 'K': 13, 'A': 14}
        self.suite_val = {'C': 1, 'D': 2, 'H': 3, 'S': 4}
        self.hand = hand_str.split()
        self.hand_n = sorted(self._read_hand(), key=lambda tup: tup[0])
        self.hand_names = {1: 'high card', 2: 'pair', 3: 'two pairs',
                           4: 'three of a kind', 5: 'straight', 6: 'flush',
                           7: 'full house', 8: 'four of a kind',
                           9: 'straight flush', 10: 'royal flush'}

    def _read_hand(self):
        c = self.card_val
        s = self.suite_val
        return [(c[card[:-1]], s[card[-1]]) for card in self.hand]

    def is_royal_flush(self):
        suite_to_match = self.hand_n[0][1]
        if all(suite[1] == suite_to_match for suite in self.hand_n):
            if all(val[0] == i + 10 for i, val in enumerate(self.hand_n)):
                return True
            else:
                return False
        else:
            return False

    def is_straight_flush(self):
        suite_to_match = self.hand_n[0][1]
        first = self.hand_n[0][0]
        if all(suite[1] == suite_to_match for suite in self.hand_n):
            if all(val[0] == i + first for i, val in enumerate(self.hand_n)):
                return True
            else:
                return False
        else:
            return False

    def is_four_of_a_kind(self):
        values = [value[0] for value in self.hand_n]
        for value in values:
            if values.count(value) == 4:
                return True
        return False

    def is_full_house(self):
        values = [value[0] for value in self.hand_n]
        for value in values:
            if values.count(value) == 3:
                for other_values in values:
                    if values.count(other_values) == 2:
                        return True
        return False

    def is_flush(self):
        suite_to_match = self.hand_n[0][1]
        if all(suite[1] == suite_to_match for suite in self.hand_n):
            return True
        else:
            return False

    def is_straight(self):
        first = self.hand_n[0][0]
        if all(val[0] == i + first for i, val in enumerate(self.hand_n)):
            return True
        else:
            return False

    def is_three_of_a_kind(self):
        # make sure to test AFTER full house else gives false positive
        values = [value[0] for value in self.hand_n]
        for value in values:
            if values.count(value) == 3:
                return True
        return False

    def is_two_pairs(self):
        first = 0
        second = 0
        values = [value[0] for value in self.hand_n]
        for value in values:
            if values.count(value) == 2 and first and first != value:
                second = value
                break
            if values.count(value) == 2:
                first = value
        if first and second:
            return True
        else:
            return False

    def is_pair(self):
        # make sure to test is_two_pairs first
        values = [value[0] for value in self.hand_n]
        for value in values:
            if values.count(value) == 2:
                return True
        return False

    def find_hand(self):
        if self.is_royal_flush():
            return 10
        elif self.is_straight_flush():
            return 9
        elif self.is_four_of_a_kind():
            return 8
        elif self.is_full_house():
            return 7
        elif self.is_flush():
            return 6
        elif self.is_straight():
            return 5
        elif self.is_three_of_a_kind():
            return 4
        elif self.is_two_pairs():
            return 3
        elif self.is_pair():
            return 2
        else:
            return 1

    def tie_value(self):


if __name__ == '__main__':
    poker_hands = []
    with open('poker.txt', 'r') as poker_file:
        for line in poker_file:
            poker_hands.append((line[:14], line[15:].rstrip('\n')))

    player_one_score = 0
    number_of_times_tied = 0
    for hand in poker_hands:
        player_one_hand = PokerHand(hand[0])
        player_two_hand = PokerHand(hand[1])
        if player_one_hand.find_hand() > player_two_hand.find_hand():
            player_one_score += 1
        elif player_one_hand.find_hand() == player_two_hand.find_hand():
            number_of_times_tied += 1

    print('player one won', player_one_score, 'times')
    print('players tied', number_of_times_tied, 'times')
