import numpy as np
import sys
import math
import matplotlib.pyplot as plt

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


'''for i in range(M):
    arr1 = np.array(data[i])
#print(arr1[0:])
# x, y = arr1.T
# plt.scatter(x, y)



    #print(arr1[:, 0])


#print(arr1[:, 1])

    plt.plot(arr1[:, 0], arr1[:, 1])

plt.show()'''

