class Node:
	def __init__(self, data=None):
		self.data = data
		self.prev = None
		self.next = None


class Deque:
	def __init__(self):
		self.front = None
		self.rear = None

	def append(self, data):
		new_node = Node(data)

		if self.front == None:
			self.front = new_node
			self.rear = new_node
		else:
			new_node.prev = self.front
			self.front.next = new_node
			self.front = new_node

	def append_left(self, data):
		new_node = Node(data)

		if self.front == None:
			self.front = new_node
			self.rear = new_node
		else:
			self.rear.prev = new_node
			new_node.next = self.rear
			self.rear = new_node

	def pop(self):
		if self.front == None:
			raise Exception("cant pop from empty dequeue")
		if self.front == self.rear:
			self.front = None
			self.rear = None
		else:
			self.front.prev.next = None
			self.front = self.front.prev

	def pop_left(self):
		if self.rear == None:
			raise Exception("cant pop from empty dequeue")

		if self.front == self.rear:
			self.front = None
			self.rear = None
		else:
			self.rear = self.rear.next

	def print_dequeue(self):
		current = self.rear

		while current:
			print current.data, '-->',
			current = current.next


a = Deque()
a.append(1)
a.append(2)
a.append(3)

a.pop()
a.pop()
a.pop()

a.append_left(1)
a.append_left(2)
a.append_left(3)

a.pop()
a.pop_left()
a.pop_left()

a.print_dequeue()
