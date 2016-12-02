'''
You are given a set of coins S. In how many ways can you make sum N assuming you have infinite amount of each coin in the set.

Input :
	S = [1, 2, 3]
	N = 4

Return : 4

Explanation : The 4 possible ways are
{1, 1, 1, 1}
{1, 1, 2}
{2, 2}
{1, 3}

hacky trick to pass values by reference
'''


def coins(arr, n, target, result, comb_result):
    if result == None:
        return
    result = result[:]
    if target == 0:
        comb_result.append(result)
        return

    if target < 0 or n < 0:
        return

    result.append(arr[n])
    coins(arr, n, target - arr[n], result, comb_result)
    result.pop()

    coins(arr, n - 1, target, result, comb_result)
    return comb_result


S = [1, 2, 3]
N = 4

print coins(S, len(S) - 1, N, [], [])
