class Node:
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self,head):
		self.head = head

	def printall(self):
		current = self.head

		while current:
			print (current.data,'')
			current = current.next

b = Node(2)
a = Node(1,b)

ll = LinkedList(a)
ll.printall()
