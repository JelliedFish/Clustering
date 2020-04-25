import math


def _Standard_Deviation_AVG(arr):
    x_ = 0
    d = 0
    size = len(arr)

    for i in arr:
        x_ += i

    x_ /= size

    for i in arr:
        d += (i - x_) ** 2

    d /= size
    d = math.sqrt(d)

    return d + x_
