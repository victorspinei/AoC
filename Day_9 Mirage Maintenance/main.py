import sys, pprint
from functools import reduce
# my solution
def find_next_number(numbers):
    differences = []
    differences.append(numbers)
    index = 0
    while any(differences[-1]):
        current = [differences[index][i] - differences[index][i - 1] for i in range(1, len(differences[index]))]
        differences.append(current)
        index += 1

    for i in range(len(differences) - 2, -1, -1):
        differences[i].append(differences[i][-1] + differences[i + 1][-1])

    return differences[0][-1]

# https://youtu.be/qbP0p673l8M?si=tkSET6EjBU-Mwez9
def extrapolate(nums):
    if not any(nums):
        return 0
    deltas = [y - x for x, y in zip(nums, nums[1:])]
    diff = extrapolate(deltas)
    return nums[-1] + diff

sum = 0
sum2 = 0
sum_part2_1 = 0
sum_part2_2 = 0

for line in open(sys.argv[1], 'r'):
    nums = list(map(int, line.split()))
    sum += extrapolate(nums)
    sum2 += find_next_number(nums)
    sum_part2_1 += extrapolate(nums[::-1])
    sum_part2_2 += find_next_number(nums[::-1])

print("Part 1:", sum, sum2)
print("Part 2:", sum_part2_1, sum_part2_2)