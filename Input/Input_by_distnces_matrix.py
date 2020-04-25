import numpy as np



f = open('../Data/matrix.txt', 'r')

arr = []
for line in f:
    nums = [float(x) for x in line.strip().split(" ")]
    arr.append(nums)

matrix = np.array(arr)
M = len(matrix)