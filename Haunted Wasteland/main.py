import sys, re, math
from pprint import pprint
network = {}
position_points = []
steps_for_each_point = []
with open(sys.argv[1], 'r') as f:    
    lines = f.readlines()
    instructions = "".join(['1' if x == 'R' else '0' for x in lines[0].strip()])
    # print(instructions)
    for i in range(2, len(lines)):
        nodes = re.findall(r'([A-Z|\d]+)', lines[i])
        network[nodes[0]] = (nodes[1], nodes[2])
        if nodes[0].endswith('A'): 
            position_points.append(nodes[0])
            steps_for_each_point.append(0)

    # pprint(len(instructions))
    # pprint(network)
    # print(position_points)

    steps = 0

    # Part 1:
    
    current_node = 'AAA'
    while True:
        if current_node == 'ZZZ':
            break
        for instruction in instructions:
            current_node = network[current_node][int(instruction)]
            if current_node == 'ZZZ':
                break
            steps += 1

    # Part 2:
        
    for i in range(len(position_points)):

        # for instruction in instructions:
        #     position_points[i] = network[position_points[i]][int(instruction)]
        #     steps_for_each_point[i] += 1

        while True:
            current_node = position_points[i] 
            if current_node.endswith('Z'):
                break
            for instruction in instructions:
                position_points[i] = network[position_points[i]][int(instruction)]
                if current_node.endswith('Z'):
                    break
                steps_for_each_point[i] += 1

    result = 1
    for steps in steps_for_each_point:
        result = math.lcm(result, steps)
        
    print("Part 1:", steps)
    print("Part 2:", result)