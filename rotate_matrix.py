'''
Given a matrix, clockwise rotate elements in it.

Examples:

Input
1    2    3
4    5    6
7    8    9

Output:
4    1    2
7    5    3
8    9    6

'''

import random

import printmatrix

n = 5
matrix = [[random.randint(1, 9) for each in range(n)] for each in range(n)]

printmatrix.p(matrix)


def rotate(matrix):
    top = 0
    bottom = len(matrix) - 1

    left = 0
    right = len(matrix[0]) - 1

    while top < bottom and left < right:
        prev = matrix[top + 1][left]

        for i in range(left, right + 1):
            current = matrix[top][i]
            matrix[top][i] = prev
            prev = current

        top += 1

        for i in range(top, bottom + 1):
            current = matrix[i][right]
            matrix[i][right] = prev
            prev = current

        right -= 1

        for i in range(right, left - 1, - 1):
            current = matrix[bottom][i]
            matrix[bottom][i] = prev
            prev = current
        bottom -= 1

        for i in range(bottom, top - 1, - 1):
            current = matrix[i][left]
            matrix[i][left] = prev
            prev = current

        left += 1


rotate(matrix)
print '\n'
printmatrix.p(matrix)
