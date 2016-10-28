
arr = [['a', 'b', 'c'], ['d', 'e','f']]

def find_comb(arr, current_list, current_index, result):
    if current_list >= len(current_list):
        return 
    if current_list == len(current_list)-1:
        result + arr[current_list][current_index]
        print result
    
    find_comb(arr, current_list+1, current_index, result+arr[current_list][current_index])
    current_index+=1
