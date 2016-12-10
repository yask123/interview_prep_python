'''
Smallest k numbers

k size max heap
'''

import heapq


def smallest_k(arr, k):
    max_heap = [] * k
    for i in range(k):
        heapq.heappush(max_heap, arr[i] * - 1)

    for i in range(k, len(arr)):

        if arr[i] < max_heap[0] * -1:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, arr[i] * -1)

    return [each * -1 for each in max_heap]


arr = [8, 9, 1, 5, 6, 4, 3, -9]

print smallest_k(arr, 3)
