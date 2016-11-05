from collections import deque


class Stack(object):
	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.first_queue = deque()
		self.second_queue = deque()

	def push(self, x):
		"""
		:type x: int
		:rtype: nothing
		"""
		if len(self.first_queue) == 0 and len(self.second_queue) == 0:
			self.first_queue.append(x)
		elif len(self.first_queue) == 0:
			self.second_queue.append(x)
		else:
			self.first_queue.append(x)

	def pop(self):
		"""
		:rtype: nothing
		"""
		if len(self.first_queue) == 0 and len(self.second_queue) == 0:
			raise Exception("Cant remove from empry stack")
		if len(self.first_queue) > 0:
			while len(self.first_queue) != 1:
				self.second_queue.append(self.first_queue.popleft())
			self.first_queue.popleft()
		else:
			while len(self.second_queue) != 1:
				self.first_queue.append(self.second_queue.popleft())
			self.second_queue.popleft()

	def top(self):
		"""
		:rtype: int
		"""
		if len(self.first_queue) == 0 and len(self.second_queue) == 0:
			raise Exception("Emptry stack")
		if len(self.first_queue) > 0:
			while len(self.first_queue) != 1:
				self.second_queue.append(self.first_queue.popleft())
			result = self.first_queue.popleft()
			self.second_queue.append(result)
			return result
		else:
			while len(self.second_queue) > 0:
				while len(self.second_queue) != 1:
					self.first_queue.append(self.second_queue.popleft())
				result = self.second_queue.popleft()
				self.first_queue.append(result)
				return result

	def empty(self):
		"""
		:rtype: bool
		"""
		if len(self.first_queue) == 0 and len(self.second_queue) == 0:
			return True
		return False


my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)

my_stack.pop()
my_stack.pop()
print my_stack.first_queue, ' - ', my_stack.second_queue
