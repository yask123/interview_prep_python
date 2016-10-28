arr = [7,8,9,1,2,3,4,5]

def search_in_rotated(arr, key):

    start_index = 0
    end_index = len(arr)-1

    while start_index <= end_index:

        mid = (end_index + start_index)/2
        if arr[mid] == key:
            return mid

        if arr[start_index] <= arr[mid-1]:
            if in_range(key, start_index, mid-1):
                end_index = mid - 1
            else:
                start_index = mid + 1
        else:
            if in_range(key, mid+1, end_index):
                start_index = mid + 1
            else:
                end_index = mid - 1
    return -1

def in_range(key, start_index, end_index):
    if key >= arr[start_index] and key <= arr[end_index]:
        return True
    return False

print search_in_rotated(arr, 4)
