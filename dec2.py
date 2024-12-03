def is_safe(row):
    increasing = row[0] < row[1]
    for i in range(1, len(row)):
        prev = row[i-1]
        curr = row[i]
        if not is_valid(prev, curr, increasing): 
            return False
    return True

def is_valid(prev, curr, increasing):
    if increasing and prev > curr:
        return False
    if not increasing and prev < curr:
        return False
    diff = abs(prev-curr)
    if diff < 1 or diff > 3:
        return False
    return True

inputs = []
with open("input/dec2.txt", "r") as file:
    while line := file.readline():
        data = line.split()
        data = list(map(lambda x: int(x), data))
        inputs.append(data)

num_safe = 0
num_safe_v2 = 0

for row in inputs:    
    safe = is_safe(row)
    if(safe):
        num_safe+=1   
        num_safe_v2 +=1 
    else:
        for i in range(len(row)):
            tolerant_row = row[:i] + row[i+1 :]
            if is_safe(tolerant_row):
                num_safe_v2 +=1
                break

print(num_safe)
print(num_safe_v2)
