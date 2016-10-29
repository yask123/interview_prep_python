class TrieNode:
	def __init__(self):
		self.links = [None] * 26
		self.is_end = False

	def add_link(self, character):
		new_trie_node = TrieNode()
		self.links[ord(character) - ord('a')] = new_trie_node

	def get_link(self, character):
		return self.links[ord(character) - ord('a')]


class Trie:
	def __init__(self):
		self.root = TrieNode()

	def add_word(self, word):
		current = self.root

		for each_char in word:
			if current.get_link(each_char) == None:
				current.add_link(each_char)

			current = current.get_link(each_char)
		current.is_end = True

	def search_word(self, word):
		current = self.root

		for each_char in word:
			if current.get_link(each_char) == None:
got 				return False
			current = current.get_link(each_char)
		if current.is_end == True:
			return True

		return False

	def words_with_prefixes(self, word):
		current = self.root
		for each_char in word:
			current = current.get_link(each_char)
			if current == None:
				return None
		self.dfs(current, '', word)

	def dfs(self, node, result, word):
		if node == None:
			return

		if node.is_end:
			print word + result

		for i in range(26):
			if (node.links[i] != None):
				self.dfs(node.links[i], result + chr(ord('a') + i), word)


my_trie = Trie()

my_trie.add_word('yask')
my_trie.add_word('yahoo')
my_trie.add_word('hello')
my_trie.words_with_prefixes('yah')
