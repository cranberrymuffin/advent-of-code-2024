from collections import defaultdict

def blink(data):
    stone_counter = defaultdict(int)
    for stone,frequency in data.items():
        if stone == '0':
            stone_counter['1'] += frequency
        elif len(stone) % 2 == 0:
            stone_counter[str(int(stone[0:int(len(stone)/2)]))] += frequency
            stone_counter[str(int(stone[int(len(stone)/2):]))] += frequency
        else:
            stone_counter[str(int(stone) * 2024)] += frequency
    return stone_counter

with open("input/dec11.txt", "r") as file:
    data = file.readline().strip().split(' ')

    stone_counter = defaultdict(int)

    for stone in data:
        stone_counter[stone] += 1

    for i in range(25):
        stone_counter = blink(stone_counter)

    total = 0
    for stone,frequency in stone_counter.items():
        total+= frequency

    print(total)
    
    stone_counter = defaultdict(int)

    for stone in data:
        stone_counter[stone] += 1

    for i in range(75):
        stone_counter = blink(stone_counter)

    total = 0
    for stone,frequency in stone_counter.items():
        total+= frequency

    print(total)