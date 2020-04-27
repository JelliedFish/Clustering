import numpy as np
import math

def findMedian(matrix):
    median = 0.0
    max = matrix[0][0]
    min = matrix[0][0]

    M = len(matrix)
    for i in range(M):
        for j in range(M):

            if matrix[i][j] > max:
                max = matrix[i][j]

            if matrix[i][j] < min:
                min = matrix[i][j]

    count_of_intervals = (math.ceil(math.log10(max)) - math.floor(math.log10(min)))

    if count_of_intervals % 2 == 1:
        median = math.pow(10, math.ceil(count_of_intervals/2))
    else:
        median = math.pow(10, (count_of_intervals/2 + count_of_intervals/2 + 1)/2)

    return median

