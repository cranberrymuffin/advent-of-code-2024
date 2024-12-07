def is_possible_v1(ans, vars):
    if(len(vars) == 1):
        return ans == vars[0]
    concat = int(str(vars[0]) + str(vars[1]))
    return is_possible_v1(ans, list([vars[0] + vars[1]]) + vars[2:]) or is_possible_v1(ans, list([vars[0] * vars[1]]) + vars[2:])


def is_possible_v2(ans, vars):
    if(len(vars) == 1):
        return ans == vars[0]
    concat = int(str(vars[0]) + str(vars[1]))
    return is_possible_v2(ans, list([vars[0] + vars[1]]) + vars[2:]) or is_possible_v2(ans, list([vars[0] * vars[1]]) + vars[2:]) or is_possible_v2(ans, list([concat]) + vars[2:])

with open("input/dec7.txt", "r") as file:
    result_v1 = 0
    result_v2 = 0
    while line := file.readline():
        eq = line.strip().split(":")
        ans = int(eq[0])
        vars = list(map(lambda x: int(x), eq[1].strip().split(" ")))
        if is_possible_v1(ans, vars):
            result_v1 += ans
        if is_possible_v2(ans, vars):
            result_v2 += ans

print(result_v1)
print(result_v2)