import sys
from pprint import pp
def hash(code):
    sum = 0
    for c in code:
        sum += ord(c)
        sum *= 17
        sum %= 256
    return sum

with open(sys.argv[1], 'r') as f:
    data = f.read().strip().split(',')

ans = 0
for code in data:
    ans += hash(code)

print("Part 1:", ans)

boxes = [[] for _ in range(256)]

for lens in data:
    remove = "-" in lens
    if remove:
        label = lens.split("-")[0]
    else:
        label = lens.split("=")[0]
        focal_lenght = lens.split("=")[1]
    h = hash(label)
    if boxes[h]:
        found = False
        for lense in boxes[h]:
            if lense[0] == label:
                found = True
                if remove:
                    boxes[h].remove(lense)
                    break
                else:
                    lense[1] = focal_lenght
                    break
        if not found and not remove:
            boxes[h].append([label, focal_lenght])
    else:
        if not remove:
            boxes[h].append([label, focal_lenght])

# pp(boxes)
            
ans2 = 0

for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        ans2 += (i + 1) * (j + 1) * int(lens[1])

print("Part 2:", ans2)