map = []
visited_area = []
visited_perimeter = []
visited_side = []

def visit_area(row, col, val):
    if(row < 0 or col < 0 or row >= len(map) or col >= len(map[0])):
        return 0
    if(map[row][col] == val and not visited_area[row][col]):
        visited_area[row][col] = True
        return 1 + visit_area(row + 1, col, val) + visit_area(row - 1, col, val) + visit_area(row, col+1, val) + visit_area(row, col -1, val)
    return 0

def find_border(row, col, val):
    border = 0
    if(row - 1 < 0 or map[row-1][col] != val):
        border += 1
    if(col - 1 < 0 or map[row][col-1] != val):
        border += 1
    if(row + 1 >= len(map) or map[row + 1][col] != val):
        border += 1
    if(col + 1 >= len(map) or map[row][col + 1] != val):
        border += 1
    return border

def visit_perimeter(row, col, val):
    if(row < 0 or col < 0 or row >= len(map) or col >= len(map[0])):
        return 0
    if(map[row][col] == val and not visited_perimeter[row][col]):
        visited_perimeter[row][col] = True
        return find_border(row, col, val) + visit_perimeter(row + 1, col, val) + visit_perimeter(row - 1, col, val) + visit_perimeter(row, col+1, val) + visit_perimeter(row, col -1, val)
    return 0

def is_valid(row, col, val):
    return row >=0 and col >= 0 and row < len(map) and col < len(map[0]) and map[row][col] == val

def find_corner(row, col, val):
    corners = 0
    if(not is_valid(row, col -1, val) and not is_valid(row - 1, col, val)):
        corners += 1
    if(not is_valid(row, col -1, val) and not is_valid(row + 1, col, val)):
        corners += 1
    if(not is_valid(row, col + 1, val) and not is_valid(row -1, col, val)):
        corners +=1
    if(not is_valid(row+1, col, val) and not is_valid(row, col+1, val)):
        corners +=1
    if(is_valid(row - 1, col, val) and is_valid(row, col + 1, val) and not is_valid(row -1, col + 1, val)):
        corners += 1
    if(is_valid(row - 1, col, val) and is_valid(row, col - 1, val) and not is_valid(row -1, col - 1, val)):
        corners += 1
    if(is_valid(row, col + 1, val) and is_valid(row + 1, col, val) and not is_valid(row + 1, col + 1, val)):
        corners += 1
    if(is_valid(row, col - 1, val) and is_valid(row + 1, col, val) and not is_valid(row + 1, col - 1, val)):
        corners += 1
    
    return corners

def visit_sides(row, col, val):
    if(row < 0 or col < 0 or row >= len(map) or col >= len(map[0])):
        return 0
    if(map[row][col] == val and not visited_side[row][col]):
        visited_side[row][col] = True
        return find_corner(row, col, val) + visit_sides(row + 1, col, val) + visit_sides(row - 1, col, val) + visit_sides(row, col+1, val) + visit_sides(row, col -1, val)
    return 0

with open("input/dec12.txt", "r") as file:
    while line := file.readline():
        map.append(list(line.strip()))
        visited_area.append([False] * len(map[0]))
        visited_perimeter.append([False] * len(map[0]))
        visited_side.append([False] * len(map[0]))

total = 0
total_v2 = 0
for row, data in enumerate(map):
    for col, val in enumerate(data):
        if(not visited_area[row][col]):
            area = visit_area(row, col, map[row][col])
            perimeter = visit_perimeter(row, col, map[row][col])
            sides = visit_sides(row, col, map[row][col])
            total += (area * perimeter)
            total_v2 += (area * sides)

print(total)
print(total_v2)