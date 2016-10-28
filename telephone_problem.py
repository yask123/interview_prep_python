arr = [['a', 'b', 'c'],['d', 'e', 'f']]

def digits_comb(arr, current_list_index, current_comb, result):
    if current_list_index < 0:
        result.append(current_comb)
        return

    for each_char in arr[current_list_index]:
        digits_comb(arr, current_list_index-1, current_comb+each_char, result)

    return result

print (digits_comb(arr, len(arr)-1, '', []))
