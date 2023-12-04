import re, pprint

PART = 2

def main():
    sum = 0
    file_num = input("File Number: ")
    with open("i"+ file_num + ".txt") as f:
        if PART == 1:
            sum = part1(f)
        else:
            sum = part2(f)

    if PART == 1:
        if file_num == "1":
            if sum == 13:
                print("Part 1 test successful")
            else:
                print("Part 1 test failed")
        elif file_num == "2":
            if sum == 28538:
                print("Part 1 actual test successful")
            else:
                print("Part 1 actual test failed")
    elif PART == 2:
        if file_num == "1":
            if sum == 30:
                print("Part 2 test successful")
            else:
                print("Part 2 test failed")
        elif file_num == "2":
            if sum == 9425061:
                print("Part 2 actual test successful")
            else:
                print("Part 2 actual test failed")

    print("Sum:", sum)

def part1(f):
    sum = 0

    for line in f.readlines():
        winning_numbers = [int(x) for x in re.search(r"(:)( .+)(\|)", line).group(2).split()]
        numbers = [int(x) for x in re.search(r"(\|)( .+)", line).group(2).split()]
        winning_numbers_present = 0
        score = 0
        for number in numbers:
            if number in winning_numbers:
                winning_numbers_present += 1
        if winning_numbers_present > 0:
            score = 1
            winning_numbers_present -= 1
            while winning_numbers_present != 0:
                score *= 2
                winning_numbers_present -= 1
        sum += score


        # print(numbers)
    return sum

def part2(f):
    sum = 0

    scratch_cards_matching = []
    for line in f.readlines():
        winning_numbers = [int(x) for x in re.search(r"(:)(.+)(\|)", line).group(2).split()]
        numbers = [int(x) for x in re.search(r"(\|)(.+)", line).group(2).split()]
        matching = 0
        for number in numbers:
            if number in winning_numbers:
                matching += 1
        scratch_cards_matching.append(matching)
    
    # pprint.pprint(scratch_cards_matching)

    # index is the card index and the value is the number of cards
    total_cards = [] 
    for _ in range(len(scratch_cards_matching)):
        total_cards.append(1)

    for scratch_card_index in range(len(total_cards)):
        for _ in range(total_cards[scratch_card_index]):
            for i in range(scratch_cards_matching[scratch_card_index]):
                total_cards[scratch_card_index + i + 1] += 1
    
    # pprint.pprint(total_cards)

    for cards in total_cards:
        sum += cards

    return sum

if __name__ == "__main__":
    main()