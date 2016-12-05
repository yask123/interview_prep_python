'''
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
'''


def add_spaces(s, start_index, dict, count, result):
    if start_index == len(s):
        return True

    for i in range(start_index + 1, len(s)):
        if s[start_index:i + 1] in dict:
            if add_spaces(s, i + 1, dict, count + 1, result):
                result.append(i)
                return True
    return False


result = []
dict = ["cat", "cats", "and", "dog"]
s = "catsanddog"

add_spaces(s, 0, dict, 0, result)
print result
