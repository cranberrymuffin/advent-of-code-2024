map = []

def is_valid(row, col, seen):
    if(row<0 or col<0):
        return False
    if(row >= len(map) or col >= len(map[0])):
        return False
    return (row, col) not in seen

def find_score(row, col, seen):
    if(map[row][col] == 9):
        return {(row, col)}
    
    seen.add((row, col))

    score = set()
    if(is_valid(row + 1, col, seen) and map[row + 1][col]- map[row][col] == 1):
        score = score.union(find_score(row + 1, col, seen))
    if(is_valid(row - 1, col, seen) and map[row - 1][col]- map[row][col] == 1):
        score = score.union(find_score(row - 1, col, seen))
    if(is_valid(row, col + 1, seen) and map[row][col + 1]- map[row][col] == 1):
        score = score.union(find_score(row, col + 1, seen))
    if(is_valid(row, col - 1, seen) and map[row][col - 1]- map[row][col] == 1):
        score = score.union(find_score(row, col - 1, seen))

    return score

def find_rating(row, col, seen):
    if(map[row][col] == 9):
        return 1
    
    rating = 0
    if(is_valid(row + 1, col, seen) and map[row + 1][col] - map[row][col] == 1):
        rating += find_rating(row + 1, col, seen)
    if(is_valid(row - 1, col, seen) and map[row - 1][col] - map[row][col] == 1):
        rating += find_rating(row - 1, col, seen)
    if(is_valid(row, col + 1, seen) and map[row][col + 1] - map[row][col] == 1):
        rating += find_rating(row, col + 1, seen)
    if(is_valid(row, col - 1, seen) and map[row][col - 1] - map[row][col] == 1):
        rating += find_rating(row, col - 1, seen)

    return rating


with open("input/dec10.txt", "r") as file:
    start_pos = []
    while line := file.readline():
        data = list(line.strip())
        data = [int(x) for x in data]
        map.append(data)
        
score = 0
rating = 0
for row, row_data in enumerate(map):
    for col, data in enumerate(row_data):
        if(data == 0):
            found = find_score(row, col, set())
            score += len(found)
            rating += find_rating(row, col, set())

print(score)
print(rating)