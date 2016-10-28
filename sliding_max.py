'''
Input: A long array A[], and a window width w
Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
Requirement: Find a good optimal way to get B[i]
'''
'''
len = 5
5-3 = 2
1 2 3 4 5 
'''

class max_queue:
	def __init__(self):
		self.max_stack = []
		self.queue = []
	
	def push(self,value):
		if len(self.max_stack) == 0 or self.max_stack[-1] < value:
			self.max_stack.append(value)
		self.queue.append(value)

	def pop(self):
		popped_element = self.queue.pop(0)
		if popped_element == self.max_stack[-1]:
			self.max_stack.pop()
	def get_max(self):
		return self.max_stack[-1]

		


def sliding_max(arr, k):
	mq = max_queue()
	start_window_index = 0
	end_window_index = k-1

	for each in range(0,k):
		mq.push(each)
		
	for each in arr:


print (sliding_max([1, 3, -1, -3, 5, 3, 6, 7], 3))