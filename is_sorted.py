def is_sorted(arr,current_index):
    if current_index == len(arr)-1:
        return True

    return (arr[current_index] < arr[current_index+1]) and is_sorted(arr, current_index+1)

arr = [9]

print is_sorted(arr,0)
