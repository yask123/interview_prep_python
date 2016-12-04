'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example :
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

If it is not possible to reach the end index, return -1.
'''
cache = {}


def min_jumps(arr, pos):
    if pos in cache:
        return cache[pos]

    if pos == len(arr) - 1:
        cache[pos] = 0
        return cache[pos]

    if pos >= len(arr):
        return float('inf')

    result = float('inf')

    for each_jump_length in range(1, arr[pos] + 1):
        result = min(result, 1 + min_jumps(arr, pos + each_jump_length))

    cache[pos] = result
    return result


A = [2, 3, 1, 1, 4]

print min_jumps(A, 0)
