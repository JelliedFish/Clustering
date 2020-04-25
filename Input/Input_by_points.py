import numpy as np
from Algorithm.DTW import _find_matrix
import sys
import math
import matplotlib.pyplot as plt


def InputP():

    curr = []
    arr = []

    f = open('../Data/100.txt', 'r')

    for line in f:
        if len(line) > 2:
            nums = [float(x) for x in line.strip().split(" ")]
            curr.append(nums)
        else:
            arr.append(curr)
            curr = []

    arr.append(curr)
    data = np.array(arr)
    matrix = _find_matrix(data)
    return matrix



