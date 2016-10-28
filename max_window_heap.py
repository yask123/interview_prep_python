'''

[1 3 -1 -3 5 3 6 7]
           ^     ^
make s size heap -> pop max


'''

import heapq

my_heap = []

def sliding_max(arr, k):
    result = []
    for i in range(k):
        heapq.heappush(my_heap,arr[i]*-1)
    result.append(my_heap[0]*-1)

    for i in range(k, len(arr)):
        my_heap[k-1] = arr[i]*-1
        heapq.heapify(my_heap)
        result.append(my_heap[0]*-1)

    return result


print (sliding_max([1 ,3 ,-1, -3, 5, 3, 6, 7], 3))
