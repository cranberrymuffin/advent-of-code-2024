import re

num_to_pos = {'7': (0, 0), '8': (0, 1), '9': (0, 2),
              '4': (1, 0), '5': (1, 1), '6': (1, 2),
              '1': (2, 0), '2': (2, 1), '3': (2, 2), 
              '0': (3, 1), 'A': (3, 2)}

dir_to_pos = {'^': (0, 1), 'A': (0, 2), '<': (1, 0), 'v': (1, 1), '>': (1, 2)}

def vertical_first(currPos, finalPos, invalidPos):
    moves = (finalPos[0] - currPos[0], finalPos[1] - currPos[1])
    path = ''
    for i in range(abs(moves[0])):
        if moves[0] > 0:
            path = ''.join([path, 'v'])
            currPos = (currPos[0] + 1, currPos[1])
        elif moves[0] < 0:
            path = ''.join([path, '^'])
            currPos = (currPos[0] - 1, currPos[1])
        if currPos == invalidPos:
            return None
    for i in range(abs(moves[1])):
        if moves[1] > 0:
            path = ''.join([path, '>'])
            currPos = (currPos[0], currPos[1] + 1)
        elif moves[1] < 0:
            path = ''.join([path, '<'])
            currPos = (currPos[0], currPos[1] - 1)
        if currPos == invalidPos:
            return None
    path = ''.join([path, 'A'])
    return path

def horizontal_first(currPos, finalPos, invalidPos):
    moves = (finalPos[0] - currPos[0], finalPos[1] - currPos[1])
    path = ''
    for i in range(abs(moves[1])):
        if moves[1] > 0:
            path = ''.join([path, '>'])
            currPos = (currPos[0], currPos[1] + 1)
        elif moves[1] < 0:
            path = ''.join([path, '<'])
            currPos = (currPos[0], currPos[1] - 1)
        if currPos == invalidPos:
            return None
    for i in range(abs(moves[0])):
        if moves[0] > 0:
            path = ''.join([path, 'v'])
            currPos = (currPos[0] + 1, currPos[1])
        elif moves[0] < 0:
            path = ''.join([path, '^'])
            currPos = (currPos[0] - 1, currPos[1])
        if currPos == invalidPos:
            return None
    path = ''.join([path, 'A'])
    return path

verticalPaths = dict()
horizontalPaths = dict()

def find_path_recursive(currPos, finalPos, invalidPos, horizontalPath = '', verticalPath = '', level = 0):
    if (currPos, finalPos, invalidPos) not in verticalPaths:
        verticalPaths[(currPos, finalPos, invalidPos)] = vertical_first(currPos, finalPos, invalidPos)
    if (currPos, finalPos, invalidPos) not in horizontalPaths:
        horizontalPaths[(currPos, finalPos, invalidPos)] = horizontal_first(currPos, finalPos, invalidPos)
    verticalPath = verticalPaths[(currPos, finalPos, invalidPos)]
    horizontalPath = horizontalPaths[(currPos, finalPos, invalidPos)]

    if level == 25:
        if horizontalPath is None:
            return len(verticalPath)
        elif verticalPath is None:
            return len(horizontalPath)
        elif len(horizontalPath) < len(verticalPath):
            return len(horizontalPath)
        else:
            return len(verticalPath)
    
    if horizontalPath is not None:
        horizontalPath = robot2(horizontalPath, level + 1)
    if verticalPath is not None: 
        verticalPath = robot2(verticalPath, level + 1)

    return min(horizontalPath, verticalPath, key = lambda x: x if x is not None else float('inf'))

seen = dict()
seen2 = dict()
def robot2(code, level):
    if (code, level) not in seen2: 
        result = 0
        
        start_pos = dir_to_pos['A']
        for key in code:
            if (start_pos, dir_to_pos[key], level) not in seen:
                seen[(start_pos, dir_to_pos[key], level)] = find_path_recursive(start_pos, dir_to_pos[key], (0, 0), level = level)
            result += seen[(start_pos, dir_to_pos[key], level)]
            start_pos = dir_to_pos[key]
        seen2[(code, level)] = result
    return seen2[(code, level)]

def robot1(code):
    res = 0
    start_pos = num_to_pos['A']
    for key in code:
        res += find_path_recursive(start_pos, num_to_pos[key], (3, 0), level = 0)
        start_pos = num_to_pos[key]
    return res

def find_sequence(code):
   return robot1(code.strip())
    
def find_number(code):
    return int(re.findall('\d+', code)[0])

with open("input/dec21.txt", "r") as file:
    sum = 0 
    while code := file.readline():
        answer = find_sequence(code)
        print(answer, "*", find_number(code))
        sum += answer * find_number(code)
        
    print(sum)