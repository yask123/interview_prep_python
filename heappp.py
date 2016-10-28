import heapq

a = []

heapq.heappush(a,(10, 'yask'))
heapq.heappush(a,(99, 'god'))
heapq.heappop(a)[0]
print (a[0][1])