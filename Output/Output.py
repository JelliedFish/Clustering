def _output(matrix, M):
    with open('../Data/matrix.txt', 'w') as g:
        for i in range(M):
            for j in range(M):
                g.write(str(matrix[i, j]) + " ")
            g.write("\n")
    g.close()
