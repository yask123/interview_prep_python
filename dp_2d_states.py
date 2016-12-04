'''
Longest palindrome problem
'''
import printmatrix

s = 'ababab'
r = len(s)
P = [[0 for each in range(r)] for each in range(r)]

for i in range(r):
    P[i][i] = 1

for i in range(1, r):
    if s[i] == s[i - 1]:
        P[i - 1][i] = 1

printmatrix.p(P)
max_length = 0

for i in range(2, r):
    row = 0
    col = i
    while row < r and col < r:
        if P[row + 1][col - 1] == 1 and s[row] == s[col]:
            P[row][col] = 1
            max_length = max(max_length, (col - row) + 1)
        row += 1
        col += 1
print '\n'
printmatrix.p(P)
print max_length
