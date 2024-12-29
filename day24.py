import re

switches = {}

def compute(a):
    a = str(a)
    if a.isdigit():
        return int(a)

    vals = a.split(' ')
    print(vals)
    if len(vals) == 3:
        next_a = vals[0].strip()
        operator = vals[1].strip()
        next_b = vals[2].strip()
        if operator == 'AND':
            return int(compute(next_a)) and int(compute(next_b))
        if operator == 'OR':
            return int(compute(next_a)) or int(compute(next_b))
        if operator == 'XOR':
            return int(compute(next_a)) ^ int(compute(next_b))
    else:
        return compute(switches[vals[0]])
    
with open("input/dec24.txt", "r") as file:
    while line := file.readline():
        line = line.strip()
        if ':' in line:
            data = line.split(":")
            switches[data[0].strip()] = data[1].strip()
        elif '->' in line:
            data = line.split("->")
            switches[data[1].strip()] = data[0].strip()
    
    print(switches)

    for key in switches:
        a = switches[key]
        if 'AND' in a or 'OR' in a or 'XOR' in a:
            switches[key] = compute(switches[key])
    my_list = []
    for key in switches:
        if key.startswith('z'):
            index = int(re.search(r'\d+', key).group())
            while(len(my_list) <= index):
                my_list.append(0)
            my_list[index] = switches[key]
    
    my_list.reverse()
    print(int(''.join(str(x) for x in my_list), 2))
    
