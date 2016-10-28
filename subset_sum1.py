def subset_sum(arr, current_index, target, result):
    if target == 0:
        print result
        return 0
    if target < 0:
        return 0
    if current_index >= len(arr):
        return 0

    subset_sum(arr, current_index+1, target - arr[current_index], result+str(arr[current_index]))
    subset_sum(arr, current_index+1, target, result)

arr = [1,2,3]

subset_sum(arr,0,3,'')
