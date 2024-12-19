
cache = {}

def can_form(pattern, bases):
    if len(pattern) == 0:
        return 1
    if pattern in cache:
        return cache[pattern]
    
    is_possible = 0
    for base in bases:
        if(pattern.startswith(base)):
            is_possible += can_form(pattern[len(base):], bases)
        if(is_possible > 0):
            cache[pattern] = is_possible
            
    return is_possible

with open("input/dec19.txt", "r") as file:
    bases = list(file.readline().strip().split(", "))
    file.readline()
    v1 = 0
    patterns = []
    while pattern := file.readline():
        patterns.append(pattern.strip())
    
    for pattern in patterns:
        if can_form(pattern, bases) > 0:
            v1 += 1

    v2 = 0
    for pattern in patterns:
        # print(can_form(pattern, bases))
        v2 += can_form(pattern, bases)
    #    print(count_forms(pattern, subbases))

    print(v1)
    print(v2)