import time

def main():
    filenumber = input("File number: ")
    result = 0
    start = time.time()

    with open('i'+ filenumber+'.txt', 'r') as f:
        result = lowest_position(f)
    print("lowest location:", result)

    end = time.time()
    print("Execution time of the program is-", end - start)


    pass

def lowest_position(f):
    positions = [int(x) for x in f.readline().strip().split(' ')[1:]]
    # positions = get_seeds(positions)
    # print(positions)
    lowest = 2**32

    f.readline()

    maps = [get_map(f) for _ in range(7)]
    # pp(maps)
    for i in range(0, len(positions) - 1, +2):
        try:
            changed = [x + positions[i] for x in range(positions[i + 1])]
            continue
        except:
            print(positions[i], positions[-1])
        for pos_index in range(len(changed)):
            skip = False
            if not skip:
                for my_map in maps:
                    for map_range in my_map:
                        if changed[pos_index] >= map_range[1] and changed[pos_index] < map_range[1] + map_range[2]:
                            changed[pos_index] = map_range[0] + changed[pos_index] - map_range[1]
                            break
            lowest = min(changed[pos_index], lowest)
            print(lowest, changed[pos_index])

    return lowest

def get_map(f):
    my_map = []
    f.readline()
    line = f.readline()
    while line != '\n' and line :
        my_map.append(line.strip().split(' '))
        line = f.readline()

    for i in range(len(my_map)):
        for j in range(len(my_map[i])):
            my_map[i][j] = int(my_map[i][j])
    return my_map

def get_seeds(positions):
    changed = []
    for i in range(0, len(positions) - 1, +2):
        changed.extend([x + positions[i] for x in range(positions[i + 1])])
    return changed

if __name__ == '__main__':
    main()