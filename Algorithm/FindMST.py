import numpy as np

def findMst():
    f = open('matrix.txt', 'r')
    arr = []
    for line in f:
        nums = [float(x) for x in line.strip().split(" ")]
        arr.append(nums)

    matrix = np.array(arr)
    M = len(matrix)

    # print('M=', M)

    # Prim's algorithm
    INF = 10.0e777

    k = 0

    used = np.full(M, False)
    min_e = np.full(M, INF)
    sel_e = np.full(M, -1)
    edges = []

    min_e[0] = 0

    for i in range(M):

        v = -1

        for j in range(M):
            if not used[j] and (v == -1 or min_e[j] < min_e[v]):
                v = j

        if min_e[v] == INF:
            print("No MST!")
            return -1

        used[v] = True

        if sel_e[v] != -1:
            #print(v, ' ', sel_e[v])
            edges.append([v, sel_e[v], matrix[v][sel_e[v]]])
            k += 1

        for to in range(M):
            if matrix[v][to] < min_e[to]:
                min_e[to] = matrix[v][to]
                sel_e[to] = v

    # print('k=',k)
    return edges
