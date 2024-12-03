import re

def multiply(a, b):
    return a * b

total = 0
total2 = 0
with open("input/dec3.txt", "r") as file:
    while line := file.readline():
        matches = re.findall('mul\\([0-9]+,[0-9]+\\)', line)
        mul_operations = list(map(lambda x: re.findall('[0-9]+', x), matches))
        results = list(map(lambda x: multiply(int(x[0]), int(x[1])), mul_operations))
        total+= sum(results)
print(total)

with open("input/dec3.txt", "r") as file:
    on = True
    while line := file.readline():
        matches2=re.findall('mul\\([0-9]+,[0-9]+\\)|do\\(\\)|don\'t\\(\\)', line)
        mul_operations2 = list(map(lambda x: re.findall('[0-9]+', x) if x.startswith('mul') else x, matches2))
        for op in mul_operations2:
            if op == 'do()':
                print("on")
                on = True
            elif op == 'don\'t()':
                print("off")
                on = False
            elif on:
                print("adding")
                total2 += multiply(int(op[0]), int(op[1]))

print(total2)