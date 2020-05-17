import numpy as np
import Algorithm.FindMedian as fm
from Input.Input_by_distnces_matrix import InputD
from Input.Input_by_points import InputP
from Input.read_trajectories import InputCSV

Main_matrix = InputCSV()
M = len(Main_matrix)


def getMatrix():
    return InputD()


def findMst():
    # Prim's algorithm
    INF = 10.0e777

    matrix = getMatrix()
    M = len(matrix)
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
            edges.append([v, sel_e[v], matrix[v][sel_e[v]]])
            k += 1

        for to in range(M):
            if matrix[v][to] < min_e[to]:
                min_e[to] = matrix[v][to]
                sel_e[to] = v

    # sorting edges in decreasing order
    sorted(edges, key=lambda edge: edge[2], reverse=True)

    return edges


def mstAsMatrix(edges):
    matrix = 0 * np.ones((len(edges) + 1, len(edges) + 1))
    for edge in edges:
        matrix[edge[0]][edge[1]] = edge[2]
        matrix[edge[1]][edge[0]] = edge[2]

    return matrix
