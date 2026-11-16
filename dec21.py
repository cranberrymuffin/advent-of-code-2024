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
            path += 'v'
            currPos = (currPos[0] + 1, currPos[1])
        elif moves[0] < 0:
            path += '^'
            currPos = (currPos[0] - 1, currPos[1])
        if currPos == invalidPos:
            return None
    for i in range(abs(moves[1])):
        if moves[1] > 0:
            path += '>'
            currPos = (currPos[0], currPos[1] + 1)
        elif moves[1] < 0:
            path += '<'
            currPos = (currPos[0], currPos[1] - 1)
        if currPos == invalidPos:
            return None
    path += 'A'
    return path

def horizontal_first(currPos, finalPos, invalidPos):
    moves = (finalPos[0] - currPos[0], finalPos[1] - currPos[1])
    path = ''
    for i in range(abs(moves[1])):
        if moves[1] > 0:
            path += '>'
            currPos = (currPos[0], currPos[1] + 1)
        elif moves[1] < 0:
            path += '<'
            currPos = (currPos[0], currPos[1] - 1)
        if currPos == invalidPos:
            return None
    for i in range(abs(moves[0])):
        if moves[0] > 0:
            path += 'v'
            currPos = (currPos[0] + 1, currPos[1])
        elif moves[0] < 0:
            path += '^'
            currPos = (currPos[0] - 1, currPos[1])
        if currPos == invalidPos:
            return None
    path += 'A'
    return path

def find_path(currPos, finalPos, invalidPos, level = 0):
    verticalFirst = vertical_first(currPos, finalPos, invalidPos)
    horizontalFirst = horizontal_first(currPos, finalPos, invalidPos)
    if verticalFirst is None:
        return horizontalFirst
    elif horizontalFirst is None:
        return verticalFirst
    elif len(verticalFirst) < len(horizontalFirst):
        return verticalFirst
    elif level < 2:
        robot2HorizontalFirst = robot2(horizontalFirst, level + 1)
        robot2VerticalFirst = robot2(verticalFirst, level + 1)
        if robot2HorizontalFirst is None:
            return verticalFirst
        elif robot2VerticalFirst is None:
            return horizontalFirst
        elif len(robot2HorizontalFirst) < len(robot2VerticalFirst):
            return horizontalFirst
        else:
            robot2HorizontalFirst = robot2(robot2HorizontalFirst, level + 1)
            robot2VerticalFirst = robot2(robot2VerticalFirst, level + 1)
            if robot2HorizontalFirst is None:
                return verticalFirst
            elif robot2VerticalFirst is None:
                return horizontalFirst
            elif len(robot2HorizontalFirst) < len(robot2VerticalFirst):
                return horizontalFirst
            else:
                return verticalFirst
    else:
        return verticalFirst

    

def robot2(code, level):
    res = ''
    start_pos = dir_to_pos['A']
    for key in code:
        res+= find_path(start_pos, dir_to_pos[key], (0, 0), level)
        start_pos = dir_to_pos[key]
    return res

def robot1(code):
    res = ''
    start_pos = num_to_pos['A']
    for key in code:
        res += find_path(start_pos, num_to_pos[key], (3, 0), 0)
        start_pos = num_to_pos[key]
    return res

def find_sequence(code):
   return robot2(robot2(robot1(code.strip()), 1), 2)
    
def find_number(code):
    return int(re.findall('\d+', code)[0])

with open("input/dec21.txt", "r") as file:
    sum = 0 
    while code := file.readline():
        print(len(find_sequence(code)), "*", find_number(code))
        sum += len(find_sequence(code)) * find_number(code)
        
    print(sum)