'''
https://www.hackerrank.com/challenges/reduced-string

Steve has a string, , consisting of  lowercase English alphabetic letters.
In one operation, he can delete any pair of adjacent letters with same value.
For example, string "aabcc" would become either "aab" or "bcc" after operation.

'''

a = 'yyyasskkk'


def reduce(input_string):
	input_string += ' '
	current_freq = 1
	for i in range(1, len(input_string)):

		if input_string[i - 1] != input_string[i]:
			if current_freq % 2 != 0:
				print input_string[i - 1],
			current_freq = 1
		else:
			current_freq += 1


reduce(a)
