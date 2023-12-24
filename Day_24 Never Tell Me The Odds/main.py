import sys
import sympy
from functools import reduce

with open(sys.argv[1]) as f:
    lines = [line.strip() for line in f.readlines()]

hailstones = []

for line in lines:
    hailstones.append(list(map(int, line.replace(" @", ",").split(", "))))

# ans = 0
# b_min, b_max = (200000000000000, 400000000000000)

# ans = 0
# for i, p1 in enumerate(hailstones):
#     for p2 in hailstones[:i]:
#         x1, y1, z1, vx1, vy1, vz1 = p1
#         x2, y2, z2, vx2, vy2, vz2 = p2

#         a1, a2 = vy1, vy2
#         b1, b2 = -vx1, -vx2
#         c1, c2 = vy1 * x1 - vx1 * y1, vy2 * x2 - vx2 * y2

#         if a1 * b2 == b1 * a2:
#               continue
#         x = ((c1*b2)-(c2*b1))/((a1*b2)-(a2*b1))
#         y = ((c2*a1)-(c1*a2))/((a1*b2)-(a2*b1))
#         if b_min <= x <= b_max and b_min <= y <= b_max:
#             if (x - x1) * vx1 >= 0 and (y - y1) * vy1 >= 0 and (x - x2) * vx2 >= 0 and (y - y2) * vy2 >= 0:
#                 ans += 1  


# print("Part 1:", ans)

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

equations = []

for sx, sy, sz, vx, vy, vz in hailstones:
    equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
    equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))

answers = sympy.solve(equations)[0]
print(answers[xr] + answers[yr] + answers[zr])