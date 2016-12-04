'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return 1 ( true ).

A = [3,2,1,0,4], return 0 ( false ).

Return 0/1 for this problem
'''


def ispossible(arr, pos, cache):
    if pos in cache:
        return cache[pos]

    if pos == len(arr) - 1:
        cache[pos] = 1
        return cache[pos]

    if pos >= len(arr):
        cache[pos] = 0
        return cache[pos]

    for each_jump in range(arr[pos], 0, -1):
        x = ispossible(arr, pos + each_jump, cache)

        if x == 1:
            cache[pos] = 1
            return cache[pos]

    cache[pos] = 0
    return cache[pos]


A = [3, 2, 1, 0, 4]
cache = {}
print ispossible(A, 0, cache)
