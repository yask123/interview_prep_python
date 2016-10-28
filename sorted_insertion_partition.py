def searchInsert(A, B):

    if B < A[0]:
        return 0
    start = 1
    end = len(A)-1
    while start <= end:
        mid = (start+end)/2
        print start,end, mid
        if A[mid] ==B:
            return mid
        if A[mid] > B and A[mid-1] < B:
            return mid
        elif A[mid] > B:
            end = mid-1
        else:
            start = mid + 1
    return end+1
arr = [1,2,5,6]
print searchInsert(arr,19)
