import re

a = 0
b = 0
c = 0
instructions = None
output = []

def combo(operand):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c

# 0
def adv(operand):
    global a
    a = a // pow(2, combo(operand))

# 1
def bxl(operand):
    global b
    b = b ^ operand
# 2
def bst(operand):
    global b
    b = combo(operand) % 8

# 4
def bxc():
    global b
    global c
    b = b ^ c

# 5
def out(operand):
    output.append(combo(operand) % 8)
# 6
def bdv(operand):
    global a
    global b
    b = a//pow(2, combo(operand))
# 7
def cdv(operand):
    global c
    c = a//pow(2, combo(operand))

def instruction(i):
    match instructions[i]:
        case 0:
            adv(instructions[i+1])
        case 1:
            bxl(instructions[i+1])
        case 2:
            bst(instructions[i+1])
        case 4:
            bxc()
        case 5:
            out(instructions[i+1])
        case 6:
            bdv(instructions[i+1])
        case 7:
            cdv(instructions[i+1])

def run(start_a, start_b, start_c):
    global a
    global b
    global c
    global instructions
    global output

    output.clear()
    a = start_a
    b = start_b
    c = start_c
    i = 0
    while i < len(instructions):
        if(instructions[i] != 3):
            instruction(i)
        if instructions[i] != 3 or a == 0:
            i += 2
        else:
            i = instructions[i+1]

    return output

def find_a(start_a, start_b, start_c):
    matches = [pow(8, len(instructions) - 1)]
    for i in range(len(instructions) - 1, -1, -1):
        start_a = pow(8, i)
        new_matches = []
        for m in matches:
            for j in range(8):
                res = run(m + start_a * j, start_b, start_c)
                if res[i] == instructions[i]:
                    new_matches.append(m + start_a * j)
        matches = new_matches
    return min(matches)

with open("input/dec17.txt", "r") as file:

    while line := file.readline():
        if "A" in line:
            start_a = int(re.search(r'\d+', line).group())
        elif "B" in line:
            start_b = int(re.search(r'\d+', line).group())
        elif "C" in line:
            start_c = int(re.search(r'\d+', line).group())
        elif "Program" in line:
            instructions = list(map(int, re.findall(r'\d+', line)))


    run(start_a, start_b, start_c)
    print(",".join(map(str, output)))
    
    print(find_a(start_a, start_b, start_c))