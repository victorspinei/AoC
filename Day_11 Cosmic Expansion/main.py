import sys, pprint

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines()]

temp = []
for line in lines:
    temp.append([c for c in line])
# pprint.pp(lines)
# THis is a mistake because i can just add + 1 if the row is emptyr by checking automatically
# def expand_universe(lines):
#     changed = []
#     # horizontal
#     for line in lines:
#         if all(c == '.' for c in line):
#             changed.append('.' * len(line))
#         changed.append(line)

#     # vertical
#     for i in range(len(lines[0])):
#         change = all(lines[j][i] == '.' for j in range(len(lines)))

#         if change:
#             for k in range(len(changed)):
#                 changed[k] = changed[k][:i] + '.' + changed[k][i:]

#     return changed

# my_map = expand_universe(lines)
# pprint.pprint(my_map)
# print(len(lines[0]), len(my_map[0]))


# find all of the coords of the galaxies

galaxies = []
for i, line in enumerate(lines):
    for j in range(len(line)):
        if line[j] != '.':
            galaxies.append((i, j))

# pprint.pp(galaxies)

# find all of the pairs
# https://en.wikipedia.org/wiki/Cartesian_product
pairs = []
for i in range(len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
        pairs.append([galaxies[i], galaxies[j]])

# print(len(pairs))
n, m = len(lines), len(lines[0])

empty_row = [all([lines[i][j] == "." for j in range(m)]) for i in range(n)]
empty_col = [all([lines[i][j] == "." for i in range(n)]) for j in range(m)]

# https://simple.wikipedia.org/wiki/Manhattan_distance
def dist(a, b):
    i1, j1 = a
    i2, j2 = b

    i1, i2 = min(i1, i2), max(i1, i2)
    j1, j2 = min(j1, j2), max(j1, j2)

    ans = 0
    for i in range(i1, i2):
        ans += 1
        if empty_row[i]:
            ans += 1000000 - 1
    for j in range(j1, j2):
        ans += 1
        if empty_col[j]:
            ans += 1000000 - 1

    return ans


ans = 0
for i in pairs:
    ans += dist(i[0], i[1])

print(ans)