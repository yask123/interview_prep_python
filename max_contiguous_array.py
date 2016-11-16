'''
This is implemented by divide and conquer method.
solve for left, solve for right (easy)
solve for middle ->
this means get the max contiguous sum which must contain middle element

then recursively return the max of all three.

You can also solve it with Kadane's algorithm in O(n), but I still think,
solving this way is more elegant

'''


def max_cont_array(arr, start_index, end_index):
    if start_index < end_index:
        mid = (start_index + end_index) / 2
        left_max_sum = max_cont_array(arr, start_index, mid)
        right_max_sum = max_cont_array(arr, mid + 1, end_index)

        current_sum = get_current_max_sum(arr, start_index, mid, end_index)

        return max(left_max_sum, right_max_sum, current_sum)
    else:
        return arr[start_index]


def get_current_max_sum(arr, start_index, mid, end_index):
    current_sum = 0
    max_sum = -float('inf')

    for i in range(mid - 1, -1, -1):
        current_sum += arr[i]
        if max_sum < current_sum:
            max_sum = current_sum
    left_max_sum = max_sum

    max_sum = -float('inf')
    current_sum = 0
    for i in range(mid + 1, end_index + 1):
        current_sum += arr[i]
        if max_sum < current_sum:
            max_sum = current_sum

    right_max_sum = max_sum

    return arr[mid] + left_max_sum + right_max_sum


arr = [-10, 3, -1, 5, 7]
print max_cont_array(arr, 0, len(arr) - 1)
