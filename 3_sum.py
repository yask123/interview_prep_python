'''
For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

def three_sum(arr):
    arr.sort()
    if len(arr) <= 1:
        return temp
    result = []
    for i in range(len(arr)):
        k = find_three_sum(i, arr)
        if k:
            result.append(k)
    return result

def find_three_sum(current_index, arr):
    start_index, end_index = current_index+1,len(arr)-1

    while start_index < end_index:
        k = arr[start_index] + arr[end_index] + arr[current_index]

        if k == 0 and all_index_unique(start_index, end_index, current_index):
            return [arr[start_index], arr[end_index],arr[current_index]]
        elif k < 0:
            start_index += 1
        else:
            end_index -= 1

    return False
