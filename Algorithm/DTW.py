from datetime import datetime
import sys
import numpy as np
import math


def _find_matrix(data):
    M = len(data)
    matrix = sys.maxsize * np.ones((M, M))

    for i in range(M):
        start_time = datetime.now()
        print("Calculating distances for: \t", i)
        for j in range(M):
            matrix[i, j] = _dtw_distance(data[i], data[j])
        print("We have all distances for: \t", i)
        print("We spent:\t", datetime.now() - start_time)

    return matrix


a = 1


def _dtw_distance(ts_a, ts_b):
    # Create cost matrix via broadcasting with large int
    # ts_a, ts_b = np.array(ts_a), np.array(ts_b)
    M, N = len(ts_a), len(ts_b)
    cost = sys.maxsize * np.ones((M, N))
    minn = [0.0] * 2
    k, l = 0, 0
    # Initialize the first row and column
    cost[0, 0] = round(distance(ts_a[0], ts_b[0]), 5)

    # Populate rest of cost matrix within window
    k = 0
    l = 0
    while k + 1 < M or l + 1 < N:
        if k + 1 == M:
            minn[0] = k
            minn[1] = l + 1
            cost[k][l + 1] = cost[k][l] + round(distance(ts_a[k], ts_b[l + 1]), 5)
        elif l + 1 == N:
            minn[0] = k + 1
            minn[1] = l
            cost[k + 1][l] = cost[k][l] + round(distance(ts_a[k + 1], ts_b[l]), 5)
        else:
            cost[k + 1][l + 1] = cost[k][l] + round(distance(ts_a[k + 1], ts_b[l + 1]), 5)
            cost[k][l + 1] = cost[k][l] + round(distance(ts_a[k], ts_b[l + 1]), 5)
            cost[k + 1][l] = cost[k][l] + round(distance(ts_a[k + 1], ts_b[l]), 5)
            b = [cost[k + 1][l + 1], cost[k][l + 1], cost[k + 1][l]]
            iii = b.index(min(b))
            if iii == 0:
                minn[0] = k + 1
                minn[1] = l + 1
            if iii == 1:
                minn[0] = k
                minn[1] = l + 1
            if iii == 2:
                minn[0] = k + 1
                minn[1] = l
        k = minn[0]
        l = minn[1]
    # Return DTW distance given window

    return cost[-1, -1]


def distance(p1, p2):
    d = math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))
    return d
