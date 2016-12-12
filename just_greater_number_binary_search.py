def just_greater(arr, k):
    start = 0
    end = len(arr) - 1

    result = -1

    while start <= end:

        mid = (start + end) / 2
        if arr[mid] == k:
            return mid

        elif arr[mid] > k:
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    return result


def just_lower(arr, k):
    start = 0
    end = len(arr) - 1

    result = - 1

    while start <= end:
        mid = (start + end) / 2

        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    return result


arr = [1, 4, 10, 15, 20]

print just_greater(arr, 3)

print just_lower(arr, 30)
