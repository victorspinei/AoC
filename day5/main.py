from pprint import pp

def main():
    with open("i1.txt", 'r') as f:
        result = part1(f)
    print(result)

def part1(f):
    positions = [int(x) for x in f.readline().strip().split()[1:]]

    f.readline()
    maps = [get_map(f) for _ in range(7)]

    for pos_index in range(len(positions)):
        for my_map in maps:
            for sub_range in my_map:
                if positions[pos_index] >= sub_range[1] and positions[pos_index] < sub_range[1] + sub_range[2]:
                    positions[pos_index] = sub_range[0] + positions[pos_index] - sub_range[1]
                    break 


    return min(positions)

def get_map(f):
    my_map = []
    f.readline()

    line = f.readline()
    while line and line != '\n':
        sub_range = line.strip().split()
        my_map.append(sub_range)
        line = f.readline()

    for i in range(len(my_map)):
        for j in range(len(my_map[i])):
            my_map[i][j] = int(my_map[i][j])

    return my_map

if __name__ == "__main__":
    main()