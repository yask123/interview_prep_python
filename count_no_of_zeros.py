def count_zeros(arr, current_index):
    if current_index == len(arr):
        return 0

    if arr[current_index] == 0:
        return 1+ count_zeros(arr, current_index+1)
    else:
        return count_zeros(arr, current_index+1)

arr = [0,0,0,0]
print count_zeros(arr,0)
