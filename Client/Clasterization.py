import Algorithm.FindMST as mst
import numpy as np

edges = mst.findMst()

# If no MST, clastering cannot perfomed
if edges == -1:
    print('Clastering cannot be perfomed.')
else:
    # clustering preparation - creating an adjacency matrix
    matrix = -1 * np.ones((len(edges), len(edges)))
    for edge in edges:
        matrix[edge[0]][edge[1]] = edge[2]

    condition = 0.01

    # sorting edges in decreasing order
    sorted(edges, key=lambda edge: edge[2], reverse=True)

    for edge in edges:
        if edge[2] > condition:
            matrix[edge[0]][edge[1]] = 0
