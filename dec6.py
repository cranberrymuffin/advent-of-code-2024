from copy import deepcopy


start_x = 0
start_y = 0

curr_direction = 0

directions = [(-1, 0), (0,1), (1, 0), (0, -1)]
map = []


with open("input/dec6.txt", "r") as file:
    row = 0
    while line := file.readline():
        map.append(list(line.strip()))
        curr_row = map[len(map) - 1]
        if '^' in curr_row:
            col = curr_row.index('^')
            start_y = row
            start_x = col
        row += 1

def loop_found(start_direction, curr_map):
    seen = set()
    seen_pos = set()
    curr_y = start_y
    curr_x = start_x
    direction = directions[start_direction]
    curr_direction = start_direction
    while not (((curr_x, curr_y), (direction[0], direction[1])) in seen):
        seen.add(((curr_x, curr_y), (direction[0], direction[1])))

        seen_pos.add((curr_x, curr_y))
        next_y = curr_y + direction[0]
        next_x = curr_x + direction[1]

        if(next_y < 0 or next_x < 0 or next_y >= len(curr_map) or next_x >= len(curr_map[0])):
            return len(seen_pos)
        
        while(curr_map[next_y][next_x] == '#'):
            curr_direction = (curr_direction + 1) % 4
            direction = directions[curr_direction]
            next_y = curr_y + direction[0]
            next_x = curr_x + direction[1]

        curr_x = next_x
        curr_y = next_y

    return True




print(loop_found(curr_direction, map))

obstructions = set()

for row, data_row in enumerate(map):
    for col, data in enumerate(data_row):
        if data != '^' and data != '#':
           obstructions.add((row, col))

obstructions.remove((row - 1, col))

print(len(obstructions))

loop = 0
for obstruction in obstructions:
    new_map = deepcopy(map)
    new_map[obstruction[0]][obstruction[1]] = '#'
    if(loop_found(curr_direction, new_map) == True):
        loop += 1

print(loop)