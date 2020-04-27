from Algorithm.Condition import _find_Condition
import Algorithm.FindMST as mst
from collections import deque
from datetime import datetime
from Algorithm.FindMST import findMst
from Algorithm.FindMST import getMatrix
import numpy as np


def Clusterization():
    edges = mst.findMst()
    matrix = getMatrix()

    # If no MST, clustering cannot performed

    if edges == -1:
        print('Clustering cannot be performed.')
    else:
        # clustering preparation - creating an adjacency matrix

        condition = _find_Condition(edges)

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
                print(len(clusters))
    return clusters
