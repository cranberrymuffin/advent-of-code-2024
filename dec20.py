start = None
end = None
map = []

def manhattan_distance(pos1, pos2):
    return abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])

def find_cheats(path, version = 'v1'):
    if version == 'v1':
        cheat_distance = 2
    else:
        cheat_distance = 20
    cheats = {}
    for start_idx, start_pos in enumerate(path):
        for end_idx, end_pos in enumerate(path):
            if(end_idx <= start_idx):
                continue
            dist = manhattan_distance(start_pos, end_pos)
            if dist <= cheat_distance and dist >= 2:
                cheats[start_pos, end_pos] = end_idx - start_idx - dist

    return cheats

def find_neighbors(pos):
    neighbors = []
    if pos[0] - 1 >= 0 and map[pos[0] - 1][pos[1]] != '#':
        neighbors.append((pos[0] - 1, pos[1]))
    if pos[0] + 1 < len(map) and map[pos[0] + 1][pos[1]] != '#':
        neighbors.append((pos[0] + 1, pos[1]))
    if pos[1] - 1 >= 0 and map[pos[0]][pos[1] - 1] != '#':
        neighbors.append((pos[0], pos[1] - 1))
    if pos[1] + 1 < len(map[0]) and map[pos[0]][pos[1] + 1] != '#':
        neighbors.append((pos[0], pos[1] + 1))
    
    return neighbors

def find_path():
    visited = []
    queue = [(start, 0)]
    paths = [[(start)]]
    min_steps = float('inf')
    while len(queue) > 0:
        visiting = queue.pop(0)
        pos = visiting[0]
        steps = visiting[1]
        curr_path = paths.pop(0)

        if pos == end:
            if(steps < min_steps):
                min_steps = steps
                min_path = curr_path

        if pos not in visited:
            for neighbor in find_neighbors(pos):
                new_path = curr_path.copy()
                new_path.append(neighbor)
                paths.append(new_path)

                queue.append((neighbor, steps + 1))
            visited.append(pos)
    return min_path

with open("input/dec20.txt", "r") as file:
    row = 0 
    while line := file.readline():
        data = list(line.strip())
        if 'E' in data:
            end = (row, data.index('E'))
        if 'S' in data:
            start = (row, data.index('S'))
        map.append(data)
        row += 1

cheats = find_cheats(find_path(), 'v1')

v1 = 0
for cheat in cheats:
    if cheats[cheat] >= 100:
        v1 += 1
print(v1)

cheats = find_cheats(find_path(), 'v2')

v2 = 0
for cheat in cheats:
    if cheats[cheat] >= 100:
            v2 += 1
print(v2)
