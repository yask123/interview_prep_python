arr = [1, 2, 3]


def pass_by_value(arr):
    arr = arr[:]
    arr[0] = 3


print arr
pass_by_value(arr)
print arr
