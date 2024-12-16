from copy import deepcopy

def find_gps_sum(map):
    sum = 0
    for row, row_data in enumerate(map):
        for col, data in enumerate(row_data):
            if(data == 'O' or data =="["):
                sum += 100 * row + col
    
    return sum

def get_shift(move_type):
    row_shift = 0
    col_shift = 0
    if(move_type == "<"):
        col_shift = -1
    if(move_type == ">"):
        col_shift = 1
    if(move_type=="^"):
        row_shift = -1
    if(move_type=="v"):
        row_shift = 1
    return (row_shift, col_shift)

def move(map, move_type, pos):
    shift = get_shift(move_type)
    row_shift = shift[0]
    col_shift = shift[1]
    
    if(map[pos[0] + row_shift][pos[1] + col_shift] == "."):
        map[pos[0] + row_shift][pos[1] + col_shift] = map[pos[0]][pos[1]]
        map[pos[0]][pos[1]] = "."
    elif(map[pos[0] + row_shift][pos[1] + col_shift] == "O"):
        move(map, move_type, (pos[0] + row_shift, pos[1] + col_shift))
        if(map[pos[0] + row_shift][pos[1] + col_shift] != "O"):
            move(map, move_type, pos)
    return map

def can_move(map, move_type, pos):
    shift = get_shift(move_type)
    row_shift = shift[0]
    col_shift = shift[1]
    if(map[pos[0]][pos[1]] == "#"):
        return False
    if(map[pos[0]][pos[1]] == "."):
        return True
    elif(map[pos[0]][pos[1]] == "[" and row_shift != 0):
        return can_move(map, move_type, (pos[0] + row_shift, pos[1] + col_shift)) and can_move(map, move_type, (pos[0] + row_shift, pos[1] + col_shift + 1))
    elif(map[pos[0]][pos[1]] == "]" and row_shift != 0):
        return can_move(map, move_type, (pos[0] + row_shift, pos[1] + col_shift - 1)) and can_move(map, move_type, (pos[0] + row_shift, pos[1] + col_shift))
    elif(map[pos[0]][pos[1]] == "[" and col_shift != 0):
        return can_move(map, move_type, (pos[0] + row_shift, pos[1] + col_shift))
    elif(map[pos[0]][pos[1]] == "]" and col_shift != 0):
        return can_move(map, move_type, (pos[0] + row_shift, pos[1] + col_shift))

def move_v2(map, move_type, pos):
    shift = get_shift(move_type)
    row_shift = shift[0]
    col_shift = shift[1]
    
    if(map[pos[0] + row_shift][pos[1] + col_shift] == "."):
        map[pos[0] + row_shift][pos[1] + col_shift] = map[pos[0]][pos[1]]
        map[pos[0]][pos[1]] = "."
    elif(map[pos[0] + row_shift][pos[1] + col_shift] == "["):
        if can_move(map, move_type, (pos[0] + row_shift, pos[1] + col_shift)):
            move_v2(map, move_type, (pos[0] + row_shift, pos[1] + col_shift))
            if row_shift != 0:
                move_v2(map, move_type, (pos[0] + row_shift, pos[1] + col_shift + 1))
            if(map[pos[0] + row_shift][pos[1] + col_shift] == "."):
                move_v2(map, move_type, pos)
    elif(map[pos[0] + row_shift][pos[1] + col_shift] == "]"):
        if can_move(map, move_type, (pos[0] + row_shift, pos[1] + col_shift)):
            if row_shift != 0:
                move_v2(map, move_type, (pos[0] + row_shift, pos[1] + col_shift - 1))
                move_v2(map, move_type, (pos[0] + row_shift, pos[1] + col_shift))
            else: 
                move_v2(map, move_type, (pos[0] + row_shift, pos[1] + col_shift))
            if(map[pos[0] + row_shift][pos[1] + col_shift] == "."):
                move_v2(map, move_type, pos)
    return map

def print_map(map):
    for row in map:
        print(''.join(row))

def find_robot(map):
    for row, row_data in enumerate(map):
        for col, data in enumerate(row_data):
            if(data == "@"):
                return (row, col)
    return None

with open("input/dec15.txt", "r") as file:
    reading_map = True
    map = []
    map_v2 = []
    moves = ""
    while line := file.readline():
        line = line.strip()
        if line == "":
            reading_map = False
            continue
        if(reading_map):
            map.append(list(line))
            line = line.replace("#", "##")
            line = line.replace(".", "..")
            line = line.replace("O", "[]")
            line = line.replace("@", "@.")
            map_v2.append(list(line))
        else:
            moves += line

    for move_type in moves:
        map = move(map, move_type, find_robot(map))
    print(find_gps_sum(map))
    for move_type in moves:
        map_v2 = move_v2(map_v2, move_type, find_robot(map_v2))
    print(find_gps_sum(map_v2))
