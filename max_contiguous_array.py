def max_cont_array(arr):
    current_sum = arr[0]
    max_sum = arr[0]
    all_negative = True
    for i in range(len(arr)):
        if arr[i] > 0:
            all_negative = False
        current_sum += arr[i]
        if current_sum < 0:
            current_sum = 0

        if current_sum > max_sum:
            max_sum = current_sum
    if all_negative:
        return max(arr)
    else:
        return max_sum

print max_cont_array([-2,-5,12,-9])
