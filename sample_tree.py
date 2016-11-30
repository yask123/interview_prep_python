class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val


'''
		7
	2		 1
0      1 	     3
'''

a = Node(7)
a.right = Node(1)
a.right.right = Node(3)

a.left = Node(2)
a.left.left = Node(0)
a.left.right = Node(1)
