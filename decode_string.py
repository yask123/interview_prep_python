'''
https://leetcode.com/problems/decode-string/

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''
string = '1 [ 3 [ a ] 2 [ b c ] ]'


def decode(string):
	string = string.split(' ')
	stack = []
	for each in string:
		if each != ']':
			stack.append(each)
		else:
			new_string = ''
			while len(stack) > 0 and stack[-1] != '[':
				new_string = stack.pop() + new_string
			stack.pop()
			freq = int(stack[-1])
			stack.pop()
			new_string = freq * new_string
			stack.append(new_string)
	return stack


print decode(string)
