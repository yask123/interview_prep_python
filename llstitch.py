
class Node:
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

def stitch(first, second):
	while first and second:
		ftemp = first.next
		stemp = second.next
		first.next = second
		second.next = ftemp
		first = ftemp
		second = stemp


a = Node(1)
b = Node(3)
a.next = b

c = Node(2)
d = Node(4)
c.next = d

stitch(a,c)

while a:
	print a.data
	a = a.next
