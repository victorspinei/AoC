import sys
from copy import deepcopy

grid = [list(lines.strip()) for lines in open(sys.argv[1])]
n, m = len(grid), len(grid[0])

def north_load(grid):
    n, m = len(grid), len(grid[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'O':
                ans += n - i
    return ans

def tilt_up(grid):
    n, m = len(grid), len(grid[0])

    for j in range(m):
        i = 0
        while i < n:
            while i < n and grid[i][j] == "#":
                i += 1 
            
            count = 0
            start = i
            while i < n and grid[i][j] != "#":
                if grid[i][j] == "O":
                    count += 1
                i += 1

            for i1 in range(start, start + count):
                grid[i1][j] = 'O'
            for i1 in range(start + count, i):
                grid[i1][j] = '.'

    return grid

def rotate_90(grid):
    new_grid = [[None] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            new_grid[i][j] = grid[j][m - 1-i]
    return new_grid

def rotate(grid, i):
    grid_copy = deepcopy(grid)
    for _ in range(i % 4):
        grid_copy = rotate_90(grid_copy)
    return grid_copy

cycle2grid = {}
seen = {}

def get_hash(grid):
    return "\n".join(["".join(line) for line in grid])

def do_cycle(grid):
    grid_copy = deepcopy(grid)
    for i in range(4):
        grid_copy = rotate(grid_copy, 4 - (i % 4))
        grid_copy = tilt_up(grid_copy)
        grid_copy = rotate(grid_copy, i % 4)
    return grid_copy

for cycle in range(10**9):
    grid = do_cycle(grid)

    h = get_hash(grid)
    if h in seen:
        period = cycle - seen[h]
        ans_grid = cycle2grid[(10**9 - 1 - seen[h]) % period + seen[h]]
        print(north_load(ans_grid))
        break

    seen[get_hash(grid)] = cycle
    cycle2grid[cycle] = deepcopy(grid)