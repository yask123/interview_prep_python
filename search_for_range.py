'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

'''


def left_starting_point(arr, k):
    start = 0
    end = len(arr) - 1
    left_index = - 1
    while start <= end:
        mid = (start + end) / 2
        if k <= arr[mid]:
            end = mid - 1
            left_index = mid
        else:
            start = mid + 1

    if arr[left_index] == k:
        return left_index
    return - 1


def right_starting_point(arr, k):
    start = 0
    end = len(arr) - 1

    right_index = -1

    while start <= end:
        mid = (start + end) / 2

        if k >= arr[mid]:
            start = mid + 1
            right_index = mid
        else:
            end = mid - 1

    if arr[right_index] == k:
        return right_index
    return - 1


arr = [1, 1, 2, 2, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4, 5]


def get_starting_end_index(arr, k):
    return (left_starting_point(arr, k), right_starting_point(arr, k))


print get_starting_end_index(arr, 2)
