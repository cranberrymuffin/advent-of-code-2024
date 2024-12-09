disk_map = []
data = []
EMPTY = '.'

def find_space(data, size, end):
    found_space = 0
    start = 0
    started = False
    for i in range(end):
        if(data[i] != '.'):
            found_space = 0
            started = False
        else:
            if not started:
                start = i
                started = True
            found_space += 1
            if(found_space >= size):
                return start
            
    return -1


with open("input/dec9.txt", "r") as file:
    disk_map = list(map(lambda x: int(x), list(file.readline().strip())))
    id = 0
    for id in range(0,len(disk_map), 2):
        curr_size = disk_map[id]
        if(id + 1 < len(disk_map)):
            curr_space = disk_map[id + 1]
        for j in range(curr_size):
            data.append(int(id/2))
        if(id + 1 < len(disk_map)):
            for k in range(curr_space):
                data.append(EMPTY)

    data_v1 = data.copy()

    i = 0
    while data[i] != '.':
        i+=1
    j = len(data) - 1

    while (i < j):
        data_v1[i] = data_v1[j]
        data_v1[j] = '.'
        i+=1
        j-=1
        while data_v1[i] != '.':
            i+=1
        while data_v1[j] == '.':
            j-=1
    data_v1 = data_v1[:j + 1]


    checksum_v1 = 0
    for pos, val in enumerate(data_v1):
        checksum_v1 += val * pos

    print(checksum_v1)
    data_v2 = data.copy()

    j=len(disk_map) - 1

    while(j >= 0):
        idx = sum(disk_map[0:j])
        to_move = disk_map[j]
        next = find_space(data_v2, to_move, idx)
        if next >= 0:
            for k in range(to_move):
                data_v2[next + k] = data_v2[idx]
                data_v2[idx] = '.'
                idx +=1 
        j-=2    

    checksum_v2 = 0
    for pos, val in enumerate(data_v2):
        if(val == '.'):
            continue
        checksum_v2 += val * pos
    print(checksum_v2)

