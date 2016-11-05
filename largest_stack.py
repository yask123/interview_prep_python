class Stack:
	# initialize an empty list
	def __init__(self):
		self.items = []
		self.max_items = []

	# push a new item to the last index
	def push(self, item):
		if len(self.items) == 0 or item > self.max_items[-1] < item:
			self.max_items.append(item)
		self.items.append(item)

	# remove the last item
	def pop(self):
		# if the stack is empty, return None
		# (it would also be reasonable to throw an exception)
		if not self.items:
			return None
		if self.items[-1] == self.max_items[-1]:
			self.max_items.pop()
		return self.items.pop()

	# see what the last item is
	def peek(self):
		if not self.items:
			return None
		return self.items[-1]

	def get_max(self):
		if len(self.max_items):
			return self.max_items[-1]


my_max_stack = Stack()
my_max_stack.push(1)
my_max_stack.push(100)
my_max_stack.push(200)
my_max_stack.pop()
my_max_stack.pop()
print my_max_stack.get_max()
