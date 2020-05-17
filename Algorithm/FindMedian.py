import numpy as np
import math


def findMaxIndex(table):
    max_index = 0
    M = len(table)
    max_value = max(table)

    for i in range(M):
        if table[i] == max_value:
            max_index = i
    return max_index


def findPopularValue(index, diff):
    max_value = math.pow(10, index + diff)
    return max_value


def findMaxValue(table):
    table.sort()
    return table[len(table) - 1]


def findMedian(matrix, footing):
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

    count_of_intervals = (math.ceil(math.log(max_, footing)) - math.floor(math.log(min_, footing)))
    min_power = math.floor(math.log(min_, footing))

    median = math.pow(footing, min_power + (count_of_intervals / 2))

    return median
