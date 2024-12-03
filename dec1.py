import heapq

heap1=[]
heap2=[]

freq = {}
vals = []

with open("input/dec1.txt", "r") as file:
    while line := file.readline():
        data = line.split()
        heapq.heappush(heap1, int(data[0]))
        vals.append(int(data[0]))
        val = int(data[1])
        heapq.heappush(heap2, val)
        if(val in freq):
            freq[val] += 1
        else:
            freq[val] = 1

assert len(heap1) == len(heap2)

distance = 0

while heap1 and heap2:
    distance+= abs(heapq.heappop(heap1) - heapq.heappop(heap2))

print(distance)

similarity = 0

for item in vals:
    factor = 0
    if(item in freq):
        factor = freq[item]
    similarity+= (item * factor)

print(similarity)

