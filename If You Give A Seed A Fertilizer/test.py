import time

def main():
    filenumber = input("File number: ")
    result = 0
    start = time.time()

    with open('i' + filenumber + '.txt', 'r') as f:
        result = lowest_position(f)
    print("lowest location:", result)

    end = time.time()
    print("Execution time of the program is-", end - start)

def lowest_position(f):
    positions = (int(x) for x in f.readline().strip().split(' ')[1:])
    positions = get_seeds(positions)
    lowest = float('inf')
    f.readline()

    maps = [get_map(f) for _ in range(7)]

    for i in range(len(positions)):
        for my_map in maps:
            for map_range in my_map:
                if map_range[1] <= positions[i] < map_range[1] + map_range[2]:
                    positions[i] = map_range[0] + (positions[i] - map_range[1])
                    lowest = min(lowest, positions[i])
                    break
        if lowest == 0:  # Early exit if minimum is found
            break

    return lowest

def get_map(f):
    my_map = []
    f.readline()
    line = f.readline()
    while line != '\n' and line:
        my_map.append(list(map(int, line.strip().split())))
        line = f.readline()
    return my_map

def get_seeds(positions):
    changed = []
    for i in range(0, len(positions) - 1, +2):
        changed.extend(x + positions[i] for x in range(positions[i + 1]))
    return changed

main()
