'''
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

'''
import heapq


def most_frequent(arr, k):
	freq_map = {}
	min_heap = []
	for each in arr:
		if each in freq_map:
			freq_map[each] += 1
		else:
			freq_map[each] = 1
		if len(min_heap) < k:
			heapq.heappush(min_heap, (freq_map[each], each))
		else:
			if min_heap[0][0] < freq_map[each]:
				heapq.heappop(min_heap)
				heapq.heappush(min_heap, (freq_map[each], each))
	for each in min_heap:
		print each


arr = [1, 1, 1, 2, 2, 3]

most_frequent(arr, 2)
