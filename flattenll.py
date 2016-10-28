'''
1 - 2 -3 -4 - 5 - 6- 9 -> 8 - 3

'''

class Node:
	def __init__(self):
		self.data = None
		self.next = None
		self.child = None

def flatten(current):
	tail = find_tail(current)

	while current:
		if current.child:
			tail.next = current.child
			tail = find_tail(current.child)
		current = current.next

def find_tail(current):
	tail = None
	while current:
		tail = current
		current = current.next
	return tail
