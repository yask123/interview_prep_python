import heapq


# Left half is max heap, right half in min heap
# To use min heap as max heap we insert -1 * item and pop as -1 * item

def running_median(arr):
	min_heap = []
	max_heap = []

	for i in range(len(arr)):
		if len(max_heap) == 0 or arr[i] < max_heap[0] * -1:
			heapq.heappush(max_heap, -1 * arr[i])
		else:
			heapq.heappush(min_heap, arr[i])

		while abs(len(max_heap) - len(min_heap)) > 1:
			if len(max_heap) > len(min_heap):
				popped_item = heapq.heappop(max_heap) * -1
				heapq.heappush(min_heap, popped_item)
			else:
				popped_item = heapq.heappop(min_heap)
				heapq.heappush(max_heap, popped_item * -1)

	if len(min_heap) > len(max_heap):
		return min_heap[0]
	elif len(max_heap) > len(min_heap):
		return -1 * max_heap[0]
	else:
		return (max_heap[0] * -1 + min_heap[0]) / 2


arr = [1, 2, 3, 4, 5, 6, 7, 100, 101]

print running_median(arr)
