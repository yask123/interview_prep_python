arr = [1,5,2]




def merge_sort(arr, start_index, end_index):
    count = 0
    if start_index < end_index:
        mid = (start_index + end_index)/2
        count += merge_sort(arr, start_index, mid)
        count += merge_sort(arr, mid+1, end_index)

        count += merger(arr, start_index, end_index)
        return count
    else:
        return 0

def merger(arr, start_index, end_index):
    a_index =  start_index
    mid = (start_index+end_index)/2
    b_index = mid+1
    temp = []
    count =  0
    while (a_index <= mid and b_index <= end_index):
        if arr[a_index] < arr[b_index]:
            temp.append(arr[a_index])
            a_index+=1
        else:
            temp.append(arr[b_index])
            count += (mid - a_index)+1
            b_index+=1
    temp.extend(arr[a_index:mid+1])
    temp.extend(arr[mid+1:end_index+1])
    arr[start_index: end_index+1] = temp
    return count

print merge_sort(arr,0,len(arr)-1)
