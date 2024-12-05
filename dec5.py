def is_valid_before(befores, tocheck):
    return befores.issuperset(set(tocheck))

def is_valid_after(afters, tocheck):
    return afters.issuperset(set(tocheck))

def find_middle_element(elements, befores, afters):
    for element in elements:
        before = befores.get(element) or set()
        after = afters.get(element) or set()

        if len(before.intersection(set(elements))) == len(after.intersection(set(elements))):
            return element
    print("error!")
    return 0

with open("input/dec5.txt", "r") as file:
    rules = []
    validate = []
    while line := file.readline():
        if "|" in line:
            rules.append(line.strip().split("|"))
        elif line.strip() != "":
            validate.append(line.strip().split(","))
    
    before = {}
    after = {}

    for rule in rules:
        smaller = rule[0]
        larger = rule[1]
        if larger not in before:
            before[larger] = set()
        if smaller not in after:
            after[smaller] = set()

        before[larger].add(smaller)
        after[smaller].add(larger)
    
    sum1 = 0
    sum2 = 0

    for to_validate in validate:
        add = True
        middle_idx = int(len(to_validate)/2)
        middle_element = to_validate[middle_idx]
        for idx, element in enumerate(to_validate):
            check_before = to_validate[:idx]
            check_after = to_validate[idx+1:]
            if not is_valid_before(before.get(element) or set(), check_before) or not is_valid_after(after.get(element) or set(), check_after):
                add = False
                break
        if add:
            sum1 += int(middle_element)
        else:
            if(is_valid_before(before.get(middle_element) or set(), to_validate[:middle_idx]) and is_valid_after(after.get(middle_element) or set(), to_validate[middle_idx+1:])):
                sum2 += int(middle_element)
            else:
                sum2 += int(find_middle_element(to_validate, before, after))
        
    print(sum1)
    print(sum2)
        


