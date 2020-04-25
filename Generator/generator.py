import random
from collections import namedtuple
import numpy as np

f = open('originTrajectories.txt', 'r')
curr = []
arr = []
dist = 0.0

# file reading

for line in f:
    if len(line) > 2:
        nums = [float(x) for x in line.strip().split(" ")]
        curr.append(nums)
    else:
        arr.append(curr)
        curr = []
arr.append(curr)
data = np.array(arr)

f1 = open('../../Desktop/100.txt', 'w')

for j in range(len(data)):
    for k in range(0, 20):
        for point in data[j]:
            noiseX = random.uniform(-0.0001, 0.0001)
            noiseY = random.uniform(-0.0001, 0.0001)
            x = point[0] + noiseX
            y = point[1] + noiseY
            f1.write(repr(x) + ' ' + repr(y) + '\n')
        f1.write('\n')








