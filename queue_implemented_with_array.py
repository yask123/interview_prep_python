class Queue:
	def __init__(self, capacity=10):
		self.capacity = capacity
		self.front = -1
		self.rear = -1
		self.arr = [None] * self.capacity

	def push(self, data):
		if (self.front + 1) % self.capacity == self.rear % self.capacity:
			raise Exception("Queue is full")
		if self.rear == -1:
			self.front = 0
			self.rear = 0
		else:
			self.front += 1

		self.arr[self.front % self.capacity] = data

	def pop(self):
		if self.front == self.rear:
			self.front = -1
			self.rear = -1
		elif (self.rear > self.front):
			raise Exception(" Queue is empty")
		else:
			self.rear += 1

	def print_queue(self):
		for i in range(self.rear, self.front + 1):
			print self.arr[i % self.capacity], '-->',


a = Queue()

a.push(1)
a.push(2)
a.pop()
a.push(3)
a.pop()
a.print_queue()
print '\n'
for i in range(9):
	a.push(i)

a.print_queue()

a.pop()
print '\n'
a.print_queue()
