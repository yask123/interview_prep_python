import heapq


def k_greatest(arr, k):
	min_heap = []
	for i in range(k):
		heapq.heappush(min_heap, arr[i])

	for i in range(k, len(arr)):
		if arr[i] > min_heap[0]:
			heapq.heappop(min_heap)
			heapq.heappush(min_heap, arr[i])
	return min_heap


arr = [7, 5, 3, 2, 44]

print k_greatest(arr, 1)
