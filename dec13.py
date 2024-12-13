import numpy as np
import re

with open("input/dec13.txt", "r") as file:
    total_presses = 0
    total_presses_v2 = 0

    while line := file.readline():
        if(line.strip() == ""):
            continue
        col1= list(map(int, re.findall(r'\d+', line)))
        col2 = list(map(int, re.findall(r'\d+', file.readline())))
        a = np.transpose(np.matrix([col1, col2]))
        col3 = list(map(int, re.findall(r'\d+', file.readline())))
        b = np.array(col3)
        presses = np.round(np.linalg.solve(a,b), decimals=3)
        if(presses[0].is_integer() and presses[1].is_integer() and presses[0] <= 100 and presses[1] <=100):
            total_presses += (presses[0] * 3) + presses[1]
        b_v2 = np.array([col3[0] + 10000000000000, col3[1] + 10000000000000])
        presses_v2 = np.round(np.linalg.solve(a,b_v2), decimals=3)
        if(presses_v2[0].is_integer() and presses_v2[1].is_integer()):
            total_presses_v2 += (presses_v2[0] * 3) + presses_v2[1]
    print(total_presses)
    print(total_presses_v2)