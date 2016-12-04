'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

Example :

Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''


def ways(arr, n):
    if n == -1:
        return 1
    if n < -1:
        return 0

    if n >= 1 and int(str(arr[n]) + str(arr[n - 1])) <= 26:
        a = ways(arr, n - 2)
        b = ways(arr, n - 1)
        return a + b
    else:
        return ways(arr, n - 1)


print ways([1, 2, 9], 2)
