import re
map = []

def find_num_antinodes(a, b, rows, cols):
    delta_x = abs(a[0] - b[0])
    low_x =  min(a[0], b[0])
    start_x = low_x - delta_x

    end_x = start_x + (4 * delta_x)
    m = (b[1] - a[1])/(b[0] - a[0])
    y_intercept = a[1] - (m * a[0])
    vals = set()
    for x in range(start_x, end_x, delta_x):
        y = m * x + y_intercept
        if(x >=0 and y >=0  and x<cols and y<rows and x != a[0] and x!= b[0]):
            vals.add((x, round(y)))
    return vals

def find_num_antinodes_v2(a, b, rows, cols, antenna):
    delta_x = abs(a[0] - b[0])
    low_x =  min(a[0], b[0])
    start_x = low_x
    while(start_x - delta_x >= 0):
        start_x = start_x - delta_x

    m = (b[1] - a[1])/(b[0] - a[0])
    y_intercept = a[1] - (m * a[0])
    vals = set()
    for x in range(start_x, cols, delta_x):
        y = round(m * x + y_intercept)
        if(x >=0 and y >=0  and x<cols and y<rows):
            vals.add((x, y))
    return vals



with open("input/dec8.txt", "r") as file:
    antennas = {}
    p = re.compile("[a-z]|[A-Z]|[0-9]")
    rows = 0
    cols = 0
    while line := file.readline():
        data = line.strip()
        map.append(list(data))

        cols = len(data)
        for m in p.finditer(data):
            antenna = m.group()
            col = m.start()
            if not antenna in antennas:
                antennas[antenna] = set()
            antennas[antenna].add((col, rows))
        rows += 1
    result = set()
    result_v2 = set()
    for antenna in antennas:
        spots = list(antennas[antenna])
        combos = set()
        for a in range(len(spots)):
            for b in range(a+1, len(spots)):

                combos.add((spots[a],spots[b]))

        for combo in combos:
            result = result.union(find_num_antinodes(combo[0], combo[1], rows, cols))
            result_v2 = result_v2.union(find_num_antinodes_v2(combo[0], combo[1], rows, cols, antenna))
    print(len(result))
    print(len(result_v2))