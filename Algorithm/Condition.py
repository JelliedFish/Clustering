from datetime import datetime
from Algorithm.AVG import _Standard_Deviation_AVG
import numpy as np
import math


# Assembled the matrix

def _find_Condition(distances, footing):
    print("Trying to find the Condition...")
    start_time = datetime.now()
    condition = 0

    arr = []

    M = len(distances)
    for i in range(M):
        for var in distances[i]:
            arr.append(var)

    arr.sort()

    min_index = 0
    while arr[min_index] == 0:
        min_index += 1

    min_ = arr[min_index]
    max_ = arr[len(arr) - 1]

    last_column: int = math.ceil(math.log(max_, footing))
    first_column: int = math.floor(math.log(min_, footing))

    last_column = last_column - first_column

    table = 0 * np.ones(last_column)

    for i in arr:
        if i != 0:
            table[math.floor(math.log(i, footing)) - first_column] += 1
        AVG = _Standard_Deviation_AVG(table)
        for j in range(len(table)):
            if table[j] >= AVG:
                interval_end = j + first_column

    condition = math.pow(footing, interval_end + 1) - math.pow(footing, interval_end)

    print("We spent:", datetime.now() - start_time, "time")

    return condition
