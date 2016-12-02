'''
Given N * M field of O's and X's, where O=white, X=black
Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)
'''


def count_black(matrix):
    l, m = len(matrix), len(matrix[0])
    count = 0
    for i in range(l):
        for j in range(m):
            if matrix[i][j] == 'X':
                count += 1
                black_dfs(matrix, i, j)
    return count


def black_dfs(matrix, row, col):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return False
    if matrix[row][col] != 'X':
        return False

    matrix[row][col] = 'O'
    black_dfs(matrix, row, col + 1)
    black_dfs(matrix, row, col - 1)
    black_dfs(matrix, row + 1, col)
    black_dfs(matrix, row - 1, col)
