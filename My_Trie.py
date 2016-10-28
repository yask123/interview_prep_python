class TrieNode:
    def __init__(self):
        self.links = [None]*26
        self.is_end = False

    def is_char_present(self, char):
        return self.links[ord('a') - ord(char)] != None

    def is_terminal(self):
        return self.is_end

    def set_terminal(self):
        self.is_end = True

    def get_node(self, char):
        return self.links[ord('a')-ord(char)]

    def add_node(self, char):
        self.links[ord['a'] - ord(char)] = char

class Trie:
    def __init__(self):
        self.root = TrieNode

    def insert_string(self, input_string):
        currnet = self.root
        index = 0
        while currnet.is_char_present(input_string[index]):
            currnet = currnet.get_node(input_string[index])
            index += 1

        currnet.add_node(c)
