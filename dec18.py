
puzzle_size = 70
fallen = 1024
map = [['.' for i in range(puzzle_size + 1)] for j in range(puzzle_size + 1)]

def find_neighbors(pos):
    neighbors = []
    if pos[0] - 1 >= 0 and map[pos[0] - 1][pos[1]] == '.':
        neighbors.append((pos[0] - 1, pos[1]))
    if pos[0] + 1 < len(map) and map[pos[0] + 1][pos[1]] == '.':
        neighbors.append((pos[0] + 1, pos[1]))
    if pos[1] - 1 >= 0 and map[pos[0]][pos[1] - 1] == '.':
        neighbors.append((pos[0], pos[1] - 1))
    if pos[1] + 1 < len(map[0]) and map[pos[0]][pos[1] + 1] == '.':
        neighbors.append((pos[0], pos[1] + 1))
    
    return neighbors

def find_path():
    visited = []
    queue = [((0,0), 0)]
    paths = [[(0, 0)]]
    min_steps = float('inf')
    while len(queue) > 0:
        visiting = queue.pop(0)
        pos = visiting[0]
        steps = visiting[1]
        curr_path = paths.pop(0)

        if pos == (puzzle_size,puzzle_size):
            if(steps < min_steps):
                min_steps = steps

        if pos not in visited:
            for neighbor in find_neighbors(pos):
                new_path = curr_path.copy()
                queue.append((neighbor, steps + 1))
                new_path.append(neighbor)
                paths.append(new_path)
            visited.append(pos)
    return min_steps

def print_map():
    for row in map:
        print(''.join(row))

with open("input/dec18.txt", "r") as file:
    i = 0
    while line := file.readline():
        if(i == fallen):
            print(find_path())
        if(i > fallen and find_path() == float('inf')):
            print(",".join(pos))
            break
        pos = line.strip().split(",")

        map[int(pos[1])][int(pos[0])] = '#'
        i += 1
