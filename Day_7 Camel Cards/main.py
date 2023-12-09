import sys
import pprint
from collections import Counter

CARD_MAPPING = {'T': 'A', 'J': '.', 'Q': 'C', 'K': 'D', 'A': 'E'} # this basically transforms the cards into ordered alfphabed order

def main(args):
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        plays = [(line.strip().split()[0], int(line.strip().split()[1])) for line in lines]
   

        plays.sort(key=lambda play: sorting(play[0]))

        sum = 0

        for i in range(len(plays)):
            sum += plays[i][1] * (i+1)

        print(sum)

def find_all_combinations(hand):
    if not hand:
        return [""]

    current_card = hand[0]
    if current_card == 'J':
        possible_values = "23456789TQKA"
    else:
        possible_values = current_card

    combinations = [
        first_half + second_half
        for first_half in possible_values
        for second_half in find_all_combinations(hand[1:])
    ]

    return combinations

def find_max_type(hand):
    return max(map(get_type, find_all_combinations(hand)))

def sorting(hand):
    return find_max_type(hand), get_order(hand) # i guess the sort function accepts tuples as the key

def get_order(hand):
    return [CARD_MAPPING.get(card, card) for card in hand]

def get_type(hand):
    counts = Counter(hand)
    if len(counts) == 1:
        return 6
    if len(counts) == 2:
        if 4 in counts.values():
            return 5
        if 3 in counts.values() and 2 in counts.values():
            return 4
    if len(counts) == 3:
        if 3 in counts.values() and list(counts.values()).count(1) == 2:
            return 3
        if list(counts.values()).count(2) == 2:
            return 2
    if len(counts) == 4:
        return 1
    return 0


    

if __name__ == '__main__':
    main(sys.argv)
