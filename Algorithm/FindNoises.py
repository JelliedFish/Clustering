import numpy as np
import Algorithm.FindMedian as fm
from Algorithm.FindMST import getMatrix
from Input.Input_by_distnces_matrix import InputD


def findNoises(footing):
    matrix = getMatrix()

    median = fm.findMedian(matrix, footing)

    M = len(matrix)
    for i in range(M):
        for j in range(M):
            if matrix[i][j] >= median:
                matrix[i][j] = 0

    return matrix
