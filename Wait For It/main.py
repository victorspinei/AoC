import re
def main():
    filenumber = input("File: ")
    with open("i" + filenumber + ".txt", 'r') as f:
        lines = f.readlines()
        result1 = solve_part1(lines)
        result2 = solve_part2(lines) 

    print("Part 1:",result1)
    print("Part 2:",result2)

def solve_part1(lines):
    sum = 1
    times = [int(x) for x in re.findall(r'(\d+)+', lines[0])]
    distances = [int(x) for x in re.findall(r'(\d+)+', lines[1])]

    # print(times, '\n', distances)

    for i in range(len(times)):
        sum *= get_solutions(times[i], distances[i])
    return sum

def solve_part2(lines):
    time = int("".join(re.findall(r'(\d+)+', lines[0])))
    distance = int("".join(re.findall(r'(\d+)+', lines[1])))

    return get_solutions(time, distance)


def get_solutions(time, distance):
    solutions = 0

    for time_holded in range(time):
        if time_holded * (time - time_holded) > distance:
            solutions += 1

    return solutions

if __name__ == "__main__":
    main()