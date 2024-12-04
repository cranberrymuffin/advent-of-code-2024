def is_xmas_v2(crossword, row, col):
    if(row-1 < 0 or col-1 < 0 or row+1 >= len(crossword) or col+1 >= len(crossword[0])):
        return False
    if(crossword[row][col] !='A'):
        return False
    
    a = crossword[row-1][col-1]
    b = crossword[row-1][col+1]
    c = crossword[row+1][col-1]
    d = crossword[row+1][col+1]

    if(a==b and c==d and a != c and (a=='M'and c =='S' or a=='S' and c=='M') ):
        return True
    if(a==c and b==d and a != b and (a=='M'and b =='S' or a=='S' and b=='M') ):
        return True

    return False

def is_xmas_row_fwd(crossword, row, col):
    xmas = 'XMAS'
    for i, letter in enumerate(xmas):
        if row + i >= len(crossword):
            return False
        if crossword[row + i][col] != letter:
            return False
    return True

def is_xmas_col_fwd(crossword, row, col):
    xmas = 'XMAS'
    for i, letter in enumerate(xmas):
        if col + i >= len(crossword[0]):
            return False
        if crossword[row][col+i] != letter:
            return False
    return True

def is_xmas_diag_fwd(crossword, row, col):
    xmas = 'XMAS'
    for i, letter in enumerate(xmas):
        if col + i >= len(crossword[0]) or row + i >= len(crossword):
            return False
        if crossword[row+i][col+i] != letter:
            return False
    return True

def is_xmas_diag_2_fwd(crossword, row, col):
    xmas = 'XMAS'
    for i, letter in enumerate(xmas):
        if col + i >= len(crossword[0]) or row - i <0:
            return False
        if crossword[row-i][col+i] != letter:
            return False
    return True

def is_xmas_diag_2_back(crossword, row, col):
    xmas = 'SAMX'
    for i, letter in enumerate(xmas):
        if col + i >= len(crossword[0]) or row - i <0:
            return False
        if crossword[row-i][col+i] != letter:
            return False
    return True

def is_xmas_row_back(crossword, row, col):
    xmas = 'SAMX'
    for i, letter in enumerate(xmas):
        if row + i >= len(crossword):
            return False
        if crossword[row + i][col] != letter:
            return False
    return True

def is_xmas_col_back(crossword, row, col):
    xmas = 'SAMX'
    for i, letter in enumerate(xmas):
        if col + i >= len(crossword[0]):
            return False
        if crossword[row][col+i] != letter:
            return False
    return True

def is_xmas_diag_back(crossword, row, col):
    xmas = 'SAMX'
    for i, letter in enumerate(xmas):
        if col + i >= len(crossword[0]) or row + i >= len(crossword):
            return False
        if crossword[row+i][col+i] != letter:
            return False
    return True
    

crossword = []
with open("input/dec4.txt", "r") as file:
    while line := file.readline():
        crossword.append(list(line.strip()))

num_xmas = 0
num_xmas_v2 = 0
for row_idx, row in enumerate(crossword):
    for col_idx, letter in enumerate(row):
        if is_xmas_row_fwd(crossword, row_idx, col_idx):
            num_xmas+=1
        if is_xmas_col_fwd(crossword, row_idx, col_idx):
            num_xmas+=1
        if is_xmas_diag_fwd(crossword, row_idx, col_idx):
            num_xmas+=1
        if is_xmas_diag_2_fwd(crossword, row_idx, col_idx):
            num_xmas+=1
        if is_xmas_row_back(crossword, row_idx, col_idx):
            num_xmas+=1
        if is_xmas_col_back(crossword, row_idx, col_idx):
            num_xmas+=1
        if is_xmas_diag_back(crossword, row_idx, col_idx):
            num_xmas+=1
        if is_xmas_diag_2_back(crossword, row_idx, col_idx):
            num_xmas+=1
        if is_xmas_v2(crossword, row_idx, col_idx):
            num_xmas_v2 +=1

print(num_xmas)
print(num_xmas_v2)