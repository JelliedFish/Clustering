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

    for var in distances:
        arr.append(var)

    arr.sort()

    min_ = arr[0]
    max_ = arr[len(arr) - 1]

    last_column: int = int(math.fabs(int(math.log10(max_))))
    first_column: int = int(math.fabs(int(math.log10(min_))))

    last_column = last_column + first_column

    table = 0 * np.ones(last_column + 1)

    if min_ < 1:

        for i in arr:
            table[int(math.log10(i)) + first_column] += 1
            interval_end = int(math.log10(_Standard_Deviation_AVG(table))) - first_column



    else:

        for i in arr:
            table[int(math.log10(i)) - first_column] += 1
            interval_end = int(math.log10(_Standard_Deviation_AVG(table))) + first_column

    condition = math.pow(10, interval_end+1)-math.pow(10, interval_end)

    print("We spent:", datetime.now() - start_time, "time")

    return condition


print(_find_Condition([0.0001, 0.0001, 0.0001, 0.0001, 0.00012, 0.000123, 0.00012, 3, 10, 100]))
