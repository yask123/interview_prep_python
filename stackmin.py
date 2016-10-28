class Node:
	def __init__(self, data = None):
		self.data = data
		self.next = None

class MinStack:
	def __init__(self,head = None):
		self.head = None
		self.min_items = []

	def push(self,data):
		if self.head == None:
			self.head = Node(data)
			self.min_items.append(data)

		else:
			new_node = Node(data)
			new_node.next = self.head
			self.head = new_node
			if data < self.min_items[-1]:
				self.min_items.append(data)

	def pop(self):
		if self.head:
			if self.head.data == self.min_items[-1]:
				self.min_items.pop()
			self.head = self.head.next

	def getMin(self):
		return self.min_items[len(self.min_items)-1]

ms = MinStack()
ms.push(4)
ms.push(2)
print ms.getMin()

ms.pop()
print ms.getMin()

