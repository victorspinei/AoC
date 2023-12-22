import sys
import pprint
import re
from functools import reduce

with open(sys.argv[1], 'r') as f:
    data = f.readlines()

# pprint.pprint(data)

workflows = dict()
ratings = list()

for line in data:
    if not line.startswith("{"):
        if line != "\n":
            label = line.split("{")[0]
            contditions = ("".join(line.split("{")[1:])[:-2]).split(",")
            workflows[label] = contditions
    if line.startswith("{"):
        rating = {}
        for val in line.strip()[1:-1].split(","):
            rating[val[0]] = int(val.split("=")[1]) 
        ratings.append(rating)
        
         

# pprint.pprint(ratings)  
# pprint.pprint(workflows)
        
def calc(rating, workflow):
    while True:
        if workflow in "AR":
            if workflow == "A":
                return reduce(lambda x, y: x + y, [rating[x] for x in rating])
            else:
                return 0
        for condition in workflows[workflow]:
            if ":" in condition:
                nworkflow = condition.split(":")[1]
                num = int(condition.split(":")[0][2:])
                if condition[1] == ">":
                    if rating[condition[0]] > num:
                        workflow = nworkflow
                        break
                else:
                    if rating[condition[0]] < num:
                        workflow = nworkflow
                        break

            else:
                workflow = condition

        
print(workflows["in"])
ans = 0
for rating in ratings:
    ans += calc(rating, "in")

print("Part 1:", ans)

def count(ranges, name = "in"):
    if name == "R":
        return 0
    if name == "A":
        product = 1
        for lo, hi in ranges.values():
            product *= hi - lo + 1
        return product

    total = 0

    for condition in workflows[name]:
            try:
                lo, hi = ranges[condition[0]]
            except KeyError:
                # print(condition)
                pass
            if ":" in condition:
                nworkflow = condition.split(":")[1]
                num = int(condition.split(":")[0][2:])
                if condition[1] == "<":
                    T = (lo, num - 1)
                    F = (num, hi)
                else:
                    T = (num + 1, hi)
                    F = (lo, num)
                if T[0] <= T[1]:
                    copy = dict(ranges)
                    copy[condition[0]] = T
                    total += count(copy, nworkflow)
                if F[0] <= F[1]:
                    ranges = dict(ranges)
                    ranges[condition[0]] = F
                else:
                    break
            else:
                total += count(ranges, condition)

    return total

print("Part 2:", count({key: (1, 4000) for key in ("xmas")}))