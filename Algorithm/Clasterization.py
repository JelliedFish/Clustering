import Algorithm.FindMST as mst

edges = mst.findMst()

# If no MST, clastering cannot perfomed
if edges == -1:
    print('Clastering cannot be perfomed.')
else:
    # clustering preparation - creating an adjacency matrix
    matrix = mst.mstAsMatrix(edges)

    condition = 0.01

    for edge in edges:
        if edge[2] > condition:
            matrix[edge[0]][edge[1]] = 0
