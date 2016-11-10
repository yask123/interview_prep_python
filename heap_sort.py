import heapq


def heap_sort(arr):
	heapq.heapify(arr)  # O(n) time
	result = []
	while len(arr) > 0:
		result.append(heapq.heappop(arr))  # Pop takes O(1) + O(log n) for re-heapification
	return result


arr = [34, 32, 3, 523, 5234, 32242, 4234]

print heap_sort(arr)
