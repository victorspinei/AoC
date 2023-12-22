import sys

map = [list(lines.strip()) for lines in open(sys.argv[1])]

def calculate(map):
    sum = 0
    for y, line in enumerate(map):
        for x, space in enumerate(line):
            if space == "O":
                map[y][x] = '.'
                i = y - 1
                while i >= 0 and map[i][x] == '.':
                    i -= 1
                map[i + 1][x] = 'O'
                sum += len(map) - i - 1
    return sum

ans1 = calculate(map)
print("Part 1", ans1)