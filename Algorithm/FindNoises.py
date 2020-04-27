import numpy as np
import Algorithm.FindMedian as fm
from Input.Input_by_distnces_matrix import InputD

def findNoises():
    matrix = InputD()

    median = fm.findMedian(matrix)

    for i in matrix:
        for j in i:
            if matrix[i][j] >= median:
                matrix[i][j] = 0

    return matrix