# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#    [1,[4,[6]]],
#        """

class NestedIterator(object):
	def __init__(self, nestedList):
		"""
		Initialize your data structure here.
		:type nestedList: List[NestedInteger]
		"""
		self.result = []
		self.nestedList = nestedList
		self.current_index = -1
		self.flat()

	def flat(self):
		self.nestedList = self._flatten_list(self.nestedList, self.nestedList)

	def _flatten_list(self, current_item, result):
		if current_item == None:
			return
		if type(current_item) == int:
			print result
			return

		for each_item in current_item:
			self._flatten_list(each_item, result)

	def next(self):
		"""
		:rtype: int
		"""
		self.current_index += 1
		return self.result[self.current_index]

	def hasNext(self):
		"""
		:rtype: bool
		"""
		if self.current_index == len(self.result) - 1:
			return False
		return True

	# Your NestedIterator object will be instantiated and called as such:
	# i, v = NestedIterator(nestedList), []
	# while i.hasNext(): v.append(i.next())


my_list = [[1, 1], 2, [1, 1]]
i, v = NestedIterator(my_list), []
while i.hasNext(): v.append(i.next())
print v
