import numpy as np
import math


def findMedian(matrix):
    median = 0.0

    max_ = -10.0e777

    min_ = 10.0e777

    M = len(matrix)

    for i in range(M):
        for j in range(M):

            if matrix[i][j] > max_:
                if matrix[i][j] != 0:
                    max_ = matrix[i][j]

            if matrix[i][j] < min_:
                if matrix[i][j] != 0:
                    min_ = matrix[i][j]

    count_of_intervals = (
                math.ceil(math.log10(max_)) - math.floor(math.log10(min_)))  # the power of number is really big

    if count_of_intervals % 2 == 1:
        median = math.pow(10, math.ceil(count_of_intervals / 2))
    else:
        median = math.pow(10, (count_of_intervals / 2 + count_of_intervals / 2 + 1) / 2)

    return median
