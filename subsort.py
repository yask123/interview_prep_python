'''
subsort: Given an array of integers, write a method to  nd indices m and n such that if you sorted
EXAMPLE

lnput:1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19

Output: (3, 9)
'''


def subsort(arr):
    prev = arr[0]
    start_index = float('inf')
    for i in range(1, len(arr)):
        if arr[i] > prev:
            prev = arr[i]
        else:
            out_of_order_index = i

            correct_index = get_correct_index(arr, arr[i])

            start_index = min(start_index, correct_index)

    return (start_index, out_of_order_index)


def get_correct_index(arr, number):
    index = 0
    while number > arr[index]:
        index += 1

    return index


arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

print subsort(arr)
