import random

import printmatrix

n = 5

matrix = [[random.randint(0, 1) for each in range(n)] for each in range(n)]


def max_sub_matrix(matrix, n):
    P = [[0 for each in range(n)] for each in range(n)]

    for i in range(n):
        P[i][0] = 1
        P[0][i] = 1

    for i in range(1, n):
        for j in range(1, n):
            if matrix[i][j] == 1:
                P[i][j] = min(P[i - 1][j - 1], P[i - 1][j], P[i][j - 1]) + 1
    max_size = 1

    for i in range(n):
        for j in range(n):
            max_size = max(max_size, P[i][j])

    return max_size


print max_sub_matrix(matrix, n)
print printmatrix.p(matrix)
