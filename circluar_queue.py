'''
Implementation of circular queue which is integer overflow safes
'''


class CircularQueue:
	def __init__(self, capacity):
		self.capacity = capacity
		self.arr = [None] * self.capacity
		self.front = -1
		self.rear = -1

	def push(self, data):
		if (self.rear + 1) % len(self.arr) == self.front:
			raise Exception("Queue is full")
		else:
			if self.front == -1:
				self.arr[0] = data
				self.front = 0
				self.rear = 0
			else:
				self.rear = (self.rear + 1) % len(self.arr)
				self.arr[self.rear] = data

	def pop(self):
		if self.front == self.rear:
			self.rear = -1
			self.front - 1
		elif self.front == -1:
			raise Exception("Cant pop from empty queue")
		else:
			self.front = (self.front + 1) % len(self.arr)

	def print_queue(self):
		if self.rear < len(self.arr):
			self.rear += len(self.arr)
		for i in range(self.front, self.rear + 1):
			print self.arr[i % len(self.arr)],


a = CircularQueue(3)
a.push(1)
a.push(2)
a.push(3)
a.pop()
a.push(4)
a.print_queue()
a.pop()
print ''
a.print_queue()
