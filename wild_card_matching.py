# coding=utf-8
'''
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
'''


def wild_card(word, pattern, word_index, pattern_index):
	if len(pattern) == pattern_index and len(word) == word_index:
		return True
	if len(pattern) == pattern_index or len(word) == word_index:
		return False

	if pattern[pattern_index] == '?':
		return wild_card(word, pattern, word_index + 1, pattern_index + 1)
	elif pattern[pattern_index] == '*':
		while word_index < len(word) - 1 and (word_index == 0 or word[word_index + 1] == word[word_index]):
			word_index += 1
		return wild_card(word, pattern, word_index + 1, pattern_index + 1)
	elif word[word_index] == pattern[pattern_index]:
		return wild_card(word, pattern, word_index + 1, pattern_index + 1)
	else:
		return False


print wild_card('abb', '?*', 0, 0)
