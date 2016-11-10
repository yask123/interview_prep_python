def merge_sort(arr):
    start_index = 0
    end_index = len(arr) - 1

    _merge_sort(arr, start_index, end_index)

    return arr


def _merge_sort(arr, start_index, end_index):
    if start_index < end_index:
        mid = (start_index + end_index) / 2

        _merge_sort(arr, start_index, mid)
        _merge_sort(arr, mid + 1, end_index)

        merge(arr, start_index, end_index)


def merge(arr, start_index, end_index):
    mid = (start_index + end_index) / 2

    a_index = start_index
    b_index = mid + 1
    temp = []
    while a_index <= mid and b_index <= end_index:
        if arr[a_index] < arr[b_index]:
            temp.append(arr[a_index])
            a_index += 1
        else:
            temp.append(arr[b_index])
            b_index += 1

    temp.extend(arr[a_index: mid + 1])
    temp.extend(arr[b_index: end_index + 1])

    arr[start_index: end_index + 1] = temp


arr = [43, 23, 324, 56, 324, 3243]

merge_sort(arr)

print arr
