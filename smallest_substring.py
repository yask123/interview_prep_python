'''
Given two strings string1 and string2, find the smallest substring in string1 containing all
characters of string2 in O(n).
You need to return the output substring.
'''

print 'hello world'

word1 = "Looks for minimum string"
word2 = "mums"

char_map = [0] * 26

start_index = 0
end_index = 0

while end_index < len(word1):
	end_index += 1
