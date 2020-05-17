import pandas as pd
from collections import namedtuple
import random
import sys
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

curr = []
arr = []

f = open('../Data/60.txt', 'r')
#f1 = open('../Data/origin_trajectories.txt')

for line in f:
    if len(line) > 2:
        nums = [float(x) for x in line.strip().split(" ")]
        curr.append(nums)
    else:
        arr.append(curr)
        curr = []
data = np.array(arr)
curr = []
arr = []

'''for line in f1:
    if len(line) > 2:
        nums = [float(x) for x in line.strip().split(" ")]
        curr.append(nums)
    else:
        arr.append(curr)
        curr = []
arr.append(curr)
origin = np.array(arr)
print(len(origin))'''

for i in range(0, 30):
    arr1 = np.array(data[i])
    plt.plot(arr1[:, 0], arr1[:, 1])

#arr2 = np.array(origin[0])
#plt.plot(arr2[:, 0], arr2[:, 1], color='black')

for i in range(30, 59):
    arr1 = np.array(data[i])
    plt.plot(arr1[:, 0], arr1[:, 1])
#arr2 = np.array(origin[1])
#plt.plot(arr2[:, 0], arr2[:, 1], color='blue')
plt.show()


'''for i in range(20, 30):
    arr1 = np.array(data[i])
    plt.plot(arr1[:, 0], arr1[:, 1])
arr2 = np.array(origin[2])
plt.plot(arr2[:, 0], arr2[:, 1], color='red')
# plt.show()

for i in range(30, 40):
    arr1 = np.array(data[i])
    plt.plot(arr1[:, 0], arr1[:, 1])
arr2 = np.array(origin[3])
plt.plot(arr2[:, 0], arr2[:, 1], color='green')
# plt.show()

for i in range(40, 50):
    arr1 = np.array(data[i])
    plt.plot(arr1[:, 0], arr1[:, 1])
arr2 = np.array(origin[4])
plt.plot(arr2[:, 0], arr2[:, 1], color='orange')
plt.show()'''
