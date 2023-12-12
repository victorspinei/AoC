import sys, re, pprint
starting_coordinates = ()
maze = []

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        row = re.findall(r'.', line)

        maze.append(row)
            
for i, row in enumerate(maze):
    for j, col in enumerate(row):
        if col == 'S':
            starting_coordinates = i, j

# pprint.pp(maze)

# [['.', '.', '.', '.', '.'],
#  ['.', 'S', '-', '7', '.'],
#  ['.', '|', '.', '|', '.'],
#  ['.', 'L', '-', 'J', '.'],
#  ['.', '.', '.', '.', '.']]

# a fucntion to find neighbors
def get_ngbrs(coords):
    ngbrs = []
    # North
    try: 
        if maze[coords[0] - 1][coords[1]] in '|7F':
            ngbrs.append((coords[0] - 1, coords[1]))
    except:
        pass
    # East
    try:  
        if maze[coords[0]][coords[1] + 1] in '-7J':
            ngbrs.append((coords[0], coords[1] + 1))
    except:
        pass
    # South
    try:  
        if maze[coords[0] + 1][coords[1]] in '|JL':
            ngbrs.append((coords[0] + 1, coords[1]))
    except:
        pass
    # West
    try:  
        if maze[coords[0]][coords[1] - 1] in '-FL':
            ngbrs.append((coords[0], coords[1] - 1))
    except:
        pass
    
    return ngbrs

# print(get_ngbrs(starting_coordinates))

# bfs https://en.wikipedia.org/wiki/Breadth-first_search
def bfs(graph, start):
    visited = {}
    queue = []
    depth = 0
    visited[start] = depth
    queue.append(start)

    while queue:
        current_node = queue.pop(0)
        depth = visited[current_node] + 1

        for neighbor in graph(current_node):
            if neighbor not in visited:
                visited[neighbor] = depth
                queue.append(neighbor)

    return visited

visited_nodes = bfs(get_ngbrs, starting_coordinates)
print(max(visited_nodes.values()))
# https://en.wikipedia.org/wiki/Point_in_polygon
def count_invs(i, j):
    line = maze[i]
    count = 0
    for k in range(j):
        if not (i, k) in visited_nodes:
            continue
        count += line[k] in {"J", "L", "|"}

    return count
ans = 0
for i, line in enumerate(maze):
    for j in range(len(line)):
        if not (i, j) in visited_nodes:
            # https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule
            if count_invs(i, j) % 2 == 1:
                ans += 1

print("part 2:", ans)