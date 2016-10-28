def rotation_point(arr):
    start_index = 0
    end_index = len(arr)-1

    while start_index <= end_index:
        mid = (start_index + end_index)/2
        if mid == 0:
            return 0
        elif mid == len(arr)-1:
            return mid

        if arr[mid] < arr[mid+1] and arr[mid-1] > arr[mid]:
            return mid

        if arr[mid] < arr[end_index]:
            end_index = mid - 1
        else:
            start_index = mid + 1

arr = [ 6,9,1]

print rotation_point(arr)
