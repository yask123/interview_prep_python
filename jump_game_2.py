'''Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
'''

A = [2, 3, 1, 1, 4]


def jump_game(pos, arr, cache={}):
    if pos in cache:
        return cache[pos]

    if pos == len(arr) - 1:
        return 0
    if pos >= len(arr):
        return float('inf')

    min_jump_count = float('inf')

    for i in range(1, arr[pos] + 1):
        min_jump_count = min(min_jump_count, 1 + jump_game(pos + i, arr))

    cache[pos] = min_jump_count
    return cache[pos]


print jump_game(0, A)
