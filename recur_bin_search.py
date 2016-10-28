def bin_search(arr, start_index, end_index, key):
    if start_index <= end_index:
        mid = (start_index + end_index)/2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return bin_search(arr,mid+1, end_index, key)
        else:
            return bin_search(arr,start_index, mid-1, key)


arr = [1,2,3,4,5]

print bin_search(arr,0,len(arr)-1,1)
