from Algorithm.Condition import _find_Condition
from Input.Input_by_points import *
from collections import deque
from datetime import datetime
import math

print("The algorithm has started:")
start_algorithm_time = datetime.now()

clusters = []
curr = []
stack = deque()

radius = _find_Condition()

print("DATA: \n")

# print(matrix[200][201])
# print(matrix[200][206])
print("DATA: \n")

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
                if matrix[cur_trajectory][j] <= radius:
                    if matrix[cur_trajectory][j] != 0:

                        new = 1

                        length = len(data[cur_trajectory]) if len(data[cur_trajectory]) < len(data[j]) else len(data[j])
                        flg = 1
                        for k in range(length):
                            f = math.sqrt((data[cur_trajectory][k][0] - data[j][k][0]) ** 2 + (
                                    data[cur_trajectory][k][1] - data[j][k][1]) ** 2)
                            if f > radius:
                                flg = 0
                                break

                        if flg == 1:
                            curr.append(j)
                            stack.append(j)
                            matrix[j] = 0
                            for z in range(M):
                                matrix[z][j] = 0
                # else:
                # print("Our tr is: ", j, "Distance: \t", matrix[cur_trajectory][j])

            matrix[cur_trajectory] = 0

            for j in range(M):
                matrix[j][cur_trajectory] = 0

            if new == 1:
                if not curr:
                    curr.append(cur_trajectory)

            print("We spent:\t", datetime.now() - start_time_Clustering)

            if curr:
                clusters.append(curr)

            curr = []

print("Our radius is:\t", radius)

print("Our clusters are:\t", clusters)

print("All time for algorithm:", datetime.now() - start_algorithm_time)
