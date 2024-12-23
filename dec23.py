max = 0
max_set = set()

def BronKerbosch1(R, P, X, neighbor_set):
    global max
    global max_set
    if len(P) == 0 and len(X) == 0:
        if(len(R) > max):
            max_set = R
            max = len(max_set)

    list_P = list(P)
    while(len(list_P) > 0):
        v = list_P.pop()
        BronKerbosch1(R.union({v}), set(list_P).intersection(neighbor_set[v]), X.intersection(neighbor_set[v]), neighbor_set)
        X = X.intersection({v})

connections = {}

with open("input/dec23.txt", "r") as file:
    vertex_set = set()
    while line := file.readline():
        connection = line.strip().split("-")
        if connection[0] not in connections:
            connections[connection[0]] = set()
        if connection[1] not in connections:
            connections[connection[1]] = set()
        vertex_set.add(connection[0])
        vertex_set.add(connection[1])
        connections[connection[0]].add(connection[1])
        connections[connection[1]].add(connection[0])

    set_of_three = set()
    for connection1 in connections:
        pairs = connections[connection1]
        for connection2 in pairs:
            for connection3 in pairs:
                if (connection2 != connection3) and connection3 in connections[connection2]:
                    result = [connection1, connection2, connection3]
                    result.sort()
                    set_of_three.add((result[0], result[1], result[2]))
    v1 = 0
    for result in set_of_three:
        if len(list(filter(lambda item: item.startswith('t'), result))) > 0:
            v1 += 1
    print(v1)

    BronKerbosch1(set(), vertex_set, set(), connections)
    password = list(max_set)
    password.sort()
    print(",".join(password))