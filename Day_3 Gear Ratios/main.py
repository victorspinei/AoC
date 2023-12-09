from functools import reduce

def main():
    lines = []
    with open("i2.txt", "r") as input:
        line = input.readline()
        while line:
            lines.append(line.strip("\n"))
            line = input.readline()

    NUM_LINES = len(lines)
    LINE_LEN = len(lines[0])

    # find all the instances of numbers within the schematic in the form
    # of a tuple, where the first element is the number itself and the second
    # is another tuple, a triple which contains the line the number is on, the
    # start index of the number, and the end index of the number (inclusive)
    nums = []
    for i in range(len(lines)):
        j = 0
        while j < LINE_LEN:
            if lines[i][j].isdecimal():
                start = j
                num = ""
                while j < LINE_LEN and lines[i][j].isdecimal():
                    num += lines[i][j]
                    j += 1
                j -= 1
                nums.append((int(num), (i, start, j)))

            j += 1

    # loop through every instance of a number in the schematic, checking
    # whether any of the characters around it is a symbol. if it is, add the
    # number to the sum
    gears = {}
    for num in nums:
        for i in range(num[1][0] - 1, num[1][0] + 2):
            if i >= 0 and i < NUM_LINES:
                for j in range(num[1][1] - 1, num[1][2] + 2):
                    if j >= 0 and j < LINE_LEN:
                        if lines[i][j] == "*":
                            if not gears.get((i, j)):
                                gears[(i, j)] = []
                            gears[(i, j)].append(num[0])

    gear_ratio_sum = 0
    for gear in gears:
        if len(gears[gear]) == 2:
            gear_ratio_sum += reduce(lambda a, b: a * b, gears[gear])

    print(gear_ratio_sum)



if __name__ == "__main__":
    main()