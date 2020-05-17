import pandas as pd
import numpy as np
import csv
from collections import defaultdict
import sys
from Algorithm.DTW import _find_matrix


def InputCSV():
    curr = defaultdict(list)
    array = []
    line = []

    id = sys.maxsize

    with open('../Data/camera_data_24_005.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            id = row['localobjectid']
            line.append(float(row['posx']))
            line.append(float(row['posy']))
            curr[id].append(line)
            line = []

    data = np.array(list(curr.values()))
    matrix = _find_matrix(data)
    return matrix
