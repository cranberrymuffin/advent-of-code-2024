from enum import Enum

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

map = []
NO_PATH = float('inf')

def can_move(map, pos):
    match pos[2]:
        case Direction.NORTH:
            return pos[0] -1 >= 0 and map[pos[0] - 1][pos[1]] != '#'
        case Direction.SOUTH:
            return pos[0] + 1 < len(map) and map[pos[0] + 1][pos[1]] != '#'
        case Direction.EAST:
            return pos[1] + 1 < len(map[0]) and map[pos[0]][pos[1] + 1] != '#'
        case Direction.WEST:
            return pos[1] -1 >= 0 and map[pos[0]][pos[1] - 1] != '#'

def find_min_path(map, pos, known_distance = None):
    visited = {}
    queue = [(pos, 0)]
    min_dist = float('inf')
    paths = [[(pos[0], pos[1])]]
    tiles = set()
    while len(queue) > 0:

        visiting = queue.pop(0)
        curr_path = paths.pop(0)

        pos = visiting[0]
        distance = visiting[1]

        if(map[pos[0]][pos[1]] == 'E'):
            if(distance <= min_dist):
                min_dist = distance
            if(distance == known_distance):
                tiles.update(curr_path)

        elif pos not in visited or distance <= visited[pos]:
            match pos[2]:
                case Direction.NORTH:
                    if can_move(map, pos):
                        next = (pos[0] - 1, pos[1], pos[2])
                        queue.append((next, distance + 1))
                        new_path = curr_path.copy()
                        new_path.append((next[0], next[1]))
                        paths.append(new_path)
                    queue.append(((pos[0], pos[1], Direction.EAST), distance + 1000))
                    paths.append(curr_path.copy())
                    queue.append(((pos[0], pos[1], Direction.WEST), distance + 1000))
                    paths.append(curr_path.copy())
                case Direction.SOUTH:
                    if can_move(map, pos):
                        next = (pos[0] + 1, pos[1], pos[2])
                        queue.append((next, distance + 1))
                        new_path = curr_path.copy()
                        new_path.append((next[0], next[1]))
                        paths.append(new_path)
                    queue.append(((pos[0], pos[1], Direction.EAST), distance + 1000))   
                    paths.append(curr_path.copy())
                    queue.append(((pos[0], pos[1], Direction.WEST), distance + 1000))  
                    paths.append(curr_path.copy())  
                case Direction.EAST:
                    if can_move(map, pos):
                        next = (pos[0], pos[1] + 1, pos[2])
                        queue.append((next, distance + 1))
                        new_path = curr_path.copy()
                        new_path.append((next[0], next[1]))
                        paths.append(new_path)
                    queue.append(((pos[0], pos[1], Direction.NORTH), distance + 1000))    
                    paths.append(curr_path.copy())   
                    queue.append(((pos[0], pos[1], Direction.SOUTH), distance + 1000))
                    paths.append(curr_path.copy())      
                case Direction.WEST:
                    if can_move(map, pos):
                        next = (pos[0], pos[1] - 1, pos[2])
                        queue.append((next, distance + 1))
                        new_path = curr_path.copy()
                        new_path.append((next[0], next[1]))
                        paths.append(new_path)
                    queue.append(((pos[0], pos[1], Direction.NORTH), distance + 1000)) 
                    paths.append(curr_path.copy())   
                    queue.append(((pos[0], pos[1], Direction.SOUTH), distance + 1000))       
                    paths.append(curr_path.copy())   

            visited[pos] = distance
    return (min_dist, len(tiles))


with open("input/dec16.txt", "r") as file:
    row = 0
    start_row = 0
    start_col = 0
    while line := file.readline():
        data = list(line.strip())
        if 'S' in data:
            start_row = row
            start_col = data.index('S')
        map.append(list(line.strip()))
        row += 1
    print(find_min_path(map, (start_row, start_col, Direction.EAST), find_min_path(map, (start_row, start_col, Direction.EAST))[0]))