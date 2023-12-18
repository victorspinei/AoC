import sys
from copy import deepcopy
from pprint import pprint

patterns = [[list(line) for line in lines.split("\n")]
                for lines in open(sys.argv[1], 'r').read().strip().split("\n\n")]

def is_horiz(grid, i):
    n, m = len(grid), len(grid[0])
    for j in range(m):
        for k1 in range(n):
            k2 = i*2+1 - k1
            if not (0 <= k2 < n):
                continue
            if grid[k1][j] != grid[k2][j]:
                return False
            
    return True

def transpose(grid):
    return list(zip(*grid))

def summary(grid, avoid=(-1, -1)):
    n, m = len(grid), len(grid[0])

    horiz = -1
    for i in range(n-1):
        if i != avoid[0] and is_horiz(grid, i):
            horiz = i
            break

    vert = -1
    T = transpose(grid)
    for j in range(m-1):
        if j != avoid[1] and is_horiz(T, j):
            vert = j
            break

    return (horiz, vert)




def summary_2(grid):
    """Fix a smudge, recompute summary."""
    n, m = len(grid), len(grid[0])
    summ_og = summary(grid)

    for i in range(n):
        for j in range(m):
            grid_copy = deepcopy(grid)
            grid_copy[i][j] = "." if grid[i][j] == "#" else "#"

            """ print(i, j)
            print("\n".join(["".join(line) for line in grid_copy])) """

            summ_new = summary(grid_copy, avoid=summ_og)

            if summ_new not in [summ_og, (-1, -1)]:
                if summ_new[0] != -1:
                    contrib = (summ_new[0] + 1) * 100
                else:
                    assert summ_new[1] != -1
                    contrib = summ_new[1] + 1

                return contrib


ans1 = 0
for block in patterns:
    result = summary(block)
    ans1 += (result[0] + 1) * 100 + result[1] + 1

print("Part 1:", ans1)

ans2 = 0

for block in patterns:
    ans2 += summary_2(block)

print("Part 2:", ans2)

