'''
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n.

Determine the maximum value obtainable by cutting up the rod and selling the pieces.
For example, if length of the rod is 8 and the values of different pieces are given as following, then

the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)


length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20
'''


def rod_curring(arr, n):
    if n <= 0:
        return 0

    max_profit = float('-inf')
    for i in range(n):
        max_profit = max(max_profit, arr[i] + rod_curring(arr, n - i - 1))

    return max_profit


arr = [1, 5, 8, 9, 10, 17, 17, 20]

print rod_curring(arr, len(arr))
