import re
import sys

cols = 101
rows = 103

def find_quadrant(col, row):
    middle_col = int(cols/2)
    middle_row = int(rows/2)
    if(col < middle_col and row < middle_row):
        return 1
    elif(col > middle_col and row < middle_row):
        return 2
    elif(col < middle_col and row > middle_row):
        return 3
    elif(col > middle_col and row > middle_row):
        return 4
    else:
        return -1

with open("input/dec14.txt", "r") as file:
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    positions = []
    velocities = []
    while line := file.readline():
        nums = list(map(int, re.findall(r'-?\d+', line)))
        col_pos = nums[0]
        row_pos = nums[1]
        col_vel = nums[2]
        row_vel = nums[3]
        positions.append((col_pos, row_pos))
        velocities.append((col_vel, row_vel))

    for i in range(len(positions)):
        pos = positions[i]
        vel = velocities[i]

        future_col_pos = pos[0] + vel[0] * 100
        future_col_pos = future_col_pos % cols

        future_row_pos = pos[1] + vel[1] * 100
        future_row_pos = future_row_pos % rows

        quadrant = find_quadrant(future_col_pos, future_row_pos)

        match quadrant:
            case 1:
                q1 += 1
            case 2:
                q2 += 1
            case 3:
                q3 += 1
            case 4:
                q4 += 1
            case _:
                continue

    print(q1 * q2 * q3 * q4)

    min_entropy = sys.maxsize
    min_entropy_time = 0

    for seconds in range(cols * rows):
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        points = []
        for i in range(len(positions)):
            pos = positions[i]
            vel = velocities[i]
            
            future_col_pos = pos[0] + vel[0] * seconds
            future_col_pos = future_col_pos % cols

            future_row_pos = pos[1] + vel[1] * seconds
            future_row_pos = future_row_pos % rows

            quadrant = find_quadrant(future_col_pos, future_row_pos)

            match quadrant:
                case 1:
                    q1 += 1
                case 2:
                    q2 += 1
                case 3:
                    q3 += 1
                case 4:
                    q4 += 1
                case _:
                    continue
        
        entropy = q1 * q2 * q3 * q4
        if(entropy < min_entropy):
            min_entropy = entropy
            min_entropy_time = seconds

    print(min_entropy_time)
