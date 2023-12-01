import time

numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'zero': 10,
}

# i3 - 281

def main():
    sum = 0
    file = input("Type file name: ")
    with open(file + '.txt', 'r') as f:
        sum = part2(f)
        print(sum)

def part1(f):
    sum = 0
    for line in f.readlines():
        line_sum = 0

        for c in range(len(line) - 1):
            if line[c].isdigit():
                line_sum += int(line[c]) * 10 
                break

        for c in range(len(line) - 1, -1, -1):
            if line[c].isdigit():
                line_sum += int(line[c]) 
                break
        sum += line_sum
    return sum

def part2(f):
    sum = 0

    for line in f.readlines():
        line_sum = 0
        for i in range(len(line) -1):
            found = False
            for n in numbers:
                if n in line[0:i]:
                    line_sum += numbers[n] * 10
                    found = True
                    break
            if found:
                break
            if line[i].isdigit():
                line_sum += int(line[i]) * 10
                break

        for i in range(len(line) - 1, -1, -1):
            found = False
            for n in numbers:
                if n in line[i:]:
                    line_sum += numbers[n]
                    found = True
                    break
            if found:
                break
            if line[i].isdigit() and not found:
                line_sum += int(line[i])
                break
        sum += line_sum
        # print(line, end='')
        # print(line_sum)
    
    return sum


if __name__ == '__main__':
    main()
