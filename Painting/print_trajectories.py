import pandas as pd
from collections import namedtuple
import random
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from collections import defaultdict

curr = defaultdict(list)
array = []
line = []

id = sys.maxsize

with open('../Data/camera_data_24_005.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        id = row['localobjectid']
        line.append(row['posx'])
        line.append(row['posy'])
        curr[id].append(line)
        line = []

data = np.array(list(curr.values()))

arr1 = np.array(data[0])
plt.plot(arr1[:, 0], arr1[:, 1], color='black')

arr1 = np.array(data[1])
plt.plot(arr1[:, 0], arr1[:, 1], color='red')

arr1 = np.array(data[2])
plt.plot(arr1[:, 0], arr1[:, 1], color='orange')

arr1 = np.array(data[3])
plt.plot(arr1[:, 0], arr1[:, 1], color='green')

arr1 = np.array(data[4])
plt.plot(arr1[:, 0], arr1[:, 1], color='blue')

arr1 = np.array(data[5])
plt.plot(arr1[:, 0], arr1[:, 1], color='brown')

arr1 = np.array(data[6])
plt.plot(arr1[:, 0], arr1[:, 1], color='yellow')

plt.show()
