from datetime import datetime
from Algorithm.AVG import _Standard_Deviation_AVG
import numpy as np
import math


# Assembled the matrix

def _find_Condition(distances):
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

    for i in range(min_index):
        arr[i] = arr[min_index]

    min_ = arr[0]
    max_ = arr[len(arr) - 1]

    last_column: int = int(math.fabs(int(math.log10(max_))))
    first_column: int = int(math.fabs(int(math.log10(min_))))

    last_column = last_column + first_column

    table = 0 * np.ones(last_column + 1)

    if min_ < 1:

        for i in arr:
            table[int(math.log10(i)) + first_column] += 1
        interval_end = table[len(table) - 1]
        AVG = _Standard_Deviation_AVG(table)
        for i in range(len(table)):
            if table[i] > AVG:
                interval_end = i - first_column



    else:

        for i in arr:
            table[int(math.log10(i)) - first_column] += 1
        interval_end = table[len(table) - 1]
        AVG = _Standard_Deviation_AVG(table)
        for i in range(len(table)):
            if table[i] > AVG:
                interval_end = i + first_column

    condition = math.pow(10, interval_end) - math.pow(10, interval_end - 1)

    print("We spent:", datetime.now() - start_time, "time")

    return condition
