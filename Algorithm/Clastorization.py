from Algorithm.Condition import _find_Condition
import Algorithm.FindMST as mst
from collections import deque
from datetime import datetime
from Algorithm.FindMST import findMst
from Algorithm.FindMST import getMatrix
from Algorithm.FindNoises import findNoises
import numpy as np


def Iterations():
    matrix = getMatrix()
    INF = 10.0e777

    max_m = -INF
    min_m = INF
    for arr in matrix:
        np.sort(arr)

        j = len(arr) - 1
        while arr[j] <= 0:
            j -= 1

        if min_m > arr[j]:
            min_m = arr[j]
        if max_m < arr[0]:
            max_m = arr[0]

    return int(max_m / min_m)


def findFooting(max_iterations, iterations):
    return pow(max_iterations, 1 / iterations)


def Clustorization():
    # If no MST, clustering cannot performed
    iterations = Iterations()
    arr_clusters = []
    arr_lengths = []

    for iteration in range(iterations, 0, -1):

        footing = findFooting(iterations, iteration)
        matrix = findNoises(footing)

        condition = _find_Condition(matrix, footing)

        if condition != 0:
            clusters = []
            curr = []
            stack = deque()
            M = len(matrix)
            for i in range(M):

                if np.count_nonzero(matrix[i]) != 0:
                    stack.append(i)
                    curr.append(i)

                    while len(stack) != 0:

                        new = 0
                        cur_trajectory = stack.pop()
                        print("Our regular Cluster:")
                        start_time_Clustering = datetime.now()

                        print(cur_trajectory)
                        print("\n")

                        for j in range(M):
                            if matrix[cur_trajectory][j] != 0:
                                if matrix[cur_trajectory][j] < condition:
                                    new = 1
                                    curr.append(j)
                                    stack.append(j)

                                    for z in range(M):
                                        matrix[z][j] = 0

                        matrix[cur_trajectory] = 0

                        for j in range(M):
                            matrix[j][cur_trajectory] = 0

                        if new == 1:
                            if not curr:
                                curr.append(cur_trajectory)

                        print("We spent:\t", datetime.now() - start_time_Clustering)

                    if curr:
                        curr.sort()
                        clusters.append(curr)

                    curr = []
            arr_lengths.append(len(clusters))
            arr_clusters.append(clusters)

    min_l = min(arr_lengths)

    for i in arr_clusters:
        if len(i) == min_l:
            print(i)
            print("\n")
