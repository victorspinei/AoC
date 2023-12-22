import sys
import math

with open(sys.argv[1], 'r') as f:
    data = [line.strip() for line in f.readlines()]

# print(data)
    
# https://en.wikipedia.org/wiki/Shoelace_formula
# https://en.wikipedia.org/wiki/Pick%27s_theorem
    
points = [(0, 0)]
b = 0
dirs = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

parse_direction = {"0": "R", "1": "D", "2": "L", "3": "U"}

for line in data:
    d, n, h = line.split()

    distance = h[2:7]
    direction = h[-2]
    d = parse_direction.get(direction, direction)

    dr, dc = dirs[d]
    n = int(distance, 16)
    r, c = points[-1]
    points.append((r + dr * n, c + dc * n))
    b += n

# print(points)
    
A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2
i = A - b // 2 + 1
print(b + i)